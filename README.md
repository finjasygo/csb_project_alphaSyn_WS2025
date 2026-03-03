# csb_project_alphaSyn_WS2025
A CoSyBio project focused on analyzing structural variations and intermediate conformations of α-synuclein involved in Parkinson’s disease.

### TM version
We used TM-align to compare alpha-synuclein structures. The scripts used for this purpose, version 20190822, are listed under [TMtools20190822](./TMtools20190822).  
If you use this software or scripts, please cite:

Zhang, Y., & Skolnick, J. (2005). TM-align: A protein structure alignment algorithm based on TM-score. *Nucleic Acids Research*, 33(7), 2302–2309. [DOI: 10.1093/nar/gki524](https://doi.org/10.1093/nar/gki524)

### Execution
In addition, a bash script was developed for execution. This requires a folder containing the pdb files to be compared. The bash script creates a `results_TMscore` folder, which contains the results of the respective structure comparisons as txt files.  
The TMscore.cpp script is used for this, which can be executed after `sudo cp TMscore /usr/local/bin/`  with the command `TMscore`.

Afterward the bash script can be executed using:
```bash
bash tm_score.sh
