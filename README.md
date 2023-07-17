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
Pre-Processing ---- This Folder contains different pre-processing techniques that can be applied to improve the results.
    |
    ---- Location_Append_Manhattan.ipynb - This file contains code for adding pixel coordinates to the hyperspectral images.
Result
   |
   ---- HS_conv_images - This folder contains results after running full_system.ipynb for comparing the final salient object and mask(ground truth).
   ---- HS_salmap - This folder contains final salient object we got after running full_system.ipynb.
Salient Object Detection
        |
        Feature Map Extraction Using Clustering - This folder contains files that will be used for extracting salient object using clustering techniques.
        Feature Map Extraction Usint Priors - This folder contains files that will be used for extracting salient object using priors like corner priors, center
                                              priors.

NOTE: You can add more pre-processing like dimension reduction etc. Also in Feature map extraction you can append contrast prior etc or using some other machine learning techniques like isolation forest etc.
