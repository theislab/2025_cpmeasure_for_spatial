import spatialdata as sd
from pathlib import Path
import squidpy as sq

proj_dir = Path("/lustre/groups/ml01/projects/2025_ttreis_icml_cpmeasure")
data_dir = proj_dir / Path("data")
sample1_path = data_dir / Path("xenium_sample1_hexes300.zarr")

sdata_sample1 = sd.read_zarr(sample1_path)

morpho_ski = sq.exp.calculate_image_features(
    sdata=sdata_sample1,
    labels_key="cell_labels_subset",
    image_key="hne_baked",
    adata_key_added="morphology",
    n_jobs=32,
    measurements=[
        "skimage:label",
        "skimage:label+image",
        # "cpmeasure:core",
        # "cpmeasure:correlation",
    ],
    show_progress_bar=True,
    scale="scale0",
    inplace=False,
)

morpho_ski.to_csv(data_dir / "xenium_sample1_hexes300_morpho_ski.csv")
