# example of configuration file

tag = 'DY'


# used by mkShape to define output directory for root files
outputDir = 'rootFile'


# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples.py' 

# file with list of samples
plotFile = 'plot.py' 



# luminosity to normalize to (in 1/fb)
# luminosity to normalize to (in 1/fb)
#lumi = 0.805
#lumi = 4.3
#lumi = 6.264
#lumi = 12.2950
#lumi = 12.8890
lumi = 35.9


# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'DYtt'


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards'


# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
# nuisancesFile = 'nuisances.py'
nuisancesFile = 'nuisances_light.py'


