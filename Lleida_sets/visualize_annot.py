from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pickle
import os
import numpy as np
import cv2

def vis_detections(im, annot):
    """Visual debugging of detections."""
    bbox = tuple(int(np.round(x)) for x in annot)        
    cv2.rectangle(im, bbox[0:2], bbox[2:4], (0, 204, 0), 2)
    
    return im

annopath = '/work/acarbo/faster_rcnn/data/lleida_dataset/annotacions_crop'
imagepath = '/work/acarbo/faster_rcnn/data/lleida_dataset/imatges_crop'
resultpath =  'images_annot'

if not os.path.exists(resultpath):
	os.mkdir(resultpath)
	print("Creating " + resultpath)
xmin_val = 100
ymin_val = 100
xmax_val = 100
ymax_val = 100
#with open('list_to_rotate.txt','wt') as fff:
for it, annofile in enumerate(os.listdir(annopath)):
	#if it == 10:
	#	break
	filename = annofile.split('.txt')[0]
	print(filename)
	with open(os.path.join(annopath,annofile), 'r') as f:
		lines = f.readlines()
		annotations = [x.strip() for x in lines]
	image = cv2.imread(os.path.join(imagepath,filename+'.JPG'))
	print(image.shape)
	'''rows, cols, _ = image.shape
	M = cv2.getRotationMatrix2D((0,0),90,1)
	image = cv2.warpAffine(image,M,(rows,cols))

	print("after rotation",image.shape)'''

	for annot in annotations:
		#print(annot)
		value = annot.split(' ')
		annotation = [float(e) for e in value if e is not '' ]
		#print(annotation)
		if annotation[0]<xmin_val:
			xmin_val = annotation[0]
		if annotation[1]<ymin_val:
			ymin_val = annotation[1]
			
		if annotation[2]>xmax_val:
			xmax_val = annotation[2]
			name = filename
		if annotation[3]>ymax_val:
			ymax_val = annotation[3]

		image = vis_detections(image, annotation)
	savepath = resultpath + '/' + filename + '_annot.JPG'
	print(savepath)
	if image.shape[0] != 1536:
		print(image.shape)
	cv2.imwrite(savepath,image)
	'''	
	if filename == 'DSIR5172':
		print('holaa')
		cv2.imwrite(savepath,image)
	elif filename == 'DSIR5224':
		cv2.imwrite(savepath,image)
	elif filename == 'DSIR5408':
		cv2.imwrite(savepath,image)
	elif filename == 'DSIR5508':
		cv2.imwrite(savepath,image)
	'''

print("xmin",xmin_val)
print("ymin",ymin_val)
print("xmax",xmax_val)
print("ymax",ymax_val)
print("name",name)


