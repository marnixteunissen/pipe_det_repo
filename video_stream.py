import pyrealsense2 as rs
import numpy as np
import cv2
import sys
import os
import cv2


yolo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'yolov5')
if yolo_path not in sys.path:
    sys.path.append(yolo_path)

from yolov5 import detect
from models.experimental import attempt_load

def show_video_stream():
    # configure streams
    pipeline = rs.pipeline()
    config = rs.config()

    # Get device product line for setting a supporting resolution
    pipeline_wrapper = rs.pipeline_wrapper(pipeline)
    pipeline_profile = config.resolve(pipeline_wrapper)
    device = pipeline_profile.get_device()
    print(device)

    # Enable RGB stream
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

    # Start streaming:
    pipeline.start(config)

    while True:
        # Wait for frames
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        if not color_frame:
            print('No frames found')
            continue

        # Convert images to numpy arrays
        color_image = np.asanyarray(color_frame.get_data())

        # Show images
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        # cv2.imshow('RealSense', images)
        cv2.imshow('RealSense', color_image)
        # exiting with 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Stop streaming
    cv2.destroyAllWindows()
    pipeline.stop()


def show_pipe_detection():
    camera = cv2.VideoCapture(1)
    if not camera.isOpened():
        print('Camera not found on channel 1')


def detect_pipe(thresh=0.85, source=1, weights=''):
    if weights == '':
        # Use most recent training
        last_training = []
    elif weights != '':
        # Use specified weights
        file = weights

    model = attempt_load()
    box = []
    return box
