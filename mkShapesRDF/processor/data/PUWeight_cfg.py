####################### PU Weight CFG ##################################

PUCfg = {
    'Full2022EEv11': {
        'srcfile'     : "auto" ,
        'targetfiles' : { '1-1' : '/processor/data/PUweights/2022/2022_PU.root' } ,
        'srchist'     : "pileup"   ,
        'targethist'  : "pileup"   ,
        'name'        : "puWeight" ,
        'norm'        : True       ,
        'verbose'     : False      ,
        'nvtx_var'    : "Pileup_nTrueInt" ,
        'doSysVar'    : False ,
    } ,
}
