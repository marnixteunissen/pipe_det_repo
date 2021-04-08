using transfer learning in yolov5:
https://github.com/ultralytics/yolov5/issues/1314

W&B workspace: 
https://wandb.ai/marnixteunissen/YOLOv5?workspace=user-marnixteunissen

Dataset:
https://app.roboflow.com/dataset/pipe-detection

transfer learning command:

python train_transfer.py --batch 8 --epochs 2 --data ../pipe_det_data_07_04_21/data.yaml --cfg models/yolov5s.yaml --weights yolov5s.pt --name yolov5s_pip_det

python train_transfer.py --batch 8 --epochs 100 --data ../pipe_det_data_07_04_21/data.yaml --cfg models/yolov5x.yaml --weights yolov5x.pt --name yolov5x_pip_det