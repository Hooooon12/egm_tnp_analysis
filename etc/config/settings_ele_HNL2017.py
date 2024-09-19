#############################################################
########## General settings
#############################################################
# flag to be Tested
cutpass80 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.967083,0.929117,0.726311)
cutpass90 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.913286,0.805013,0.358969)

# flag to be Tested
flags = {
    'passingVeto94XV2'    : '(passingVeto94XV2   == 1)',
    'passingLoose94XV2'   : '(passingLoose94XV2  == 1)',
    'passingMedium94XV2'  : '(passingMedium94XV2 == 1)',
    'passingTight94XV2'   : '(passingTight94XV2  == 1)',
    'passingCutBasedTight94XV2'   : '(passingCutBasedTight94XV2)', #JH : SKFlat variable
    'passingHNLMVA'   : '(passingHNLMVA)', #JH : SKFlat variable
    'passingMVA94Xwp80isoV2' : '(passingMVA94Xwp80isoV2 == 1)',
    'passingMVA94Xwp90isoV2' : '(passingMVA94Xwp90isoV2 == 1)',
    'passingMVA94Xwp80noisoV2' : '(passingMVA94Xwp80noisoV2 == 1)',
    'passingMVA94Xwp90noisoV2' : '(passingMVA94Xwp90noisoV2 == 1)',
    'passingMVA94XwpLisoV2'    : '(passingMVA94XwpLisoV2 == 1)',
    'passingMVA94XwpLnoisoV2'  : '(passingMVA94XwpLnoisoV2 == 1)',
    'passingMVA94XwpHZZisoV2'  : '(passingMVA94XwpHZZisoV2 == 1)',
    }

#baseOutDir = 'results/UL2017_HNL/tnpEleID/' #JH : This used POG trees as the input
#baseOutDir = 'results/UL2017_HNL_SKFlat/tnpEleID/' #JH : This will use our tree from SkimTree_EGamma
#baseOutDir = 'results/UL2017_HNL_SKFlat_TrigCut/tnpEleID/' #JH : This will use our tree from SkimTree_EGamma
#baseOutDir = 'results/UL2017_NewTree_HNL_SKFlat_TrigCut/tnpEleID/' #JH : This will use our tree from SkimTree_EGamma_HEEP
#baseOutDir = 'results/UL2017_OldTree_HNL_SKFlat_TrigCut/tnpEleID/' #JH : Data from SkimTree_Egamma, mc from SkimTree_Egamma_HEEP
#baseOutDir = 'results/UL2017_OldDataMCTree_HNL_SKFlat_TrigCut/tnpEleID/' #JH : Data, mc from Skimtree_EGamma
#baseOutDir = 'results/UL2017_NewDataOldMCTree_HNL_SKFlat_TrigCut/tnpEleID/' #JH : Data from Skimtree_EGamma_HEEP, MC from Skintree_EGamma
#baseOutDir = 'results/UL2017_NewDataOldMCTree_HNL_SKFlat_TrigCut_EtaCut/tnpEleID/' #JH : Data from Skimtree_EGamma_HEEP, MC from Skintree_EGamma, trigger cut to low pt, and fix eta cut referring to : https://github.com/swagata87/EgammaAnalysis-TnPTreeProducer/blob/Nm1_UL_106X/python/TnPTreeProducer_cfg.py#L117, later add TightId to tag see https://github.com/swagata87/EgammaAnalysis-TnPTreeProducer/blob/Nm1_UL_106X/python/egmElectronIDModules_cff.py#L307-L312
baseOutDir = 'results/UL2017_NewDataNewMCTree_HNL_SKFlat_TrigCut_240919/tnpEleID/' #JH : Data from Skimtree_EGamma_HEEP, MC from Skintree_EGamma, trigger cut to low pt, and finally matched to https://github.com/swagata87/EgammaAnalysis-TnPTreeProducer/blob/Nm1_UL_106X/python/TnPTreeProducer_cfg.py

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'tnpEleIDs'

samplesDef = {
    #'data'   : tnpSamples.UL2017['data_Run2017B'].clone(),
    #'data'   : tnpSamples.UL2017['data_Run2017'].clone(), #JH
    #'mcNom'  : tnpSamples.UL2017['DY_madgraph'].clone(),
    #'mcAlt'  : tnpSamples.UL2017['DY_amcatnloext'].clone(),
    #'tagSel' : tnpSamples.UL2017['DY_madgraph'].clone(),
    'data'   : tnpSamples.HNL2017['data_Run2017B'].clone(),
    'mcNom'  : tnpSamples.HNL2017['DY_madgraph'].clone(),
    'mcAlt'  : tnpSamples.HNL2017['DY_amcatnloext'].clone(),
    'tagSel' : tnpSamples.HNL2017['DY_madgraph'].clone(), #JH
}

## can add data sample easily
#samplesDef['data'].add_sample( tnpSamples.UL2017['data_Run2017C'] )
#samplesDef['data'].add_sample( tnpSamples.UL2017['data_Run2017D'] )
#samplesDef['data'].add_sample( tnpSamples.UL2017['data_Run2017E'] )
#samplesDef['data'].add_sample( tnpSamples.UL2017['data_Run2017F'] )
samplesDef['data'].add_sample( tnpSamples.HNL2017['data_Run2017C'] )
samplesDef['data'].add_sample( tnpSamples.HNL2017['data_Run2017D'] )
samplesDef['data'].add_sample( tnpSamples.HNL2017['data_Run2017E'] )
samplesDef['data'].add_sample( tnpSamples.HNL2017['data_Run2017F'] ) #JH

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
samplesDef['data' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
if not samplesDef['tagSel'] is None:
    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph')
    samplesDef['tagSel'].set_cut('tag_Ele_pt > 37') #canceled non trig MVA cut

## set MC weight, simple way (use tree weight) 
#weightName = 'totWeight'
#if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

## set MC weight, can use several pileup rw for different data taking periods
weightName = 'weights_2017_runBCDEF.totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/data6/Users/jihkim/tnp_tamsa/POG_tree/2017//DY_madgraph_ele.pu.puTree.root')
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('/data6/Users/jihkim/tnp_tamsa/POG_tree/2017//DY_amcatnloext_ele.pu.puTree.root')
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('/data6/Users/jihkim/tnp_tamsa/POG_tree/2017//DY_madgraph_ele.pu.puTree.root') #JH


#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
   { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },
#   { 'var' : 'el_pt' , 'type': 'float', 'bins': [10,20,35,50,100,500] },
   { 'var' : 'el_pt' , 'type': 'float', 'bins': [10,20,35,50,100,200,500] },


]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0'

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
#LS: we removed the met cuts cause JEC not ready for UL2017
#additionalCuts = { 
#    0 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    1 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    2 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    3 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    4 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    5 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    6 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    7 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    8 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    9 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
#}
additionalCuts = { 
    #0 : 'tag_Ele_trigMVA > 0.92 ',
    #1 : 'tag_Ele_trigMVA > 0.92 ',
    #2 : 'tag_Ele_trigMVA > 0.92 ',
    #3 : 'tag_Ele_trigMVA > 0.92 ',
    #4 : 'tag_Ele_trigMVA > 0.92 ',
    #5 : 'tag_Ele_trigMVA > 0.92 ',
    #6 : 'tag_Ele_trigMVA > 0.92 ',
    #7 : 'tag_Ele_trigMVA > 0.92 ',
    #8 : 'tag_Ele_trigMVA > 0.92 ',
    #9 : 'tag_Ele_trigMVA > 0.92 '
    0 : 'tag_Ele_IsoMVA94XV2 > 0.92 ',
    1 : 'tag_Ele_IsoMVA94XV2 > 0.92 ',
    2 : 'tag_Ele_IsoMVA94XV2 > 0.92 ',
    3 : 'tag_Ele_IsoMVA94XV2 > 0.92 ',
    4 : 'tag_Ele_IsoMVA94XV2 > 0.92 ',
    5 : 'tag_Ele_IsoMVA94XV2 > 0.92 ',
    6 : 'tag_Ele_IsoMVA94XV2 > 0.92 ',
    7 : 'tag_Ele_IsoMVA94XV2 > 0.92 ',
    8 : 'tag_Ele_IsoMVA94XV2 > 0.92 ',
    9 : 'tag_Ele_IsoMVA94XV2 > 0.92 ' #JH : SKFlat variable
}

#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",
    ]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]

tnpParAltSigFit_addGaus = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,6.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "meanGF[80.0,70.0,100.0]","sigmaGF[15,5.0,125.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,85.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
         
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]
        
