import torch
import os
import sys

current_dir = os.path.dirname(__file__)
yolo_dir = os.path.join(current_dir, 'yolov5')
print(yolo_dir)
sys.path.append(yolo_dir)
print(sys.path)
os.system('python train_transfer.py --batch 8 --epochs 2 --data ../pipe_det_data_08_04_21/data.yaml --cfg models/yolov5s.yaml --weights yolov5s.pt --name yolov5s_pip_det')

