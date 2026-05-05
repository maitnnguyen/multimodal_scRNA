"""
Shared I/O functions used across all notebooks.
Import with: from utils.io import load_adata, save_adata
"""

import scanpy as sc
import pandas as pd
import yaml
import os

def load_config(config_path='config/parameters.yml'):
    with open(config_path) as f:
        return yaml.safe_load(f)

def load_samples(samples_path='config/samples.tsv'):
    return pd.read_csv(samples_path, sep='\t')

def load_adata(stage: str) -> sc.AnnData:
    """
    Load adata at specific processing stage.
    stage: 'raw' | 'qc' | 'annotated' | 'integrated'
    """
    paths = {
        'raw':        'data/processed/adata/adata_raw.h5ad',
        'qc':         'data/processed/adata/adata_qc.h5ad',
        'annotated':  'data/processed/adata/adata_annotated.h5ad',
        'integrated': 'data/processed/adata/adata_integrated.h5ad',
    }
    assert stage in paths, f"Unknown stage: {stage}"
    path = paths[stage]
    assert os.path.exists(path), f"File not found: {path}"
    print(f"Loading {stage} adata from {path}")
    return sc.read_h5ad(path)

def save_adata(adata: sc.AnnData, stage: str):
    """Save adata at processing stage."""
    paths = {
        'raw':        'data/processed/adata/adata_raw.h5ad',
        'qc':         'data/processed/adata/adata_qc.h5ad',
        'annotated':  'data/processed/adata/adata_annotated.h5ad',
        'integrated': 'data/processed/adata/adata_integrated.h5ad',
    }
    path = paths[stage]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    adata.write_h5ad(path)
    print(f"✓ Saved {stage} adata → {path}")
