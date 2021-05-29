import argparse
import os
import pandas as pd

log_file_pattern = '{}{}_{}.txt'
output_file_pattern = '{}{}_{}.txt'
docking_command = 'vina --receptor {} --ligand {} --center_x {} --center_y {} --center_z {} --size_x {} --size_y {} --size_z {} --log {} --out {} --energy_range 100'

def docking(args):
	
	## iterate over the files contain the binding score (protein, ligand, binding_score)
	for binding_score_file in os.listdir(args.binding_score):
		binding_score_data = pd.read_csv(os.path.join(args.binding_score, binding_score_file))
		
		# get target name
		target_name = binding_score_data.iloc[0]['Target-Name']
		target_name_pdbqt = '{}{}.pdbqt'.format(args.protein, target_name)
		
		## check if the protein.pdbqt exists
		if not os.path.isfile(target_name_pdbqt):
			continue
		
		## check is the config.txt file exists
		target_config_txt = '{}{}.txt'.format(args.config, target_name)
		if not os.path.isfile(target_config_txt):
			continue
			
		## get configurations from config file
		cx, cy, cz, sx, sy, sz = tuple([None]*6)
		with open(target_config_txt) as file:
			lines = file.readlines()
			cx, cy, cz = tuple(lines[-1].split()[1:])
			sx, sy, sz = tuple(lines[-2].split()[1:])
			
		## iterate over (ligand, target, binding_score) triples
		for row in binding_score_data.iterrows():
			ligand_name = row[1]['Ligand-Name'].split('_')[-1]
			ligand_name_pdbqt = '{}{}.pdbqt'.format(args.ligand, ligand_name)
			if not os.path.isfile(ligand_name_pdbqt):
				continue
		
			# log path
			log_file = log_file_pattern.format(args.log, ligand_name, target_name)
			output_file = output_file_pattern.format(args.output, ligand_name, target_name)
			
			## check if the output file already exists
			if os.path.isfile(output_file):
				continue
			
			# run the docking with autodock vina
			os.system(docking_command.format(target_name_pdbqt, ligand_name_pdbqt, cx, cy, cz, sx, sy, sz, log_file, output_file))
		

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='files location')
	parser.add_argument('--output', dest='output', type=str, required=True)
	parser.add_argument('--binding_score', dest='binding_score', type=str, required=True)
	parser.add_argument('--config', dest='config', type=str, required=True)
	parser.add_argument('--log', dest='log', type=str, required=True)
	parser.add_argument('--ligand', dest='ligand', type=str, required=True)
	parser.add_argument('--protein', dest='protein', type=str, required=True)
	
	args = parser.parse_args()
	docking(args)
