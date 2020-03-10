import os
import cv2
import numpy as np
from scipy import io as sio
from bbox import annotate_bbox


dir_path = "./egohands_data/_LABELLED_SAMPLES/"
annotation_dir = "./Annotations"

def dump_vocformat(base_path, dir):
    image_path_array = []
    for root, dirs, filenames in os.walk(base_path + dir):
        for f in filenames:
            if(f.split(".")[1] == "jpg"):
                img_path = base_path + dir + "/" + f
                image_path_array.append(img_path)

    image_path_array.sort()
    boxes = sio.loadmat( base_path + dir + "/polygons.mat")
    polygons = boxes["polygons"][0]
    pointindex = 0

    for first in polygons:
        index = 0

        img_id = image_path_array[pointindex]
        img = cv2.imread(img_id)
        dir_name = img_id.split('/')[-2]
        annotation_name = dir_name+'_'+os.path.basename(img_id).split('.')[0]+'.xml'

        pointindex += 1

        bbstatus_list = []
        name_tag_list = ["hand" for _ in first]
        image_shape = img.shape
        for pointlist in first:
            max_x = max_y = min_x = min_y = height = width = 0

            findex = 0
            for point in pointlist:
                if(len(point) == 2):
                    x = int(point[0])
                    y = int(point[1])

                    if(findex == 0):
                        min_x = x
                        min_y = y
                    findex += 1
                    max_x = x if (x > max_x) else max_x
                    min_x = x if (x < min_x) else min_x
                    max_y = y if (y > max_y) else max_y
                    min_y = y if (y < min_y) else min_y
                    bbstatus_list.append([min_x, min_y, max_x, max_y])
        xml = annotate_bbox(bbstatus_list, annotation_name, image_shape, name_tag_list)
        with open(os.path.join(annotation_dir, annotation_name), 'w') as annotation_file:
            annotation_file.write(xml)


for root, dirs, filenames in os.walk(dir_path):
    for dir in dirs:
        dump_vocformat(dir_path, dir)
