# CVID Multi-modal Single-Cell Analysis

## Study
7 CVID patients vs 9 healthy controls
7,000-10,000 purified B cells per donor

## Data layers
| Layer          | Platform      | Module          |
|----------------|---------------|-----------------|
| Gene expression| 5' scRNA-seq  | 01_transcriptomics |
| BCR repertoire | 5' scRNA+VDJ  | 02_BCR          |
| Enhancers/CTSS | REAPTEC       | 03_regulatory   |

## Analysis order
Must run in numbered order within each module.
Cross-module dependencies noted in each notebook header.

## Environment
conda env create -f environment.yml
conda activate cvid_scrna

## Key outputs
- data/processed/adata/adata_annotated.h5ad
- data/processed/enhancers/consensus_enhancers.csv
- data/processed/BCR/clonal_trees/
