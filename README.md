# csb_project_alphaSyn_WS2025
A CoSyBio project focused on analyzing structural variations and intermediate conformations of α-synuclein involved in Parkinson’s disease.

## Repository Overview

This repository contains scripts and data for the structural analysis of α-synuclein, including intermediate structures, chain comparisons, and TM-score analysis.  

**Main directories and files:**

| Directory / File | Description |
|-----------------|-------------|
| `TMtools20190822` | Scripts for TM-Score structure comparison (version 20190822). |
| `alphasyn_intermediate_structures_pdb` | α-synuclein intermediate PDB structures and results used in analyses. |
| `asyn_1-99_Q_DA_paper_vs_ML_paper` | Comparison files for α-synuclein residues 1–99. |
| `asyn_36-93_Q_DA_paper_vs_ML_paper` | TM-score results for α-synuclein residues 36–93. |
| `comparison_of_chains` | Files for comparing individual chains. |
| `sorting_chains.py` | Python script for sorting protein chains. |
| `tm_score.sh` | Bash script to calculate TM-score between PDB files. |


### TM-Score
We used TM-Score to compare alpha-synuclein structures. The scripts used for this purpose, version 20190822, are listed under [TMtools20190822](./TMtools20190822).  

**Citation:**  
Zhang, Y., & Skolnick, J. (2005). *TM-align: A protein structure alignment algorithm based on TM-score*. Nucleic Acids Research, 33(7), 2302–2309. [DOI](https://doi.org/10.1093/nar/gki524)


### Execution
In addition, a bash script was developed for execution. This requires a folder containing the pdb files to be compared. The bash script creates a `results_TMscore` folder, which contains the results of the respective structure comparisons as txt files.  
The TMscore.cpp script is used for this, which can be executed after `sudo cp TMscore /usr/local/bin/`  with the command `TMscore`.

Afterward the bash script can be executed using:
```bash
bash tm_score.sh
