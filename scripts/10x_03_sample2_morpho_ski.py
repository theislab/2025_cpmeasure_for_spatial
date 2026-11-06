import spatialdata as sd
from pathlib import Path
import squidpy as sq

proj_dir = Path("/lustre/groups/ml01/projects/2025_ttreis_icml_cpmeasure")
data_dir = proj_dir / Path("data")
sample2_path = data_dir / Path("xenium_sample2_subset_baked_cropped.zarr")

sdata_sample2 = sd.read_zarr(sample2_path)

morpho_ski = sq.exp.calculate_image_features(
    sdata=sdata_sample2,
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

morpho_ski.to_csv(data_dir / "xenium_sample2_subset_morpho_ski.csv")
