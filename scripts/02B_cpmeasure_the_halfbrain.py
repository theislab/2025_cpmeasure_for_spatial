import spatialdata as sd
from pathlib import Path
import squidpy as sq

proj_dir = Path("/lustre/groups/ml01/projects/2025_ttreis_icml_cpmeasure")
data_dir = proj_dir / Path("data")
halfbrain_path = data_dir / Path("halfbrain_sdata.zarr")

sdata_halfbrain = sd.read_zarr(halfbrain_path)

sq.exp.calculate_image_features(
    sdata=sdata_halfbrain,
    labels_key="segmentation",
    image_key="stitched_image",
    adata_key_added="morphology",
    n_jobs=32,
    show_progress_bar=True,
    scale="scale1"
)

sdata_halfbrain.write(data_dir / "halfbrain_sdata_measured.zarr", overwrite=True)
