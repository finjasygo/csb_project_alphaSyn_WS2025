import numpy as np
from Bio.PDB import PDBParser
from sklearn.cluster import KMeans
import os
import sys
import pandas as pd

folder = sys.argv[1]

output_folder = os.path.join(folder, 'results_sorted_chains')
os.makedirs(output_folder, exist_ok=True)


pdbs = []

for file in os.listdir(folder):
    if file.endswith('.pdb'):
        pdbs.append(os.path.join(folder, file))

parser = PDBParser(QUIET=True)

for pdb in pdbs:
    structure = parser.get_structure('structure', pdb)
    centroids = []
    chain_ids = []
    
    for model in structure:
        for chain in model:
            coords = []
            for res in chain:
                if 'CA' in res:
                    coords.append(res['CA'].get_coord())
            if len(coords) == 0:
                continue
            coords = np.array(coords)
            
            centroids.append(coords.mean(axis=0))
            chain_ids.append(chain.id)

    centroids = np.array(centroids)
    
    if len(centroids) < 2:
        print(f"Nicht genug Ketten in {pdb} für KMeans")
        continue

    # KMeans → find 2 protofilaments
    kmeans = KMeans(n_clusters=2, random_state=0).fit(centroids)
    labels = kmeans.labels_     # giving the labels of the cluster
    centers = kmeans.cluster_centers_

    # put chains into left/right according to centroid X position
    # Cluster with smaller mean-X is left-side since profilaments 
    # are lying next to eachother in the xy-layer
    x_positions = centers[:, 0]     # centers[:, 0] → alle X-Koordinaten
    left_cluster  = np.argmin(x_positions)
    right_cluster = np.argmax(x_positions)
    
    # assign chains
    left_chains = []
    right_chains = []
    
    for i in range(len(chain_ids)):
        if labels[i] == left_cluster:
            left_chains.append((chain_ids[i], centroids[i][2]))     # saving the chain and its z position as tupel
        if labels[i] == right_cluster:
            right_chains.append((chain_ids[i], centroids[i][2]))
        
    # sort by Z (bottom→top)
    # sorting left chains
    left_tmp = []
    left_chains_sorted = []

    for chain_id, z in left_chains:
        left_tmp.append((z, chain_id))

    left_tmp_sorted = sorted(left_tmp)

    for z, chain_id in left_tmp_sorted:
        left_chains_sorted.append(chain_id)

    # sorting right chains
    right_tmp = []
    right_chains_sorted = []

    for chain_id, z in right_chains:
        right_tmp.append((z, chain_id))

    right_tmp_sorted = sorted(right_tmp)

    for z, chain_id in right_tmp_sorted:
        right_chains_sorted.append(chain_id)

    pdb_name = os.path.basename(pdb)
    struct_name = os.path.splitext(pdb_name)[0]

    print('file', pdb_name, 'left', left_chains_sorted, 'right', right_chains_sorted)
    
    data = {'file': pdb_name, 
            'left': left_chains_sorted, 
            'right': right_chains_sorted}
    
    df = pd.DataFrame(data)
    


    filename = f'{struct_name}.csv'
    

    df.to_csv(os.path.join(output_folder, filename), index=False)

    print(df)
    print('dataframe was saved as', filename) 


    
