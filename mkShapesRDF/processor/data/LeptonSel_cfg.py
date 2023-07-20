LepFilter_dict = {
    "Loose": "isLoose",
    "Veto": "isVeto",
    "WgStar": "isWgs",
    "isLoose": "FakeObjWP",
    "isVeto": "VetoObjWP",
    "isWgs": "WgStarObjWP",
}

ElectronWP = {
    "Full2018v9": {
        "VetoObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts
                    "True": ["False"],
                },
            },
        },
        # ------------
        "FakeObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_cutBased >= 3",
                        "Electron_convVeto == 1",
                    ],
                    # Barrel
                    "ROOT::VecOps::abs(Electron_eta)  <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                    ],
                    # EndCap
                    "ROOT::VecOps::abs(Electron_eta)  > 1.479": [
                        "Electron_sieie  < 0.03",
                        "ROOT::VecOps::abs(Electron_eInvMinusPInv) < 0.014",
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.2",
                    ],
                },
            },
        },
        "TightObjWP": {
            # ----- mvaFall17V2Iso
            "mvaFall17V2Iso_WP90": {
                "cuts": {
                    # Common cuts
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_mvaFall17V2Iso_WP90",
                        "Electron_convVeto",
                        "Electron_pfRelIso03_all < 0.06",
                    ],
                    # Barrel
                    "ROOT::VecOps::abs(Electron_eta) <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                    ],
                    # EndCap
                    "ROOT::VecOps::abs(Electron_eta) > 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz) <  0.2",
                    ],
                }
            }
        },
    },
    "Full2022EEv11": {
        "VetoObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts                                                                                                                                                                          
                    "True": ["False"],
                },
            },
        },
        # ------------                                                                                                                                                                                     
        "FakeObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts                                                                                                                                                                          
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_cutBased >= 3",
                        "Electron_convVeto == 1",
                    ],
                    # Barrel                                                                                                                                                                               
                    "ROOT::VecOps::abs(Electron_eta)  <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                    ],
                    # EndCap                                                                                                                                                                               
                    "ROOT::VecOps::abs(Electron_eta)  > 1.479": [
                        "Electron_sieie  < 0.03",
                        "ROOT::VecOps::abs(Electron_eInvMinusPInv) < 0.014",
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.2",
                    ],
                },
            },
        },
        "TightObjWP": {
            "cut_Tight_HWWW": {
                "cuts": {
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_cutBased >= 4",
                        "Electron_convVeto",
                        "Electron_pfRelIso03_all < 0.06",
                    ],
                    # Barrel
                    "ROOT::VecOps::abs(Electron_eta) <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                        "Electron_pfRelIso03_all < (0.0388+0.535/Electron_pt)",
                    ],
                    "ROOT::VecOps::abs(Electron_eta) > 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz) <  0.2",
                    ],
                },
                'tkSF':  {
                    '1-5' : 'data/jsonpog-integration/POG/EGM/2022EE/electron.json.gz'
                } ,
                'wpSF':  {
                    '1-4' : 'data/scale_factor/Full2017v9/egammaEffi_TightHWW_2017BCDE.txt' ,
                    '5-5' : 'data/scale_factor/Full2017v9/egammaEffi_TightHWW_2017F.txt' ,
                } ,
                'fakeW' : 'data/fake_prompt_rates/Full2017v9/mvaFall17V2Iso_WP90/',
            },
            "cut_Tight_HWWW_tthmva70": {
                "cuts": {
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_cutBased >= 4",
                        "Electron_convVeto",
                        "Electron_pfRelIso03_all < 0.06",
                        "Electron_mvaTTH > 0.7",
                    ],
                    # Barrel                                                                                                                                                                               
                    "ROOT::VecOps::abs(Electron_eta) <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                        "Electron_pfRelIso03_all < (0.0388+0.535/Electron_pt)",
                    ],
                    "ROOT::VecOps::abs(Electron_eta) > 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz) <  0.2",
                    ],
                },
                'tkSF':  {
                    '1-5' : 'data/jsonpog-integration/POG/EGM/2022EE/electron.json.gz'
                } ,
                'wpSF':  {
                    '1-4' : 'data/scale_factor/Full2017v9/egammaEffi_TightHWW_2017BCDE.txt' ,
                    '5-5' : 'data/scale_factor/Full2017v9/egammaEffi_TightHWW_2017F.txt' ,
                } ,
                'fakeW' : 'data/fake_prompt_rates/Full2017v9/mvaFall17V2Iso_WP90/',
            },
            "cut_Medium_HWWW": {
                "cuts": {
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_cutBased >= 3",
                        "Electron_convVeto",
                        "Electron_pfRelIso03_all < 0.06",
                    ],
                    # Barrel                                                                                                                                                                               
                    "ROOT::VecOps::abs(Electron_eta) <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                        "Electron_pfRelIso03_all < (0.0388+0.535/Electron_pt)",
                    ],
                    "ROOT::VecOps::abs(Electron_eta) > 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz) <  0.2",
                    ],
                },
                'tkSF':  {
                    '1-5' : 'data/jsonpog-integration/POG/EGM/2022EE/electron.json.gz'
                } ,
                'wpSF':  {
                    '1-4' : 'data/scale_factor/Full2017v9/egammaEffi_TightHWW_2017BCDE.txt' ,
                    '5-5' : 'data/scale_factor/Full2017v9/egammaEffi_TightHWW_2017F.txt' ,
                } ,
                'fakeW' : 'data/fake_prompt_rates/Full2017v9/mvaFall17V2Iso_WP90/',
            },
            # ----- MVA                                                                                                                                                                         
            "mvaWinter22V2Iso_WP90": {
                "cuts": {
                    # Common cuts                                                                                                                                                                          
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_mvaIso_WP90",
                        "Electron_convVeto",
                        "Electron_pfRelIso03_all < 0.06",
                    ],
                    # Barrel                                                                                                                                                                               
                    "ROOT::VecOps::abs(Electron_eta) <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                    ],
                    # EndCap                                                                                                                                                                               
                    "ROOT::VecOps::abs(Electron_eta) > 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz) <  0.2",
                    ],
                },
                'tkSF':  {
                    '1-5' : 'data/jsonpog-integration/POG/EGM/2022EE/electron.json.gz'
                } ,
                'wpSF':  {
                    '1-4' : 'data/scale_factor/Full2017v9/egammaEffi_TightHWW_2017BCDE.txt' ,
                    '5-5' : 'data/scale_factor/Full2017v9/egammaEffi_TightHWW_2017F.txt' ,
                } ,
                'fakeW' : 'data/fake_prompt_rates/Full2017v9/mvaFall17V2Iso_WP90/',
            },
            "mvaWinter22V2Iso_WP90_tthmva70": {
                "cuts": {
                    # Common cuts                                                                                                                                                                          
                    "ROOT::RVecB (Electron_pt.size(), true)": [
                        "ROOT::VecOps::abs(Electron_eta) < 2.5",
                        "Electron_mvaIso_WP90",
                        "Electron_convVeto",
                        "Electron_pfRelIso03_all < 0.06",
                        "Electron_mvaTTH > 0.7",
                    ],
                    # Barrel                                                                                                                                                                               
                    "ROOT::VecOps::abs(Electron_eta) <= 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.05",
                        "ROOT::VecOps::abs(Electron_dz)  < 0.1",
                    ],
                    # EndCap                                                                                                                                                                               
                    "ROOT::VecOps::abs(Electron_eta) > 1.479": [
                        "ROOT::VecOps::abs(Electron_dxy) < 0.1",
                        "ROOT::VecOps::abs(Electron_dz) <  0.2",
                    ],
                },
                'tkSF':  {
                    '1-5' : 'data/jsonpog-integration/POG/EGM/2022EE/electron.json.gz'
                } ,
                'wpSF':  {
                    '1-4' : 'data/scale_factor/Full2017v9/egammaEffi_TightHWW_2017BCDE.txt' ,
                    '5-5' : 'data/scale_factor/Full2017v9/egammaEffi_TightHWW_2017F.txt' ,
                } ,
                'fakeW' : 'data/fake_prompt_rates/Full2017v9/mvaFall17V2Iso_WP90/',
            },
        },
    },

}

MuonWP = {
    # ____________________Full2018v9__________________________
    "Full2018v9": {
        # ------------
        "VetoObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_pt > 10.0",
                    ]
                },
            }
        },
        # ------------
        "FakeObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfRelIso04_all < 0.4",
                    ],
                    # dxy for pT < 20 GeV
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    # dxy for pT > 20 GeV
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
            },
        },
        # ------------
        "TightObjWP": {
            "cut_Tight_HWWW": {
                "cuts": {
                    # Common cuts
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfRelIso04_all < 0.15",
                    ],
                    # dxy for pT < 20 GeV
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    # dxy for pT > 20 GeV
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                "idSF": {
                    "1-1": [
                        "data/scale_factor/Full2018v9/NUM_TightHWW_DEN_TrackerMuons_eta_pt.root"
                    ],
                },
                "isoSF": {
                    "1-1": [
                        "data/scale_factor/Full2018v9/NUM_TightHWW_ISO_DEN_TightHWW_eta_pt.root"
                    ],
                },
                "fakeW": "data/fake_prompt_rates/Full2018v9/cut_Tight_HWWW/",
            },
            "cut_Tight_HWWW_tthmva_80": {
                "cuts": {
                    # Common cuts
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfRelIso04_all < 0.15",
                        "Muon_mvaTTH > 0.8",
                    ],
                    # dxy for pT < 20 GeV
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    # dxy for pT > 20 GeV
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                # Update with new SFs
                "idSF": {
                    "1-1": [
                        "LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_TightHWW_DEN_TrackerMuons_eta_pt.root"
                    ],
                },
                "isoSF": {
                    "1-1": [
                        "LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_TightHWW_ISO_DEN_TightHWW_eta_pt.root"
                    ],
                },
                "tthMvaSF": {
                    "1-1": [
                        "NUM_TightHWW_tth_ISO_DEN_TightHWW_ISO_eta_pt",  # Hist name
                        "LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_TightHWW_tth_ISO_DEN_TightHWW_ISO_eta_pt.root",
                    ]  # Nominal+Stat+Syst
                    # 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v7/ttHMVA0p8_TightHWWCut_SFs_SYS_2018.root', ] # Syst
                },
                "fakeW": "/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v9/cut_Tight_HWWW_tthmva_80/",
            },
        },
    },
    ### ------------------- Full2022EE --------------------
    "Full2022EEv11": {
        # ------------                                                                                                                                                                                     
        "VetoObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts                                                                                                                                                                          
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_pt > 10.0",
                    ]
                },
            }
        },
        # ------------                                                                                                                                                                                     
        "FakeObjWP": {
            "HLTsafe": {
                "cuts": {
                    # Common cuts                                                                                                                                                                          
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfRelIso04_all < 0.4",
                    ],
                    # dxy for pT < 20 GeV                                                                                                                                                                  
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    # dxy for pT > 20 GeV                                                                                                                                                                  
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
            },
        },
        # ------------                                                                                                                                                                         
        "TightObjWP": {
            "cut_Tight_HWWW": {
                "cuts": {
                    # Common cuts                                                                                                                                                                          
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfRelIso04_all < 0.15",
                    ],
                    # dxy for pT < 20 GeV                                                                                                                                                                  
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    # dxy for pT > 20 GeV                                                                                                                                                                  
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                "idSF": {
                    "1-1": [
                        "LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_TightHWW_DEN_TrackerMuons_eta_pt.root"
                    ],
                },
                "isoSF": {
                    "1-1": [
                        "LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_TightHWW_ISO_DEN_TightHWW_eta_pt.root"
                    ],
                },
                "fakeW": "/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v9/cut_Tight_HWWW/",
            },
            "cut_Medium_HWWW": {
                "cuts": {
                    # Common cuts                                                                                                                                                                          
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_mediumId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfRelIso04_all < 0.15",
                    ],
                    # dxy for pT < 20 GeV                                                                                                                                                                  
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    # dxy for pT > 20 GeV                                                                                                                                                                  
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                "idSF": {
                    "1-1": [
                        "LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_MediumHWW_DEN_TrackerMuons_eta_pt.root"
                    ],
                },
                "isoSF": {
                    "1-1": [
                        "LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_MediumHWW_ISO_DEN_MediumHWW_eta_pt.root"
                    ],
                },
                "fakeW": "/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v9/cut_Medium_HWWW/",
            },
            "cut_Tight_HWWW_tthmva_80": {
                "cuts": {
                    # Common cuts                                                                                                                                                                          
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_tightId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfRelIso04_all < 0.15",
                        "Muon_mvaTTH > 0.8",
                    ],
                    # dxy for pT < 20 GeV                                                                                                                                                                  
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    # dxy for pT > 20 GeV                                                                                                                                                                  
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                # Update with new SFs                                                                                                                                                                      
                "idSF": {
                    "1-1": [
                        "LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_TightHWW_DEN_TrackerMuons_eta_pt.root"
                    ],
                },
                "isoSF": {
                    "1-1": [
                        "LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_TightHWW_ISO_DEN_TightHWW_eta_pt.root"
                    ],
                },
                "tthMvaSF": {
                    "1-1": [
                        "NUM_TightHWW_tth_ISO_DEN_TightHWW_ISO_eta_pt",  # Hist name                                                                                                                       
                        "LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_TightHWW_tth_ISO_DEN_TightHWW_ISO_eta_pt.root",
                    ]  # Nominal+Stat+Syst  
                },
                "fakeW": "/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v9/cut_Tight_HWWW_tthmva_80/",
            },
            "cut_Medium_HWWW_tthmva_80": {
                "cuts": {
                    # Common cuts                                                                                                                                                                          
                    "ROOT::RVecB (Muon_pt.size(), true)": [
                        "ROOT::VecOps::abs(Muon_eta) < 2.4",
                        "Muon_mediumId",
                        "ROOT::VecOps::abs(Muon_dz) < 0.1",
                        "Muon_pfRelIso04_all < 0.15",
                        "Muon_mvaTTH > 0.8",
                    ],
                    # dxy for pT < 20 GeV                                                                                                                                                                  
                    "Muon_pt <= 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.01",
                    ],
                    # dxy for pT > 20 GeV                                                                                                                                                                  
                    "Muon_pt > 20.0": [
                        "ROOT::VecOps::abs(Muon_dxy) < 0.02",
                    ],
                },
                # Update with new SFs                                                                                                                                                                      
                "idSF": {
                    "1-1": [
                        "LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_TightHWW_DEN_TrackerMuons_eta_pt.root"
                    ],
                },
                "isoSF": {
                    "1-1": [
                        "LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v9/NUM_TightHWW_ISO_DEN_TightHWW_eta_pt.root"
                    ],
                },
                "tthMvaSF": {
                    "1-1": [
                        "NUM_TightHWW_tth_ISO_DEN_TightHWW_ISO_eta_pt",  # Hist name                                                                                                                       
                        "LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2022v11/NUM_MediumHWW_tth_ISO_DEN_TightHWW_ISO_eta_pt.root",
                    ]  # Nominal+Stat+Syst                                                                                                                                                                 
                },
                "fakeW": "/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2022v11/cut_Medium_HWWW_tthmva_80/",
            },
        },
    }
}
