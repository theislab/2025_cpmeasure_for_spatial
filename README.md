# cp_measure for spatial transcriptomics

Analysis code for the spatial use case in the `cp_measure` workshop paper (CODEML workshop, ICML 2025). We measured morphology features with [`cp_measure`](https://github.com/afermg/cp_measure) on the H&E images of two 10x Xenium breast cancer sections, and we compared how well cell types can be predicted from H&E morphology, from RNA, and from both.

Preprint: [arXiv:2507.01163](https://arxiv.org/abs/2507.01163)

```
@article{munoz2025cpmeasure,
  title={cp\_measure: API-first feature extraction for image-based profiling workflows},
  author={Mu{\~n}oz, Al{\'a}n F and Treis, Tim and Kalinin, Alexandr A and Dasgupta, Shatavisha and Theis, Fabian and Carpenter, Anne E and Singh, Shantanu},
  journal={arXiv preprint arXiv:2507.01163},
  year={2025}
}
```

## Data

- Xenium sections: the 10x datasets "FFPE Human Breast with Custom Add-on Panel", sample 1 = "Xenium V1 FFPE Human Breast IDC With Addon" and sample 2 = "ILC With Addon" (breast cancer). In [SpatialData-DB](https://lamin.ai/scverse/spatialdata-db) they are the datasets `10ajs` (IDC, Lamin artifact `B3zp6W2YeX4byunn`) and `10ajt` (ILC, Lamin artifact `k6XDMZ5acbyhjDn4`). Notebook 01 loads older uploads of the same data (`1lNcghy5uvSIIj1X`, `Uj7J4jjgzHw0lcm8`). Those uploads were later removed from SpatialData-DB as duplicates with identical count matrices, so use the datasets above to rerun.
- H&E images: the H&E images and alignment matrices that 10x published with the same two datasets. Notebook 01 registers each H&E image to the Xenium coordinates with the 10x alignment matrix and resamples it onto the Xenium pixel grid (`hne_baked`), so the Xenium cell masks can be used to measure the H&E image.

Data files are not in this repository (`data/` is ignored), except for three small result tables.

## Order of the analysis

The notebooks in `notebooks/10x_xenium/` run in order:

1. `01`: load the Xenium data and add the registered H&E images.
2. `02A` to `02D`: annotate cell types from RNA (decoupler, HLCA with scArches, manual).
3. `03`: subsample cells for feature extraction.
4. `scripts/10x_03_*`: run `cp_measure` and scikit-image feature extraction on the H&E images (run as jobs on a cluster).
5. `05` and `06`: collect the features and preprocess both modalities.
6. `07`: predict cell types with XGBoost from RNA only, H&E morphology only, and both.
7. `08` to `10`: repeat the measurement and evaluation on hexagonal tiles 300 and 500 pixels wide (about 64 and 106 µm) instead of single cells.

## Known issues

- Paths are absolute paths on the Helmholtz Munich cluster. Change `proj_dir` (scripts) and the data paths (notebooks) to run the code elsewhere.
- The `10x_03_sample2_*` scripts point at the sample 1 hexagon files. They are kept as they were run.
- The CosMx analysis in `notebooks/nanostring_cosmx/` did not work and is not part of the paper.

## License

MIT, see `LICENSE`.
