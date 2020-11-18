#!/bin/bash

## FIXME this is where the Combine framework is installed
cd /afs/cern.ch/work/r/rceccare/VBF/CMSSW_10_2_13
eval `scramv1 runtime -sh`
cd -

## work directory
workdir=/afs/cern.ch/work/r/rceccare/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBF/Keras_2016_v6

cd $workdir



#echo "class0:" "">> significance_class0_30_10_fdm_vbf.txt
#combine -M Significance class0_30_10_fdm_vbf.root -t -1 --setParameters r_vbf=1 --redefineSignalPOIs=r_vbf >> significance_class0_30_10_fdm_vbf.txt

#echo "class0:" "">> significance_class0_30_10_multicut_cat_cross.txt
#combine -M Significance class0_30_10_multicut_cat_cross.root -t -1 --setParameters r_vbf=1 --redefineSignalPOIs=r_vbf >> significance_class0_30_10_multicut_cat_cross.txt

#echo "class0:" "">> significance_class0_27_09_cuts.txt
#combine -M Significance class0_27_09_cuts.root -t -1 --setParameters r_vbf=1 --redefineSignalPOIs=r_vbf >> significance_class0_27_09_cuts.txt

echo "class0:" "">> significance_class0_15_11_quad_multicut.txt
combine -M Significance class0_15_11_quad_multicut.root -t -1 --setParameters r_vbf=1 --redefineSignalPOIs=r_vbf --freezeParameters THU_ggH_Mu,THU_ggH_Res,THU_ggH_Mig01,THU_ggH_Mig12,THU_ggH_VBF2j,THU_ggH_VBF3j,THU_ggH_PT60,THU_ggH_PT120,THU_ggH_qmtop >> significance_class0_15_11_quad_multicut.txt

