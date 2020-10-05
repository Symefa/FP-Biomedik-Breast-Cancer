# FP-Biomedik-Breast-Cancer

a Breast Cancer Segmentation using FCN.

## Datasets

The dataset that being used in this project are DATASET_BUSI from Aly Fahmy
[source](https://scholar.cu.edu.eg/?q=afahmy/pages/dataset) | [mirror](https://dev.poroskolektif.com/Dataset_BUSI.zip)

## Preparation

first we make sure the dimension of data is same for each image file. we choose dimension of 360x398 pixel that resulted an uniform size across all the image file while keeping the area of the mask.

we are using preprocess.py

the next step we split the data into test set and train set you can modify the ratio on splitter.py

finally we transforming the mask so it resulted an image that contain 0 value pixel and 1 value pixel using annotation_fix.py

## train & evaluation

we are using FCN_32 from keras to train the model. and compares it using IOU method.