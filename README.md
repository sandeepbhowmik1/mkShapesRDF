# Simple Parallel RDF version of Latinos mkShapes

1. Run the setup command:
```
. ./setup.sh
```

2. Configure the configuration folder (e.g. 2016Renorm) with the main files:
- aliases.py
- configuration.py
- cuts.py
- nuisances.py
- plot.py
- samples.py
- variables.py

3. Run the analysis:
```
python mkShapesRDFParallel.py -o 0 -f 2016Renorm -b 1
```
`-o` indicates the operationMode:
- 0 run analysis
- 1 check batch output and errs
- 2 merge root files
- 3 plot them

For the provided example (2016Renorm) it's estimated an execution time of ~ 10 mins running on lxbatch (condor on lxplus) @ CERN.


It's highly recommended to limit input ROOT files at the first run to check for errors. The following command will only take 1 file for each sample type:
```
python mkShapesRDFParallel.py -o 0 -f 2016Renorm -l 1
```

4. After all the jobs finished (or most of them did) you can run `mkShapesRDFParallel.py -o 1 -f 2016Renorm` to know which jobs failed and why

5. If all the jobs succeeded run the merger with the option: 
```
python mkShapesRDFParallel.py -o 2 -f 2016Renorm
```

6. Plot with 
```
python mkShapesRDFParallel.py -o 3 -f 2016Renorm
```
which will create the plots to the specified paths provided in `configuration.py` 

