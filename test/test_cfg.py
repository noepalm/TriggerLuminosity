import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
#process.load('Configuration.Geometry.GeometryRecoDB_cff')
#process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = cms.string('124X_dataRun3_Prompt_v4')

process.source = cms.Source(
    "PoolSource",
    # fileNames = cms.untracked.vstring(
    #     #'root://cms-xrd-global.cern.ch//store/data/Run2022C/ParkingDoubleElectronLowMass0/MINIAOD/PromptReco-v1/000/356/170/00000/45c0f2ed-eb5b-4292-abc8-3117424d9432.root',
    #     #'root://cms-xrd-global.cern.ch//store/data/Run2022D/ParkingDoubleElectronLowMass0/MINIAOD/PromptReco-v1/000/357/538/00000/5fa3a99a-66e3-4925-a1da-95e669cc128b.root',
    #     # 'root://cms-xrd-global.cern.ch//store/data/Run2022D/ParkingDoubleElectronLowMass0/MINIAOD/PromptReco-v2/000/357/734/00000/3375647e-199a-4a8c-a041-5e8536d55077.root',
    #     'root://cms-xrd-global.cern.ch///store/data/Run2023D/ParkingDoubleElectronLowMass/MINIAOD/22Sep2023_v1-v1/70000/29f18a67-ef96-495d-b52e-b7c697bcb66b.root',
    #     'root://cms-xrd-global.cern.ch///store/data/Run2023D/ParkingDoubleElectronLowMass/MINIAOD/22Sep2023_v1-v1/70000/12bc1af1-cf6c-4c1b-8e5c-bb97566fea58.root',
    #     'root://cms-xrd-global.cern.ch///store/data/Run2023D/ParkingDoubleElectronLowMass/MINIAOD/22Sep2023_v1-v1/70000/36dcd43c-5894-49a2-b0da-a80128a8f1f0.root',
    #     'root://cms-xrd-global.cern.ch///store/data/Run2023D/ParkingDoubleElectronLowMass/MINIAOD/22Sep2023_v1-v1/70000/f5c766ee-24c6-4b3e-9ce3-289f487e3efc.root',
    #     'root://cms-xrd-global.cern.ch///store/data/Run2023D/ParkingDoubleElectronLowMass/MINIAOD/22Sep2023_v1-v1/70000/fd6dee27-3d89-4af8-991e-e00c6e0c7d6e.root',
    #     'root://cms-xrd-global.cern.ch///store/data/Run2023D/ParkingDoubleElectronLowMass/MINIAOD/22Sep2023_v1-v1/70000/ac02f5cd-bcf6-4f9c-9591-45abee14545d.root',
    #     'root://cms-xrd-global.cern.ch///store/data/Run2023D/ParkingDoubleElectronLowMass/MINIAOD/22Sep2023_v1-v1/70000/236c1578-f9de-4273-9612-50fcc6ef18bc.root',
    #     'root://cms-xrd-global.cern.ch///store/data/Run2023D/ParkingDoubleElectronLowMass/MINIAOD/22Sep2023_v1-v1/70000/6a676553-a0b5-417b-a82a-80a2b1fecb05.root',
    #     'root://cms-xrd-global.cern.ch///store/data/Run2023D/ParkingDoubleElectronLowMass/MINIAOD/22Sep2023_v1-v1/70000/7eb7dec5-38ae-4078-9309-ec0812faf2a1.root',
    #     'root://cms-xrd-global.cern.ch///store/data/Run2023D/ParkingDoubleElectronLowMass/MINIAOD/22Sep2023_v1-v1/70000/e0aaf252-70c8-4a2e-b999-fc3e04c66df6.root',
    # )
)

process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.source.skipEvents=cms.untracked.uint32(0)

process.load("PhysicsTools.TriggerLuminosity.JsonFilterAnalyzer_cff")
process.load("PhysicsTools.TriggerLuminosity.MiniAODTriggerAnalyzer_cff")
process.p = cms.Path(
    process.miniAODTriggerSequence+
    process.jsonFilterSequence
)
