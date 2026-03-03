#!/bin/bash

# provide path to the directory where the pdb-files are saved
folder="/Users/finjasygo/Documents/uni_MScBioinfo/sem3/project_csb/clustering_210126" 

cd "$folder" || exit

mkdir -p results_TMscore

list_pdb_files=(*.pdb)

for ((i=0; i<${#list_pdb_files[@]}; i++)); do
    file_1="${list_pdb_files[$i]}"
    filename_1="${file_1%.pdb}"
    for ((j=i+1; j<${#list_pdb_files[@]}; j++)); do
        file_2="${list_pdb_files[$j]}"
        filename_2="${file_2%.pdb}"
        TMscore "$file_1" "$file_2" > "results_TMscore/${filename_1}_vs_${filename_2}.txt"
    done
done