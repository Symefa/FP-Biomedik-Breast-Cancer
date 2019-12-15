from PIL import Image
import os

name = "image"
path = os.curdir + "/datasetfinal/"+name


test_dir=path+"_test_annotation"
train_dir=path+"_train_annotation"

dirs = os.listdir(test_dir)
for f in dirs:
    fullpath = os.path.join(test_dir,f) 
    if os.path.isfile(fullpath):
        img=Image.open(fullpath)
        pixels = img.load()
        img = img.convert('L')
        for i in range(img.size[0]): # for every pixel:
            for j in range(img.size[1]):
                if pixels[i,j] != 0:
                    img.putpixel((i,j),1)
        img.save(fullpath)


dirs = os.listdir(train_dir)

for f in dirs:
    fullpath = os.path.join(train_dir,f) 
    if os.path.isfile(fullpath):
        img=Image.open(fullpath)
        pixels = img.load()
        img = img.convert('L')
        for i in range(img.size[0]): # for every pixel:
            for j in range(img.size[1]):
                if pixels[i,j] != 0:
                    img.putpixel((i,j),1)
        img.save(fullpath)
