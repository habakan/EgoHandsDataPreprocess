import os
import shutil
import cv2


base_path = "./egohands_data/_LABELLED_SAMPLES/"
out_img_dir_path = "./JPEGImages/"

for root, dirs, filenames in os.walk(base_path):
    for dir in dirs:
        for root, dirs, filenames in os.walk(base_path + dir):
            for f in filenames:
                if(f.split(".")[1] == "jpg"):
                    img_path = base_path + dir + "/" + f
                    shutil.move(img_path, os.path.join(out_img_dir_path, dir+"_"+f))
