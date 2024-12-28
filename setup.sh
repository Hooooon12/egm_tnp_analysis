#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /cvmfs/cms.cern.ch/slc7_amd64_gcc900/cms/cmssw/CMSSW_11_2_5
cmsenv
cd -
mkdir -p log
make
