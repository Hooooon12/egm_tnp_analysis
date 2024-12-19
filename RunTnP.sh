#!/bin/bash

# POG reproduction
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingTight94XV2 --checkBins
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingTight94XV2 --createBins
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingTight94XV2 --createHists
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingTight94XV2 --doFit
#
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingTight94XV2 --doFit --mcSig --altSig
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingTight94XV2 --doFit --altSig
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingTight94XV2 --doFit --altBkg
#
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingTight94XV2 --sumUp

#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingMedium94XV2 --checkBins
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingMedium94XV2 --createBins
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingMedium94XV2 --createHists
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingTight94XV2 --doFit
#
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingTight94XV2 --doFit --mcSig --altSig
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingTight94XV2 --doFit --altSig
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingTight94XV2 --doFit --altBkg
#
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingTight94XV2 --sumUp


# Use SKFlat tree
#pushd /data6/Users/jihkim/egm_tnp_analysis
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingCutBasedTight94XV2 --checkBins
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingCutBasedTight94XV2 --createBins
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingCutBasedTight94XV2 --createHists
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingCutBasedTight94XV2 --doFit
#
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingCutBasedTight94XV2 --doFit --mcSig --altSig
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingCutBasedTight94XV2 --doFit --altSig
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingCutBasedTight94XV2 --doFit --altBkg
#
#python tnpEGM_fitter.py etc/config/settings_ele_HNL2017.py --flag passingCutBasedTight94XV2 --sumUp

# use python
python create-batch.py -e 2017 -f passingCutBasedTight94XV2
python create-batch.py -e 2017 -f passingHNLMVA
python create-batch.py -e 2017 -f passingHNLMVAFake
python create-batch.py -e 2017 -f passingHNLMVACF
python create-batch.py -e 2017 -f passingHNLMVAConv
python create-batch.py -e 2017 -f passingHNLMVA_TrkIso
python create-batch.py -e 2017 -f passingMVALoose
python create-batch.py -e 2017 -f passingHEEP
python create-batch.py -e 2017 -f passingHNLHeep
python create-batch.py -e 2017 -f passingTriggerEmul
