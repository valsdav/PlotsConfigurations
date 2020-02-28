# example of configuration file
treeName= 'Events'


tag = 'wbindetalpt'
direc = "conf_wbindeta"

# used by mkShape to define output directory for root files
outputDir = 'rootFile_'+tag 

# file with TTree aliases
aliasesFile = direc+'/aliases.py'

# file with list of variables
variablesFile = direc+'/variables_detalpt.py'

# file with list of cuts
cutsFile = direc +'/cuts.py' 

# file with list of samples
samplesFile = direc+'/samples_detalpt.py' 

# file with list of samples
plotFile = direc+'/plot_detalpt.py' 



# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plot_'+tag


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards_'+tag


# structure file for datacard
structureFile = direc+'/structure_detalpt.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = direc+'/nuisances.py'
#nuisancesFile = direc+'/nuisances_datacard_detalpt.py'
