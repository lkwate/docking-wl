## Introduction
We present in this work the intersection of Deep Learning-based and empirical Molecular docking tools for the ligand-target interaction. The first part of the work relies on Deep Learning, in this case, we used [DeepPurpose](https://arxiv.org/abs/2004.08919) , the second part on Molecular docking tool [Autodock Vina](http://vina.scripps.edu/). The molecular docking involves two main internal steps : the extraction of the most promising binding sites from the protein structures, and the computation of the energy of the pose made of the ligand located in the most promising protein's binding sites. After computing the pose's energies with autodock vina, we optimzed them by setting the ligand in their corresponding binding sites using [chimera](https://www.cgl.ucsf.edu/chimera/)
## Requirements
* DeepPurpose : the instructions are described in this [repository](https://github.com/kexinhuang12345/DeepPurpose)
* Autodock Vina & Openbabel
```
sudo apt update
sudo apt install autodock-vina
sudo apt-get install -y openbabel
```
* CB-Dock : the instructions are described in [instructions](http://clab.labshare.cn/cb-dock/php/manual.php)
* chimera : the instructions are described in [instructions](https://www.cgl.ucsf.edu/chimera/download.html)

## Deep Learning Ligand-Target Affinity Computation
The ligand-target affinity computation consisted in the following steps:
* ligand & target conversion using openbabel
   * Ligand : From pdb to smiles
   * Target : From pdb to Amino Acid Sequence
* Binding-score computation : the Deepurpose pretrained models were used to figured out the affinity from the data (ligand & target) previously well converted. This [code](https://github.com/lkwate/docking-wl/blob/master/ML-binding-score-computation.ipynb) was used to carry out this operation.
## Molecular Docking
