#!/usr/bin/env python                                                                                                                                                                                                                                                         

import sys
import optparse
import copy
import collections
import os.path
import math
import logging
import tempfile
import subprocess
import fileinput
import argparse
from sys import argv
from mkShapesRDF.processor.framework.Sites_cfg import Sites

def defaultParser():

    parser = argparse.ArgumentParser(add_help=False)
    
    parser.add_argument(
        "-p",
        "--prod",
        type=str,
        help="Production name to run",
        required=True,
    )

    parser.add_argument(
        "-s",
        "--step",
        type=str,
        help="Step name to run",
        required=True,
    )

    parser.add_argument(
        "-i",
        "--inputFolder",
        type=str,
        help="Input folder to search for files",
        required=False,
        default="",
    )

    parser.add_argument(
        "-Sub",
        "--Submit",
        action='store_true',
        help="Submit files",
        default=False,
    )
    
    return parser

def run(production, step, initialStep="", submit=False):


    if initialStep!="":
        initialStep = initialStep + "__"

    prePath = os.path.abspath(os.path.dirname(__file__))

    path = prePath + "/condor/" + production + "/" + step + "/"
    output_path = Sites["eosDir"] + production + "/" + initialStep + step
    jobDir = path

    cmd = "find {} -type d -name '*'".format(path)
    
    fnames = subprocess.check_output(cmd, shell=True).strip().split(b'\n')
    fnames = [fname.decode('ascii').split(step+"/")[1] for fname in fnames] 

    
    failed_jobs = []
    error_files = []
    script_files = []
    
    for fname in fnames:
        
        file_name = output_path + "/nanoLatino_" + fname + ".root"
        error_file = jobDir + fname + "/" + "err.txt"
        script_file = jobDir + fname + "/" + "script.py"

        if os.path.exists(file_name) or fname=="":
            continue
        else:
            print("ERROR: File does not exist in output folder")
            print("LABEL: " + fname)
            failed_jobs.append(fname)
            error_files.append(error_file)
            script_files.append(script_file)

    print("=========================")
    print("Ratio of failed jobs: " + str(len(failed_jobs)) + "/" + str(len(fnames)) + " = " + str(round(100*len(failed_jobs)/len(fnames), 2)) + "%")
    
    
    doCheckDAS = False
    
    if doCheckDAS:    
        for i in range(len(failed_jobs)):
            
            isCopyError = False
            if not os.path.exists(error_files[i]):
                continue

            with fileinput.FileInput(error_files[i], inplace=False) as errf:
                for line in errf:
                    if "Error copying file" in line:
                        isCopyError = True
        
            if isCopyError:
                print(script_files[i])
                with fileinput.FileInput(script_files[i], inplace=True, backup='.bak') as f:
                    for line in f:
                        if "cms-xrd-global.cern.ch" in line:
                            print(line.replace("cms-xrd-global.cern.ch", "xrootd-cms.infn.it"), end='\n')
                        else:
                            print(line, end='')
            


    if submit:
        resubmit = """
universe = vanilla
executable = run.sh
arguments = $(Folder)

should_transfer_files = YES
transfer_input_files = $(Folder)/script.py
max_transfer_input_mb = 4000
max_transfer_output_mb = 4000

output = $(Folder)/out.txt
error  = $(Folder)/err.txt
log    = $(Folder)/log.txt

request_cpus   = 1
request_memory = 4500
request_disk = 10000000
+JobFlavour = "workday"

queue 1 Folder in RPLME_ALLSAMPLES"""
        
        resubmit = resubmit.replace("RPLME_ALLSAMPLES", " ".join(failed_jobs[0:300]))
        
        with open(jobDir + "submit_failed.jdl", "w") as f:
            f.write(resubmit)
            
            
        proc = subprocess.Popen(
            f"cd {jobDir}; condor_submit submit_failed.jdl;", shell=True
        )
        
        proc.wait()


if __name__ == "__main__":
    parser = defaultParser()
    args = parser.parse_args()
    
    prodName = args.prod
    step = args.step
    initialStep = args.inputFolder
    doSubmit = args.Submit

    run(prodName, step, initialStep, doSubmit)
