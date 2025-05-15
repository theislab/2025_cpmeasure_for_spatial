import spatialdata as sd
from pathlib import Path
import squidpy as sq

proj_dir = Path("/lustre/groups/ml01/projects/2025_ttreis_icml_cpmeasure")
data_dir = proj_dir / Path("data")
quarterbrain_path = data_dir / Path("quarterbrain_sdata.zarr")

sdata_quarterbrain = sd.read_zarr(quarterbrain_path)

sq.exp.calculate_image_features(
    sdata=sdata_quarterbrain,
    labels_key="segmentation",
    image_key="stitched_image",
    adata_key_added="morphology",
    n_jobs=20,
    show_progress_bar=True,
    scale="scale1"
)

sdata_quarterbrain.write(data_dir / "quarterbrain_sdata_measured.zarr", overwrite=True)