"""
Implementation of MEV-SFS algorithm
Detail can be found in paper "A Geometry-Based Band Selection
Approach for Hyperspectral Image Analysis" in Algorithm 1
"""

#from osgeo import gdal
import numpy as np
#from tqdm_progress import TqdmUpTo
import scipy.io as scio
import matplotlib.pyplot as plt
import h5py
import mat73
from PIL import Image
import PIL
import cv2
import os

def mkdir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def main():
    File_path = './HS_images/' 
    HS_files = os.listdir(File_path)
    print("HS_files", HS_files)
    num = 0;
    save_path = './HS_Results/'
    mkdir(save_path)
    sal_result_path = os.path.join(save_path, 'sal_result')
    mkdir(sal_result_path)

    remove_bands = []
    for file in HS_files:
        input_img = os.path.join(File_path, file)
        print("Reading File[%d/%d]: %s" % (num, len(HS_files), input_img))
        mat_dict = mat73.loadmat(input_img)
        
        for key in mat_dict:
            if type(mat_dict[key]) is np.ndarray:
                image_data = mat_dict[key]  # type: np.ndarray

        image_normal = []
   
        for i in range(0,81):
            print("image data", image_data.shape)
            image_data_1_band = image_data[:,:,i]
            image_data_1_band = np.array(image_data_1_band)
            max_band = np.max(image_data_1_band)
            #print("image data is", image_data_1_band)
            image_data_1_band = image_data_1_band/max_band
            print("image data band shape", image_data_1_band.shape)
            image_normal.append(image_data_1_band)
        im_norm = np.array(image_normal)
        print("normalise image", im_norm.shape)
        #im_norm = im_norm.reshape(768,1024,81)
        #print("image",np.max(image_data_1_band))
        
    
        file = file.rsplit('.', 1)
        save_sal_name = sal_result_path + '/' + file[0] + '.mat'
    #cv2.imwrite(save_sal_name, salmap_final)
        scio.savemat(save_sal_name, {'mydata': im_norm})
    
    
if __name__ == "__main__":
    main()
