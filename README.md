# Preprocessing EgoHands Dataset for Object Detection
This repository is preprocess scripts for Hand Detection.  
Using script, you can generate Annotation XML file that is PASCAL-VOC format.

## How to use

```
$ cd EgoHandsDataPreprocess
$ wget http://vision.soic.indiana.edu/egohands_files/egohands_data.zip
$ unzip egohands_data
$ mkdir Annotations
$ python convert_vocformat.py
```
