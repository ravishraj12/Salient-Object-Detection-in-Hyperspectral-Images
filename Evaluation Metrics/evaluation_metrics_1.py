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
#converted_files = './HS_cov_images/'
Sorted_final_files = sorted(os.listdir(final_files))
Sorted_mask_files = sorted(os.listdir(mask_files))
def mkdir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

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
save_path = './HS_conv_images/'
mkdir(save_path)
for (file_final, file_mask) in zip(Sorted_final_files, Sorted_mask_files):
  prec_1 =0
  rec_1 = 0
  f1 = 0
  csee = 0;
  ns = 0;
  mae = 0 
  input_final_img = os.path.join(final_files, file_final)
  #print('input_final_img', input_final_img)
  input_mask_img = os.path.join(mask_files, file_mask)
  print('input_mask_img', input_mask_img[:])

  final_img = cv2.imread(input_final_img)
  mask_img = cv2.imread(input_mask_img)
  numpydata_in = np.array(final_img)
  numpydata_in = np.mean(numpydata_in, axis = 2)
  numpydata_in = numpydata_in.astype('uint8')
  #numpydata_in = cv2.medianBlur(numpydata_in,)
  kernel = np.ones((3,3),np.uint8)
  numpydata_in = cv2.erode(numpydata_in,kernel,iterations=1)
  #kernel = np.ones((5,5),np.uint8)
  #numpydata_in = cv2.ximgproc.thinning(numpydata_in)
  
  #kernel_dil = np.ones((38,38),np.uint8)
  #numpydata_in = cv2.dilate(numpydata_in, kernel_dil, iterations =1)
 # print("npy_in", numpydata_in)
  #numpydata_in = cv2.blur(numpydata_in, (3,3))
  save_sal_name = save_path + '/' + input_mask_img[8]+input_mask_img[9]+input_mask_img[10]+input_mask_img[11] + '.jpg'
  cv2.imwrite(save_sal_name, numpydata_in)
  numpydata_out = np.array(mask_img)
  numpydata_out = np.max(numpydata_out, axis = 2)
  #print(numpydata_out.shape)
 # print("npy_out", np.max(numpydata_out))
 # mae = mean_absolute_error(numpydata_in, numpydata_out)
#  ns = nss(numpydata_in, numpydata_out)
 # csee = cc(numpydata_in, numpydata_out)
  prec_1 = medpy.metric.binary.precision(numpydata_in, numpydata_out)
  rec_1 = medpy.metric.binary.recall(numpydata_in, numpydata_out)
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
print("final results are %f \t %f \t %f \t %f \t %f \t %f" %(prec, rec, f1_score_f, nss_f, csee_f, mae_f))
log_path = File_path + "final_results.txt"
with open(log_path, "w") as chosen_res:
    chosen_res.write("prec: %f Rec: %f f1: %f NSS: %f CC: %f MAE: %f \n" %(prec, rec, f1_score_f, nss_f, csee_f, mae_f))

  # print(cv2.imread(input_final_img))
  # print(cv2.imread(input_mask_img))