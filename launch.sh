#!/bin/bash
sudo apt-get update -y
sudo apt-get install -y autodock-vina
python3 docking.py --output 'outputs/' --binding_score 'binding_scores/' --config 'configs/' --log 'logs/' --ligand 'ligand-pdbqt/' --protein 'protein-pdbqt/'
