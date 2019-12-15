from PIL import Image
import os, sys
name = "normal"
path = os.curdir + "/Dataset/"+name
dirs = os.listdir(path)
new_width, new_height = 360,398



def crop():
    i = 0
    flag = 0
    if not os.path.exists(path+"_dataset"):
        os.makedirs(path+"_dataset")
    if not os.path.exists(path+"_dataset_annotation"):
        os.makedirs(path+"_dataset_annotation")
    for item in dirs:
        fullpath = os.path.join(path,item)         #corrected
        if os.path.isfile(fullpath):
            print("Processing " + str(i) +".....")
            im = Image.open(fullpath)
            width, height = im.size
            left = (width - new_width)/2
            top = (height - new_height)/2
            right = (width + new_width)/2
            bottom = (height + new_height)/2
            f, e = os.path.splitext(fullpath)
            imCrop = im.crop((left, top, right, bottom)) #corrected
            if "mask" in f:
                flag = flag+1
                imCrop.save(os.curdir + "/Dataset/"+name+"_dataset_annotation/"+name+"_"+str(i) + '.png', "png", quality=100)
            else:
                flag=flag+1
                imCrop.save(os.curdir + "/Dataset/"+name+"_dataset/"+name+"_"+str(i) + '.png', "png", quality=100)
            if flag == 2:
                flag = 0
                i= i+1
            

crop()