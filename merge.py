import pandas as pd
import os
from tqdm import tqdm
import argparse

def merge(args):
	for filename in tqdm(os.listdir(args.binding_score_dir)):
		data = pd.read_csv(args.binding_score_dir + filename)
		energies = []
		target = data.iloc[0]['Target-Name']
		for row in data.iterrows():
			ligand = row[1]['Ligand-Name'].split('_')[-1]
			log_file = '{}{}_{}.txt'.format(args.log_dir, ligand, target)
			score = get_energy(log_file)
			energies.append(score)
		data['InterfE'] = energies
		data = data.dropna()
		if len(data) != 0:
			data.to_csv(args.binding_score_dir + filename, index=False)

def get_energy(filename):
	if not os.path.isfile(filename):
		return None
	with open(filename) as file:
		try:
			return float(file.readlines()[-10].split()[1])
		except:
			return None

parser = argparse.ArgumentParser(description='parser merge output file')
parser.add_argument('--binding_score_dir', dest='binding_score_dir', type=str, required=True)
parser.add_argument('--log_dir', dest='log_dir', type=str, required=True)

args = parser.parse_args()
merge(args)
