**Accepted Poster at the MLPC Workshop of ICLR 2021 : [poster](https://mlpcp21.github.io/files/posters/ICLR%202021%20Poster_%20Computationally%20Accelerating%20Protein%20Ligand%20Matching_%20A%20Case%20Study%20on%20Leishmaniasis%20(MLPCP).pdf)**


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
* Autodock : [instructions](http://mgltools.scripps.edu/)

## Deep Learning Ligand-Target Affinity Computation
The ligand-target affinity computation consisted in the following steps:
* ligand & target conversion using openbabel
   * Ligand : From pdb to smiles
   * Target : From pdb to Amino Acid Sequence
* Binding-score computation : the Deepurpose pretrained models were used to figured out the affinity from the data (ligand & target) previously well converted. This [code](https://github.com/lkwate/docking-wl/blob/master/ML-binding-score-computation.ipynb) was used to carry out this operation.
## Molecular Docking
In this part, we performed the following operations to realize the protein-ligand docking.
* Ligand-Target preparation: Autodock vina required ligands and target both converted into pdbqt format. To realize it, we used the Vina's built-in scripts to prepare both ligands and proteins.
  * [ligand preparation](http://autodock.scripps.edu/faqs-help/how-to/how-to-prepare-a-ligand-file-for-autodock4)
  * [receptor preparation](http://autodock.scripps.edu/faqs-help/how-to/how-to-prepare-a-receptor-file-for-autodock4)
* Once the ligand and receptor preparation completed, we moved first, on searching the binding pockets of the receptor then on computing the energy of the ligand-receptor pairs with ligand located in each of the most promising binding sites. This was done using [CB-Dock](http://clab.labshare.cn/cb-dock/php/manual.php) built on Autodock vina. The main added feature of CB-Dock is the computation of the receptor binding pocket, the remain work related to the docking entirely relies on Autodock (vina).
* In the last step, we built the optimized pose (ligand-receptor) using [chimera](https://www.cgl.ucsf.edu/chimera/download.html) which readily output the optimized pose into pdb format for submission at the [indaba-grand-challenge-curing-leishmaniasis](https://zindi.africa/competitions/indaba-grand-challenge-curing-leishmaniasis)
