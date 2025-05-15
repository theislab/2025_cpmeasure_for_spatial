# download data from https://smi-public.objects.liquidweb.services/muBrainRelease_seurat_noTranscripts.RDS

# install.packages("SeuratObject")
library(SeuratObject)

seurat_obj <- readRDS("./muBrainRelease_seurat_noTranscripts.RDS")
celltype_data <- data.frame(
  cell_barcode = rownames(my_data@meta.data),
  cluster      = my_data@meta.data$RNA_nbclust_clusters,
  cluster_long = my_data@meta.data$RNA_nbclust_clusters_long,
  tissue       = my_data@meta.data$tissue,
  run_tissue   = my_data@meta.data$Run_Tissue_name,
  fov          = my_data@meta.data$fov,
  x_fov_px     = my_data@meta.data$x_FOV_px,
  y_fov_px     = my_data@meta.data$y_FOV_px,
  stringsAsFactors = FALSE
)


write.csv(
  celltype_data,
  "./seurat_celltypes.csv",
  row.names = FALSE
)
