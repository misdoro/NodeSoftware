#
#rewrite of update_functions.py
#

from datetime import datetime

from models import *

import vamdclib.query     as vl_query
import vamdclib.results   as vl_results
import vamdclib.request   as vl_request
import vamdclib.nodes     as vl_registry
import vamdclib.specmodel as vl_specmodel

#Do not use vamdclib.inchi as it seems to be buggy
import traceback,sys



def update_nodes():
  """
  #Search for nodes in the registry, update or create records in the database
  """
  
  print "query the registry for active nodes"
  nodelist=vl_registry.Nodelist()
  ivoaids=[]
  nowtime=datetime.now()
    
  #Add new nodes or update the existing ones
  for node in nodelist:
      db_node, created = VamdcNodes.objects.get_or_create(ivo_identifier = node.identifier)
      if created:
        print "Adding new node "+node.identifier+" nn"+node.name+" nu"+node.url+" em"+node.maintainer+"\n"
        db_node.short_name = node.name
        db_node.contact_email = node.maintainer
        db_node.status=0
        db_node.last_update_date = nowtime
      else:
        print "Updating the node information for "+db_node.short_name
        db_node.contact_email = node.maintainer
        db_node.last_update_date = nowtime
      db_node.save()
      
      
      
def query_active_nodes():
    """
    #Update species for nodes that are marked active
    """
    vl_nl=vl_registry.Nodelist()
    for db_node in VamdcNodes.objects.filter( status = RecordStatus.ACTIVE ):
       try:
         vl_node=vl_nl.getnode(db_node.ivo_identifier)
         print "Process species for node "+vl_node.name
         load_species(vl_node)
       except Exception, e:
         exc_type, exc_value, exc_traceback = sys.exc_info()
         print "failed to process the node %s (%s)"%(db_node.short_name,db_node.ivo_identifier)
         traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=5, file=sys.stdout)
         

def load_species(vl_node):
    """
    Load and update node species
    """
    #---------------------------------------------------------------------------------
    # Retrieve the data from the node using SELECT SPECIES
    vl_atoms, vl_molecules = get_species(vl_node)
    db_node=VamdcNodes.objects.get(ivo_identifier = vl_node.identifier)
    
    #Update or insert the atoms in the database
    
    for atomid in vl_atoms:
      vl_atom = vl_atoms[atomid]
      db_atom=update_atom(vl_atom,db_node)
      update_species_in_node(db_node,db_atom,vl_atom)
    
    #Update or insert the molecules
    #for moleculeid in vl_molecules:
    #  vl_molecule = vl_molecules[moleculeid]
    #  update_molecule(vl_molecule,db_node)
    
    

def update_atom(vl_atom,db_node):
    """
    Insert or update the atom record, coming for the node
    """
    speciesid=vl_atom.VAMDCSpeciesID
    try:
      massnumber=vl_atom.MassNumber
    except:
      db_dict_atom=VamdcDictAtoms.objects.get(symbol=vl_atom.ChemicalElementSymbol,most_abundant=1)
      massnumber=db_dict_atom.mass_number
    
    db_atom, created = VamdcSpecies.objects.get_or_create(
      defaults={
        'origin_member_database':db_node,
        'mass_number':massnumber,
        'charge':vl_atom.IonCharge,
      },
      id = speciesid,
      )
    if created:
      db_atom.inchi=vl_atom.InChI
      db_atom.inchikey = vl_atom.InChIKey
      db_atom.stoichiometric_formula = vl_atom.ChemicalElementSymbol
      db_atom.mass_number = massnumber
      db_atom.charge = vl_atom.IonCharge
      db_atom.species_type = SpeciesType.ATOM
      db_atom.status = RecordStatus.NEW
      db_atom.origin_member_database = db_node
      print ("adding atom %s %s"%(db_atom.stoichiometric_formula,db_atom.charge))
      db_atom.save()    
    else:
      print ("found atom %s %d"%(db_atom.stoichiometric_formula,db_atom.charge))
      
    return db_atom
  
  
def update_species_in_node(db_node,db_species,vl_species):
    """
    Insert or update the information on the species contained in the node
    """
    db_nodeSpecies, created = VamdcNodeSpecies.objects.get_or_create(
      species=db_species,
      member_database=db_node,
      database_species_id=vl_species.SpeciesID)
    
    if not created:
      db_nodeSpecies.last_seen_dateTime=datetime.now()
      db_nodeSpecies.save()
      
      
    
  
def get_species(vl_node):
    """
    Retrieves a dictionary with species available at the specified node

    nodename: short_name of the node, which is stored in the database
    """

    #------------------------------------------------------------------
    # Query data from the node via SELECT SPECIES
    query = vl_query.Query()
    request = vl_request.Request()

    query_string = "SELECT SPECIES"
    #query_string = "SELECT SPECIES WHERE ((InchiKey!='UGFAIRIUMAVXCW'))" 
    request.setnode(vl_node)
    request.setquery(query_string)

    result = request.dorequest()
    
    try:
        result.populate_model()
    except:
        print " Error: Could not process data "
    #------------------------------------------------------------------
    # Return Molecules and Atoms

    Molecules = result.data['Molecules']
    Atoms = result.data['Atoms']

    return Atoms, Molecules
  
  
