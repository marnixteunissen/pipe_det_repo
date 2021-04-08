
pipe detection - v13 pipe_det_data_08_04_21
==============================

This dataset was exported via roboflow.ai on April 8, 2021 at 6:22 AM GMT

It includes 224 images.
Pipe-ends are annotated in YOLO v5 PyTorch format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Fit (black edges))

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* Randomly crop between 0 and 15 percent of the image
* Random Gaussian blur of between 0 and 0.75 pixels
* Salt and pepper noise was applied to 3 percent of pixels


