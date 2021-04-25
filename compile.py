import os
import pandas as pd

for file in os.listdir('results-100/'):
	energy = pd.read_csv('results-100/' + file)
	score = []
	best_energy = []
	binding_score = pd.read_csv('binding-score/' + file)
	binding_score['LigandName'] = binding_score['LigandName'].apply(lambda x : str(x).split('_')[-1])

	for row in energy.iterrows():
		best_energy.append(min(row[1]['E1'], row[1]['E2'], row[1]['E3']))
		s = binding_score[binding_score['LigandName'] == row[1]['ligand']].iloc[0]['BindingScore']
		score.append(s)
	energy['binding score'] = score
	energy['energy'] = best_energy
	del energy['E1'], energy['E2'], energy['E3']
	energy.to_csv('results-100/' + file, index=False)
