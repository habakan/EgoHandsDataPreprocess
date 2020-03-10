import os
import re
import xml.etree.ElementTree as xml_tree

from bs4 import BeautifulSoup


def read_bbox(file_path):
    tree = xml_tree.parse(file_path)
    root = tree.getroot()
    obj = root.find('object')
    bbox = obj.find('bndbox')
    bbox = [
        int(bbox.find('xmin').text),
        int(bbox.find('ymin').text),
        int(bbox.find('xmax').text),
        int(bbox.find('ymax').text)
    ]
    name_tag = obj.find('name').text

    return bbox, name_tag


def simpletag(tagname, item):
    return '<' + tagname + '>' + str(item) + '</' + tagname + '>'


def annotate_bbox(bbstatus_list, filename_tag, image_shape, name_tag_list):
    xml = ''
    xml += '<annotation>'
    xml += simpletag('folder', 'WIDER')
    xml += simpletag('filename', filename_tag)

    xml += '<size>'
    # WARN:width and height swapped!!!
    xml += simpletag('width', image_shape[1])
    xml += simpletag('height', image_shape[0])
    xml += simpletag('depth', image_shape[2])
    xml += '</size>'

    for bbstatus, name_tag in zip(bbstatus_list, name_tag_list):
        xml += '<object>'
        xml += simpletag('name', name_tag)
        xml += simpletag('truncated', 0)
        xml += simpletag('difficult', 0)
        xml += '<bndbox>'
        xml += simpletag('xmin', int(bbstatus[0]))
        xml += simpletag('ymin', int(bbstatus[1]))
        xml += simpletag('xmax', min(int(bbstatus[2]), image_shape[1]))
        xml += simpletag('ymax', min(int(bbstatus[3]), image_shape[0]))
        xml += '</bndbox>'
        xml += '</object>'

    xml += '</annotation>'
    return xml
