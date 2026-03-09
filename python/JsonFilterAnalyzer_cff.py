import FWCore.ParameterSet.Config as cms

files = [
    "/eos/home-n/npalmeri/DiEleAnalyzer/trigger_prescale_lumi/CMSSW_13_3_0_new/src/PhysicsTools/TriggerLuminosity/test/jsons/L1_10p5_HLT_5p0_final.json",
    "/eos/home-n/npalmeri/DiEleAnalyzer/trigger_prescale_lumi/CMSSW_13_3_0_new/src/PhysicsTools/TriggerLuminosity/test/jsons/L1_10p5_HLT_6p5_final.json",
    "/eos/home-n/npalmeri/DiEleAnalyzer/trigger_prescale_lumi/CMSSW_13_3_0_new/src/PhysicsTools/TriggerLuminosity/test/jsons/L1_11p0_HLT_6p5_final.json",
    "/eos/home-n/npalmeri/DiEleAnalyzer/trigger_prescale_lumi/CMSSW_13_3_0_new/src/PhysicsTools/TriggerLuminosity/test/jsons/L1_5p5_HLT_4p0_final.json",
    "/eos/home-n/npalmeri/DiEleAnalyzer/trigger_prescale_lumi/CMSSW_13_3_0_new/src/PhysicsTools/TriggerLuminosity/test/jsons/L1_5p5_HLT_6p0_final.json",
    "/eos/home-n/npalmeri/DiEleAnalyzer/trigger_prescale_lumi/CMSSW_13_3_0_new/src/PhysicsTools/TriggerLuminosity/test/jsons/L1_6p0_HLT_4p0_final.json",
    "/eos/home-n/npalmeri/DiEleAnalyzer/trigger_prescale_lumi/CMSSW_13_3_0_new/src/PhysicsTools/TriggerLuminosity/test/jsons/L1_6p5_HLT_4p5_final.json",
    "/eos/home-n/npalmeri/DiEleAnalyzer/trigger_prescale_lumi/CMSSW_13_3_0_new/src/PhysicsTools/TriggerLuminosity/test/jsons/L1_7p0_HLT_5p0_final.json",
    "/eos/home-n/npalmeri/DiEleAnalyzer/trigger_prescale_lumi/CMSSW_13_3_0_new/src/PhysicsTools/TriggerLuminosity/test/jsons/L1_8p0_HLT_5p0_final.json",
    "/eos/home-n/npalmeri/DiEleAnalyzer/trigger_prescale_lumi/CMSSW_13_3_0_new/src/PhysicsTools/TriggerLuminosity/test/jsons/L1_8p5_HLT_5p0_final.json",
    "/eos/home-n/npalmeri/DiEleAnalyzer/trigger_prescale_lumi/CMSSW_13_3_0_new/src/PhysicsTools/TriggerLuminosity/test/jsons/TOTAL.json",
]

JsonFilterAnalyzer = cms.EDAnalyzer(
    "JsonFilterAnalyzer",
    Verbose = cms.int32(0),
    JsonFiles = cms.vstring(files),
)

jsonFilterSequence = cms.Sequence(
    JsonFilterAnalyzer
)
