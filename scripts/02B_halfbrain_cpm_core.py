import spatialdata as sd
from pathlib import Path
import squidpy as sq

# silence warning
import dask
dask.config.set({"dataframe.query-planning": True})

proj_dir = Path("/lustre/groups/ml01/projects/2025_ttreis_icml_cpmeasure")
data_dir = proj_dir / Path("data")
halfbrain_path = data_dir / Path("halfbrain_sdata.zarr")

sdata_halfbrain = sd.read_zarr(halfbrain_path)

morpho_cpm_core = sq.exp.calculate_image_features(
    sdata=sdata_halfbrain,
    labels_key="segmentation",
    image_key="stitched_image",
    adata_key_added="morphology",
    n_jobs=32,
    measurements=[
        # "skimage:label",
        # "skimage:label+image",
        "cpmeasure:core",
        # "cpmeasure:correlation",
    ],
    show_progress_bar=True,
    scale="scale1",
    inplace=False,
)

morpho_cpm_core.to_csv(data_dir / "halfbrain_morpho_cpm_core.csv")
