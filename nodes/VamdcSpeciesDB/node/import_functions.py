#
# rewrite of update_functions.py
#

from datetime import datetime
from models import *
import vamdclib.query     as vl_query
import vamdclib.results   as vl_results
import vamdclib.request   as vl_request
import vamdclib.nodes     as vl_registry
import vamdclib.specmodel as vl_specmodel
# Do not use vamdclib.inchi as it seems to be buggy
from node.InchiInfo import InchiInfo
import traceback, sys
from pprint import pprint


def update_nodes():
    """
    #Search for nodes in the registry, update or create records in the database
    """

    print "query the registry for active nodes"
    nodelist = vl_registry.Nodelist()
    nowtime = datetime.now()

    # Add new nodes or update the existing ones
    for node in nodelist:
        db_node, created = VamdcNodes.objects.get_or_create(ivo_identifier=node.identifier)
        if created:
            print "Adding new node " + node.identifier + " nn" + node.name + " nu" + node.url + " em" + node.maintainer + "\n"
            db_node.short_name = node.name
            db_node.contact_email = node.maintainer
            db_node.status = RecordStatus.NEW
            db_node.last_update_date = nowtime
        else:
            print "Updating the node information for " + db_node.short_name
            db_node.contact_email = node.maintainer
            db_node.last_update_date = nowtime
        db_node.save()


def query_active_nodes():
    """
    #Update species for nodes that are marked active
    """
    vl_nl = vl_registry.Nodelist()
    for db_node in VamdcNodes.objects.filter(status=RecordStatus.ACTIVE):
        try:
            vl_node = vl_nl.getnode(db_node.ivo_identifier)
            print "Process species for node " + vl_node.name
            load_species(vl_node)
        except Exception, e:
            print "failed to process the node %s (%s)" % (db_node.short_name, db_node.ivo_identifier)
            traceback.print_exc(file=sys.stdout)


def load_species(vl_node):
    """
    Load and update node species
    """
    # ---------------------------------------------------------------------------------
    # Retrieve the data from the node using SELECT SPECIES
    vl_atoms, vl_molecules = get_species(vl_node)
    db_node = VamdcNodes.objects.get(ivo_identifier=vl_node.identifier)

    # Update or insert the atoms in the database
    for atomid in vl_atoms:
        vl_atom = vl_atoms[atomid]
        try:
            verify_atom(vl_atom)
            db_atom = update_atom(vl_atom, db_node)
            update_species_in_node(db_node, db_atom, vl_atom)
        except Exception, e:
            print "Failed to load atom:", e
            pprint(vl_atom)
            # print sys.exc_info()[0]
            # traceback.print_exc(file=sys.stdout)

    # Update or insert the molecules
    for moleculeid in vl_molecules:
        vl_molecule = vl_molecules[moleculeid]
        try:
            vl_molecule = verify_molecule(vl_molecule)
            db_molecule = update_molecule(vl_molecule, db_node)
            update_species_in_node(db_node, db_molecule, vl_molecule)
        except  Exception, e:
            print "Failed to load molecule:", e
            pprint(vl_molecule)
            traceback.print_exc(file=sys.stdout)


def verify_atom(vl_atom):
    speciesid = vl_atom.VAMDCSpeciesID
    if speciesid is None or len(speciesid) < 27:
        raise ValueError("Bad speciesid for atom '%s'" % vl_atom.ChemicalElementSymbol)
    symbol = vl_atom.ChemicalElementSymbol
    try:
        atom = VamdcDictAtoms.objects.filter(symbol=symbol)
        if len(atom) == 0:
            raise ValueError("Atom '%s' not found in the atoms dictionary." % symbol)
    except:
        raise ValueError("Atom '%s' not found in the atoms dictionary." % symbol)
    return vl_atom


def update_atom(vl_atom, db_node):
    """
    Insert or update the atom record, coming for the node

    Args:
        vl_atom (vamdclib atom):
    """
    speciesid = vl_atom.VAMDCSpeciesID

    try:
        massnumber = vl_atom.MassNumber
    except:
        try:
            db_dict_atom = VamdcDictAtoms.objects.get(symbol=vl_atom.ChemicalElementSymbol, most_abundant=1)
            massnumber = db_dict_atom.mass_number
        except:
            massnumber = 0

    db_atom, created = VamdcSpecies.objects.get_or_create(
        defaults={
            'origin_member_database': db_node,
            'mass_number': massnumber,
            'charge': vl_atom.IonCharge,
        },
        id=speciesid,
    )
    if created:
        db_atom.inchi = vl_atom.InChI
        db_atom.inchikey = vl_atom.InChIKey
        db_atom.stoichiometric_formula = vl_atom.ChemicalElementSymbol
        db_atom.species_type = SpeciesType.ATOM
        db_atom.status = RecordStatus.NEW
        print ("adding atom %s %s" % (db_atom.stoichiometric_formula, db_atom.charge))
        db_atom.save()
    else:
        print ("found atom %s %d" % (db_atom.stoichiometric_formula, db_atom.charge))

    return db_atom


def verify_molecule(vl_molecule):
    speciesid = vl_molecule.VAMDCSpeciesID

    if speciesid is None or len(speciesid) < 27:
        speciesid = vl_molecule.InChIKey
        #TODO: handle multiple inchikeys/conformers here?
        if speciesid is None or len(speciesid) < 27:
            raise ValueError("Bad speciesid for molecule '%s'" % vl_molecule.StoichiometricFormula)

    vl_molecule.VAMDCSpeciesID = speciesid

    try:
        inchiinfo = InchiInfo(vl_molecule.InChI)
    except:
        print ("Unable to load the inchi information for molecule '%s'" %vl_molecule.StoichiometricFormula )
        traceback.print_exc(file=sys.stdout)
        inchiinfo = None

    try:
        mass = int(round(float(vl_molecule.MolecularWeight)))
    except:
        if (inchiinfo is None):
            mass = 0
            print ("Warning: no molecular mass information and no inchi present, setting weight to zero")
        else:
            mass = int(inchiinfo.weight)
    if (inchiinfo is not None and int(inchiinfo.weight) <> mass):
        print (
        "Warning: molecular weight from Inchi (%d) does not match the XSAMS weight %d" % (int(inchiinfo.weight), mass))
    vl_molecule.MolecularWeight = mass

    try:
        charge = int(vl_molecule.IonCharge)
    except:
        if (inchiinfo is None):
            charge = 0
            print ("Warning: no charge information and no inchi present, setting charge to zero")
        else:
            charge = inchiinfo.totalCharge
    if (inchiinfo is not None and inchiinfo.totalCharge <> charge):
        print ("Warning: charge from Inchi (%d) does not match XSAMS charge %d" % (inchiinfo.totalCharge, charge))
    vl_molecule.IonCharge=charge

    return vl_molecule


def update_molecule(vl_molecule, db_node):
    speciesid = vl_molecule.VAMDCSpeciesID
    molecularweight = vl_molecule.MolecularWeight
    charge = vl_molecule.IonCharge

    db_molecule, created = VamdcSpecies.objects.get_or_create(
        defaults={
            'origin_member_database': db_node,
            'mass_number': molecularweight,
            'charge': charge,
        },
        id=speciesid,
    )

    if created:
        db_molecule.inchi = vl_molecule.InChI
        db_molecule.inchikey = vl_molecule.InChIKey
        db_molecule.stoichiometric_formula = vl_molecule.StoichiometricFormula
        db_molecule.species_type = SpeciesType.MOLECULE
        db_molecule.status = RecordStatus.NEW
        print ("adding molecule %s %s" % (db_molecule.stoichiometric_formula, db_molecule.charge))
        db_molecule.save()
    else:
        print ("found molecule %s %d" % (db_molecule.stoichiometric_formula, db_molecule.charge))

    assert isinstance(db_molecule, VamdcSpecies)
    return db_molecule


def update_species_in_node(db_node, db_species, vl_species):
    """
    Insert or update the information on the species contained in the node
    """
    db_nodeSpecies, created = VamdcNodeSpecies.objects.get_or_create(
        species=db_species,
        member_database=db_node,
        database_species_id=vl_species.SpeciesID)

    if not created:
        db_nodeSpecies.last_seen_dateTime = datetime.now()
        db_nodeSpecies.save()


def get_species(vl_node):
    """
    Retrieves a dictionary with species available at the specified node

    """

    # ------------------------------------------------------------------
    # Query data from the node via SELECT SPECIES
    query = vl_query.Query()
    request = vl_request.Request()

    query_string = "SELECT SPECIES"
    # query_string = "SELECT SPECIES WHERE ((InchiKey!='UGFAIRIUMAVXCW'))"
    request.setnode(vl_node)
    request.setquery(query_string)

    result = request.dorequest()

    try:
        result.populate_model()
    except:
        print " Error: Could not process data "
    # ------------------------------------------------------------------
    # Return Molecules and Atoms
    try:
        molecules = result.data['Molecules']
    except:
        molecules = []
    try:
        atoms = result.data['Atoms']
    except:
        atoms = []

    return atoms, molecules
