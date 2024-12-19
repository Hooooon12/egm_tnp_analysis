# python create-batch.py -e 2017 -f passingCutBasedTight94XV2

import os, sys
import commands as cmd
import argparse

parser = argparse.ArgumentParser(description='option')
parser.add_argument('-e', dest='eras', nargs='+') # take args as a list, return error when there is no arg
parser.add_argument('-f', dest='flags', nargs='+') # take args as a list, return error when there is no arg # passingCutBasedTight94XV2
args = parser.parse_args()

pwd = os.getcwd()
CMSSW_BASE = os.environ['CMSSW_BASE']
SCRAM_ARCH = os.environ['SCRAM_ARCH']

if not "CMSSW_11_2_5" in CMSSW_BASE:
  print "[!!ERROR!!] Please set a proper CMSSW version"
  print "[!!ERROR!!] Current version:",CMSSW_BASE
  print "Exiting ..."
  sys.exit(1)

for era in args.eras:
  for flag in args.flags:
    with open(pwd+"/log/runHNL"+era+"_"+flag+".sh",'w') as runfile:
      runfile.write("#!/bin/bash\n")
      runfile.write("pushd "+pwd+"\n")
      runfile.write("python tnpEGM_fitter.py etc/config/settings_ele_HNL"+era+".py --flag "+flag+" --checkBins\n"             ) 
      runfile.write("python tnpEGM_fitter.py etc/config/settings_ele_HNL"+era+".py --flag "+flag+" --createBins\n"            )     
      runfile.write("python tnpEGM_fitter.py etc/config/settings_ele_HNL"+era+".py --flag "+flag+" --createHists\n"           )     
      runfile.write("python tnpEGM_fitter.py etc/config/settings_ele_HNL"+era+".py --flag "+flag+" --doFit\n"                 )        
      runfile.write("python tnpEGM_fitter.py etc/config/settings_ele_HNL"+era+".py --flag "+flag+" --doFit --mcSig --altSig\n")   
      runfile.write("python tnpEGM_fitter.py etc/config/settings_ele_HNL"+era+".py --flag "+flag+" --doFit --altSig\n"        )    
      runfile.write("python tnpEGM_fitter.py etc/config/settings_ele_HNL"+era+".py --flag "+flag+" --doFit --altBkg\n"        ) 
      runfile.write("python tnpEGM_fitter.py etc/config/settings_ele_HNL"+era+".py --flag "+flag+" --sumUp\n"                 )

    with open(pwd+"/log/submitHNL"+era+"_"+flag+".sh",'w') as submitfile:
      submitfile.write("universe = vanilla\n")
      submitfile.write("getenv   = True\n")
      submitfile.write("should_transfer_files = YES\n")
      submitfile.write("when_to_transfer_output = ON_EXIT\n")
      submitfile.write("request_memory = 24000\n")
      submitfile.write("executable = "+pwd+"/log/runHNL"+era+"_"+flag+".sh\n")
      submitfile.write("log =        "+pwd+"/log/runHNL"+era+"_"+flag+".log\n")
      submitfile.write("output =     "+pwd+"/log/runHNL"+era+"_"+flag+".out\n")
      submitfile.write("error =      "+pwd+"/log/runHNL"+era+"_"+flag+".err\n")
      submitfile.write("queue\n")

    os.system("condor_submit "+pwd+"/log/submitHNL"+era+"_"+flag+".sh -batch-name tnpEGM_"+era+"_"+flag)
