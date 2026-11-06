import spatialdata as sd
from pathlib import Path
import squidpy as sq

proj_dir = Path("/lustre/groups/ml01/projects/2025_ttreis_icml_cpmeasure")
data_dir = proj_dir / Path("data")
sample2_path = data_dir / Path("xenium_sample2_hexes300.zarr")

sdata_sample2 = sd.read_zarr(sample2_path)

sq.exp.calculate_image_features(
    sdata=sdata_sample2,
    labels_key="filtered_hexes",
    image_key="hne_baked",
    adata_key_added="morphology",
    n_jobs=32,
    measurements=[
        "skimage:label",
        "skimage:label+image",
        "cpmeasure:core",
        "cpmeasure:correlation",
    ],
    show_progress_bar=True,
    scale="scale0",
    inplace=True,
)

sdata_sample2.write(data_dir / "xenium_sample2_hexes300_measured.zarr", overwrite=True)
