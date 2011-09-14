RETURNABLES = {
'AtomInchi':'Atom.inchi',
'AtomInchiKey':'Atom.inchikey',
'AtomIonCharge':'Atom.molecule.formalcharge',
#'AtomMass':'AtomState.',
'AtomMassNumber':'Atom.getMassNumber()',
#'AtomNuclearCharge':'AtomState.',
#'AtomNuclearSpin':'AtomState.',
'AtomSpeciesID':'Atom.id',
#'AtomStateCompositionComments':'AtomState.',
#'AtomStateConfigurationLabel':'AtomState.',
#'AtomStateCoupling':'AtomState.',
#'AtomStateDescription':'AtomState.',
'AtomStateEnergy':'AtomState.energy',
'AtomStateEnergyOrigin':'Zero-point energy',
'AtomStateEnergyUnit':'1/cm', 
#'AtomStateHyperfineConstantA':'AtomState.',
#'AtomStateHyperfineConstantB':'AtomState.',
#'AtomStateHyperfineMomentum':'AtomState.',
'AtomStateID':'AtomState.id',
#'AtomStateIonizationEnergy':'AtomState.',
#'AtomStateJ1':'AtomState.',
#'AtomStateJ2':'AtomState.',
#'AtomStateK':'AtomState.',
#'AtomStateKappa':'AtomState.',
#'AtomStateL':'AtomState.',
#'AtomStateLandeFactor':'AtomState.',
#'AtomStateLifeTime':'AtomState.',
#'AtomStateMagneticQuantumNumber':'AtomState.',
#'AtomStateMixingCoefficient':'AtomState.',
#'AtomStateParity':'AtomState.',
#'AtomStatePolarizability':'AtomState.',
#'AtomStateQuantumDefect':'AtomState.',
#'AtomStateRef':'AtomState.',
#'AtomStateS':'AtomState.',
#'AtomStateS2':'AtomState.',
#'AtomStateStatisticalWeight':'AtomState.',
'AtomStateTotalAngMom':'AtomState.qn1',
'AtomSymbol':'Atom.molecule.stoichiometricformula',

'MethodComment':'Method.description',
'MethodCategory':'Method.category', # <- NEW
'MethodDescription':'Method.description', # <- NEW
'MethodRef':'Method.ref',
'MethodID':'Method.id', # <- NEW
'MethodSourceRef':'Method.sourcesref', # <- NEW

'MoleculeChemicalName':'Molecule.molecule.trivialname',
'MoleculeID':'Molecule.id',
'MoleculeInchi':'Molecule.inchi',
'MoleculeInchiKey':'Molecule.inchikey',
'MoleculePartitionFunctionT':'Molecule.partitionfuncT',
'MoleculePartitionFunction':'Molecule.partitionfuncQ',
#'MoleculeMolecularWeight':'Molecule.',
#'MoleculeNormalModeHarmonicFrequency':'Molecule.',
#'MoleculeNormalModeIntensity':'Molecule.',
#'MoleculeNuclearSpins':'Molecule.',
#'MoleculeNuclearSpinsAtomArray':'Molecule.',
#'MoleculeNuclearSpinsBondArray':'Molecule.',
'MoleculeSpeciesID':'Molecule.id',
'MoleculeStructure': 'Molecule',    # we have an XML() method for this

#'MoleculeStateCharacLifeTime':'MoleculeState.',
#'MoleculeStateCharacNuclearSpinSymmetry':'MoleculeState.',
'MoleculeStateEnergy':'MoleculeState.energy',
'MoleculeStateEnergyOrigin':'Zero-point energy',
'MoleculeStateEnergyUnit':'1/cm', 
'MoleculeStateTotalStatisticalWeight':'MoleculeState.degeneracy', # has to be changed  <- new
'MoleculeStateNuclearSpinIsomer':'MoleculeState.nuclearspinisomer',
'MoleculeStateNuclearStatisticalWeight':'MoleculeState.nuclearstatisticalweight',
'MoleculeStateID':'MoleculeState.id',
#'MoleculeStateQuantumNumbers':'MoleculeState.parsed_qns',
'MoleculeStateQuantumNumbers':'MoleculeState',
'MoleculeStoichiometricFormula':'Molecule.molecule.stoichiometricformula',
'MoleculeOrdinaryStructuralFormula':'Molecule.isotopolog',
'MoleculeComment': 'Molecule.name',
'MoleculeQnStateID': 'MolQN.stateid', # <- new
'MoleculeQnCase': 'MolQN.case',       # <- new 
'MoleculeQnLabel': 'MolQN.label',     # <- new 
'MoleculeQnValue': 'MolQN.value',     # <- new
'MoleculeQnAttribute': 'MolQN.attribute', # <- new
#'MoleculeQnXML': 'MolQN.xml',  #

'NodeID':'CDMS',

#'NonRadTranEnergy':'',
#'NonRadTranProbability':'',
#'NonRadTranWidth':'',
#'NormalModeHarmonicFrequency':'Molecule.',
#'NormalModeIntensity':'Molecule.',
#'NormalModeSymmetry':'Molecule.',
#'RadTransBandCentre':'RadTran.',
#'RadTransBandWidth':'RadTran.',
#'RadTransBroadeningComment':'RadTran.',
#'RadTransBroadeningInstrumentLineshapeName':'RadTran.',
#'RadTransBroadeningInstrumentLineshapeParameter':'RadTran.',
#'RadTransBroadeningInstrumentLineshapeParameterName':'RadTran.',
#'RadTransBroadeningInstrumentRef':'RadTran.',
#'RadTransBroadeningNaturalLineshapeName':'RadTran.',
#'RadTransBroadeningNaturalLineshapeParameter':'RadTran.',
#'RadTransBroadeningNaturalLineshapeParameterName':'RadTran.',
#'RadTransBroadeningNaturalRef':'RadTran.',
#'RadTransBroadeningRef':'RadTran.',
#'RadTransBroadeningStarkLineshapeName':'RadTran.',
#'RadTransBroadeningStarkLineshapeParameter':'RadTran.',
#'RadTransBroadeningStarkLineshapeParameterName':'RadTran.',
#'RadTransBroadeningStarkRef':'RadTran.',
#'RadTransBroadeningVanDerWaalsLineshapeName':'RadTran.',
#'RadTransBroadeningVanDerWaalsLineshapeParameter':'RadTran.',
#'RadTransBroadeningVanDerWaalsLineshapeParameterName':'RadTran.',
#'RadTransBroadeningVanDerWaalsRef':'RadTran.',
#'RadTransComments':'RadTran.',
#'RadTransEffectiveLandeFactor':'RadTran.',
#'RadTransEnergy':'RadTran.',
'RadTransFinalStateRef':'RadTran.upperstateref_id',
'RadTransInitialStateRef':'RadTran.lowerstateref_id',
'RadTransFrequency':'RadTran.frequency',
'RadTransFrequencyUnit':'RadTran.unit',
'RadTransFrequencyAccuracy':'RadTran.uncertainty',
#'RadTransFrequencyRef':'RadTran.freqmethodref_id',
#'RadTransFrequencyMethod':'RadTran.freqmethodref_id',
'RadTransFrequencyMethod':'RadTran.species_id',
'RadTransProbabilityA':'RadTran.einsteina',
'RadTransProbabilityAUnit':'1/cm', # <-New
#'RadTransProbabilityIdealisedIntensity':'RadTran.',
#'RadTransProbabilityLineStrength':'RadTran.',
'RadTransProbabilityLog10WeightedOscillatorStrength':'RadTran.intensity',
'RadTransProbabilityMultipole':'E2',
#'RadTransProbabilityOscillatorStrength':'RadTran.',
#'RadTransProbabilityWeightedOscillatorStrength':'RadTran.',
#'RadTransRefs':'RadTran.',
#'RadTransSpeciesRef':'RadTran.',
#'RadTransWavelength':'RadTran.',
#'RadTransWavenumber':'RadTran.',

'SourceAuthorName':'Source.getAuthorList()',
'SourceCategory':'Source.category',
'SourceID':'Source.rId',
'SourceName':'Source.name',
'SourcePageBegin':'Source.pageBegin',
'SourcePageEnd':'Source.pageEnd',
#'SourceTitle':'Source.title',
#'SourceURI':'Source.',
'SourceVolume':'Source.vol',
'SourceYear':'Source.year',
}


# import the unit converter functions
from vamdctap.unitconv import *

RESTRICTABLES = { 
#'AsOfDate':'',
#'AtomInchi':'',
#'AtomInchiKey':'',
#'AtomIonCharge':'',
#'AtomMass':'',
#'AtomMassNumber':'',
#'AtomNuclearCharge':'',
#'AtomNuclearSpin':'',
#'AtomStateCoupling':'',
#'AtomStateEnergy':'',
#'AtomStateHyperfineMomentum':'',
#'AtomStateID':'',
#'AtomStateIonizationEnergy':'',
#'AtomStateKappa':'',
#'AtomStateLandeFactor':'',
#'AtomStateLifeTime':'',
#'AtomStateMagneticQuantumNumber':'',
#'AtomStateMixingCoefficient':'',
#'AtomStateParity':'',
#'AtomStatePolarizability':'',
#'AtomStateQuantumDefect':'',
#'AtomStateStatisticalWeight':'',
#'AtomSymbol':'',
'MoleculeInchiKey':'species__inchikey',
'MoleculeChemicalName':'species__molecule__trivialname',
#'MoleculeMolecularWeight':'',
#'MoleculeNormalModeHarmonicFrequency':'',
#'MoleculeNormalModeIntensity':'',
#'MoleculeStateCharacLifeTime':'',
#'MoleculeStateCharacNuclearSpinSymmetry':'',
'MoleculeStateNuclearSpinIsomer':'lowerstateref__nuclearspinisomer',
'MoleculeStateEnergy':'lowerstateref__energy',
#'MoleculeStateID':'',
'MoleculeStoichiometricFormula':'species__molecule__stoichiometricformula',
'MoleculeOrdinaryStructuralFormula':'species__isotopolog',
#'NonRadTranEnergy':'',
#'NonRadTranProbability':'',
#'NonRadTranWidth':'',
#'NormalModeSymmetry':'',
#'RadTransBandCentre':'',
#'RadTransBandWidth':'',
#'RadTransEffectiveLandeFactor':'',
'RadTransEnergy':('frequency',eV2MHz),
'RadTransFrequency':'frequency',
#'RadTransProbabilityA':'RadTran.einsteinA',
#'RadTransProbabilityIdealisedIntensity':'',
#'RadTransProbabilityLineStrength':'',
#'RadTransProbabilityLog10WeightedOscillatorStrength':'',
#'RadTransProbabilityOscillatorStrength':'',
#'RadTransProbabilityWeightedOscillatorStrength':'',
'RadTransWavelength':('frequency',Angstr2MHz),
#'RadTransWavelength':'frequency',
'RadTransWavenumber':('frequency',invcm2MHz),
#'SourceCategory':'',
#'SourceYear':'',
'MoleculeSpeciesID':'species',
}

CDMSONLYRESTRICTABLES = {
# 'MoleculeSpeciesID':'species',
 'dataset':'dataset',
 'hfsflag':'hfsflag',
}
