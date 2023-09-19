####################### PU Weight CFG ##################################

PUCfg = {
    'Full2022EEv11': {
        'srcfile'     : "auto" ,
        'targetfiles' : { '1-1' : '/processor/data/PUweights/2022/2022_PU.root' } ,
        'srchist'     : ["PV_npvsGood", "Rho_fixedGridRhoFastjetCentralCalo", "Rho_fixedGridRhoFastjetCentralChargedPileUp"],
        'targethist'  : ["PV_npvsGood", "Rho_fixedGridRhoFastjetCentralCalo", "Rho_fixedGridRhoFastjetCentralChargedPileUp"],
        'name'        : "puWeight" ,
        'norm'        : True       ,
        'verbose'     : False      ,
        'nvtx_var'    : ["PV_npvsGood", "Rho_fixedGridRhoFastjetCentralCalo", "Rho_fixedGridRhoFastjetCentralChargedPileUp"],
        'doSysVar'    : True ,
    } ,
}
