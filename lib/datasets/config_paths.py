import os
import os.path as osp
from easydict import EasyDict as edict

__C = edict()
# Consumers can get config by:
#   from fast_rcnn_config import cfg
PATHS = __C
#Directori on tenim els models preentrenats

__C.load_models_dir = '/work/acarbo/faster_rcnn/data/undrw_models'
__C.load_gt_box_dir = '/work/acarbo/faster_rcnn/data/underwood_dataset/apples/square_annot'

__C.save_results_dir = '/work/acarbo/faster_rcnn/data/underwood_dataset/apples/results_definitiu'
__C.save_images_dir = 'images_underwood'
__C.save_loss_dir = 'output_trainval'
