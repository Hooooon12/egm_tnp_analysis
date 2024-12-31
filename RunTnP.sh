#!/bin/bash

#python create-batch.py -c ID -e 2017 -f passingCutBasedTight94XV2
#python create-batch.py -c ID -e 2017 -f passingHNLMVA
#python create-batch.py -c ID -e 2017 -f passingHNLMVAFake
#python create-batch.py -c ID -e 2017 -f passingHNLMVACF
#python create-batch.py -c ID -e 2017 -f passingHNLMVAConv
#python create-batch.py -c ID -e 2017 -f passingHNLMVA_TrkIso
#python create-batch.py -c ID -e 2017 -f passingMVALoose
#python create-batch.py -c ID -e 2017 -f passingHEEP
#python create-batch.py -c ID -e 2017 -f passingHNLHeep
#python create-batch.py -c ID -e 2017 -f passingTriggerEmul

#python create-batch.py -c ID -e 2016preVFP 2016postVFP 2017 2018 -f passingHNLMVA passingHEEP
#python create-batch.py -c Trig -e 2016preVFP 2016postVFP 2017 2018 -f HLTEl23 HLTEl12
python create-batch.py -c Trig -e 2016preVFP -f HLTEl23 HLTEl12
