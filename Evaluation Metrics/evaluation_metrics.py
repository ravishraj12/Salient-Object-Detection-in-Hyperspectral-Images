# -*- coding: utf-8 -*-
"""Evaluation_Metrics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1roH9fI0Q4HMGi9DLEGgG78lAPzO8hou8
"""

#from google.colab.patches import cv2_imshow
from skimage import io
import itertools
import os
import numpy as np
import cv2
import medpy
import math
from medpy import metric
from sklearn.metrics import mean_absolute_error
final_files = './HS_salmap/'
mask_files = './HS_gt/'

Sorted_final_files = sorted(os.listdir(final_files))
Sorted_mask_files = sorted(os.listdir(mask_files))

print("final_files", Sorted_final_files)
print("mask_files", Sorted_mask_files)
def nss(s_map,gt):
	#gt = discretize_gt(gt)
	s_map_norm = (s_map - np.mean(s_map))/np.std(s_map)

	x,y = np.where(gt==1)
	temp = []
	for i in zip(x,y):
		temp.append(s_map_norm[i[0],i[1]])
	return np.mean(temp)


def cc(s_map,gt):
	s_map_norm = (s_map - np.mean(s_map))/np.std(s_map)
	gt_norm = (gt - np.mean(gt))/np.std(gt)
	a = s_map_norm
	b= gt_norm
	r = (a*b).sum() / math.sqrt((a*a).sum() * (b*b).sum());
	return r
prec = 0
rec = 0
nss_f = 0
csee_f = 0
mae_f = 0
f1_score_f = 0
File_path ="./"
for (file_final, file_mask) in zip(Sorted_final_files, Sorted_mask_files):
  input_final_img = os.path.join(final_files, file_final)
  #print('input_final_img', input_final_img)
  input_mask_img = os.path.join(mask_files, file_mask)
  #print('input_mask_img', input_mask_img)

  final_img = cv2.imread(input_final_img)
  mask_img = cv2.imread(input_mask_img)
  numpydata_in = np.array(final_img)
  numpydata_in = np.mean(numpydata_in, axis = 2)
  numpydata_out = np.array(mask_img)
  numpydata_out = np.mean(numpydata_out, axis = 2)
  #print(numpydata_out.shape)
  mae = mean_absolute_error(numpydata_in, numpydata_out)
  ns = nss(numpydata_out, numpydata_in)
  csee = cc(numpydata_out, numpydata_in)
  prec_1 = medpy.metric.binary.precision(numpydata_out, numpydata_in)
  rec_1 = medpy.metric.binary.recall(numpydata_out, numpydata_in)
  if (0.09*prec_1+rec_1) != 0:
    f1  =  1.09*((prec_1*rec_1))/(0.09*prec_1+rec_1)
  else:
    f1 = 0  
# print(final_img.shape)
  # print(mask_img.shape)
  #print("mae", prec_1)
  prec = prec+prec_1
  rec = rec+rec_1
  nss_f = nss_f + ns
  csee_f = csee_f + csee
  mae_f = mae_f + mae
  f1_score_f = f1_score_f + f1 
print("final results are %f \t %f \t %f \t %f \t %f \t %f" %(prec, rec, nss_f, csee_f, mae_f, f1_score_f))
log_path = File_path + "final_results.txt"
with open(log_path, "w") as chosen_res:
    chosen_res.write("prec: %f Rec: %f f1: %f NSS: %f CC: %f MAE: %f \n" %(prec, rec, nss_f, csee_f, mae_f, f1_score_f))

  # print(cv2.imread(input_final_img))
  # print(cv2.imread(input_mask_img))
