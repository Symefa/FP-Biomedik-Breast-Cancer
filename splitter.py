import os
name = "normal"
path = os.curdir + "/Dataset/"+name


mask_dir=path+"_dataset_annotation"
dat_dir =path+"_dataset"
dirs = os.listdir(mask_dir)
if not os.path.exists(path+"_test"):
        os.makedirs(path+"_test")
if not os.path.exists(path+"_test_mask"):
        os.makedirs(path+"_test_mask")
import shutil
import numpy as np
for f in dirs:
    if np.random.rand(1) < 0.2:
        shutil.move(dat_dir + '/'+ f, path+"_test" + '/'+ f)
        shutil.move(mask_dir + '/'+ f, path+"_test_mask" + '/'+ f)