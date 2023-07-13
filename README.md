# Salient-Object-Detection-in-Hyperspectral-Images
For better understand of the details please view this file in code view instead of preview mode.
Different Folders and Their Contents details:
Evaluation Metrics Folder
          |
          ----This folder contains evaluation_metrics.py file which is used to calculate Evaluation Metrics like Precision, Recall, and F1-Score.
          ----Evaluation_metrics_1.py also calculate Evaluation Metrics but we can optimize it using different erosion and dilation kernel code which are provided 
              in the file itself.
Ground Truth
       |
       ----HS_gt - This folder contain ground truth images(mask) for the input images.
Post-Processing ---- This Folder contains different post-processing techniques that can be applied to improve the results.
     |
     ----- NMS.ipynb - This file contains code for NMS technique applied on the input image for file object in non-redundant bounding boxes.
     ----- NMS_Boundary.ipynb - This file contains code for boundary pixel ratio which is used to keeping the salient object intact and removing the boundary noises.
     ----- NMS_bounding_boxes.ipynb - This file also contains code for boundary pixel ratio.
     ----- bounding_boxes_merge.ipynb - This file contains code for merging two bounding boxes.
     ----- erosion.ipynb - This file contains code for erosion and dilation operation.
     ----- gt_modifier.ipynb - This file contains code for modifying the ground truth.
     ----- normalise_band.ipynb - This file contains code for normalize each band in hyperspectral images.
     ----- normalise_band_max.py - This file contains code for normalize each band in hyperspectral images using max operation.
     ----- Full_system.ipynb - This file contains code for all the post-processing techniques mentioned above in one file.
  
