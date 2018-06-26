from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import os
import numpy as np
import pandas as pd
import shutil
import PIL
from PIL import Image
import pdb
from lxml import etree as ET

from lib.model.utils.config import cfg

path = os.path.join(cfg.DATA_DIR,'underwood_dataset','apples','annotations')
Files = os.listdir(path)
save_dir = os.path.join(cfg.DATA_DIR,'underwood_dataset','apples','square_annotations')
img_dir = os.path.join(cfg.DATA_DIR,'underwood_dataset','apples','images')
if os.path.exists(save_dir):
	shutil.rmtree(save_dir)
	os.makedirs(save_dir)


for file in Files:
	full_filename = os.path.join(path,file)
	width = PIL.Image.open(os.path.join(img_dir,file.split(".csv")[0] + ".png")).size[0]
	height = PIL.Image.open(os.path.join(img_dir,file.split(".csv")[0] + ".png")).size[1]
	circles = pd.read_csv(full_filename)
	circles = circles.values	
	xmin = circles[:,1] - circles[:,3] - 1
	xmax = circles[:,1] + circles[:,3] - 1
	ymin= circles[:,2] - circles[:,3] - 1
	ymax = circles[:,2] + circles[:,3] - 1
	for index, item in enumerate(xmin):
		if item < 0:
			xmin[index] = 0	
	for index, item in enumerate(ymin):
		if item < 0:
			ymin[index] = 0
	for index, item in enumerate(xmax):
		if item > width:
			xmax[index] = width - 1
	for index, item in enumerate(ymax):
		if item > height:
			ymax[index] = height - 1
	
	f = ET.Element("annotations")
	ET.SubElement(f,'filename').text = file.split(".csv")[0] + ".png"
	thesize = ET.SubElement(f,'size')
	ET.SubElement(thesize,'width').text = str(width)
	ET.SubElement(thesize,'height').text = str(height)
	ET.SubElement(thesize,'depth').text = "3"
	for i in range(len(xmin)):

		obj = ET.SubElement(f,'object')
		ET.SubElement(obj,'name').text = "Poma"
		ET.SubElement(obj,'difficult').text = "0"
		bbox = ET.SubElement(obj,'bbox')
		xmin_xml = ET.SubElement(bbox,'xmin')
		xmax_xml = ET.SubElement(bbox,'xmax')
		ymin_xml = ET.SubElement(bbox,'ymin')
		ymax_xml = ET.SubElement(bbox,'ymax')		
		xmin_xml.text = str(int(xmin[i]))
		xmax_xml.text = str(int(xmax[i]))
		ymin_xml.text = str(int(ymin[i]))
		ymax_xml.text = str(int(ymax[i]))
	filename = os.path.join(save_dir,file.split(".csv")[0] + ".xml")
	tree = ET.ElementTree(f)
	tree.write(filename, pretty_print = True)
	





	