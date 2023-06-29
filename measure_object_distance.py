import cv2
from realsense_camera import *
from mask_rcnn import *

# Load Realsense camera
rs = RealsenseCamera()
mrcnn = MaskRCNN()
""" class_names = []
with open('dnn/classes.txt', 'r') as file:
    for line in file:
        class_names.append(line.strip())""" 
while True:
    # Get frame in real time from Realsense camera
    ret, bgr_frame, depth_frame = rs.get_frame_stream()

    boxes, classes, contours, centers = mrcnn.detect_objects_mask(bgr_frame)
    mrcnn.draw_object_info(bgr_frame, depth_frame)
    
    #cv2.imshow("depth frame", depth_frame)
    cv2.imshow("Bgr frame", bgr_frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
"""
import cv2
from realsense_camera import *
from mask_rcnn import *

# Load Realsense camera
rs = RealsenseCamera()
mrcnn = MaskRCNN()

# Load object names from file
class_names = []
with open('dnn/classes.txt', 'r') as file:
    for line in file:
        class_names.append(line.strip())

while True:
    # Get frame in real time from Realsense camera
    ret, bgr_frame, depth_frame = rs.get_frame_stream()

    boxes, classes, contours, centers = mrcnn.detect_objects_mask(bgr_frame)

    # Check if "person" class is detected
    if "person" in class_names:
        person_index = class_names.index("person")
        if person_index in classes:
            print("Detected")

    mrcnn.draw_object_info(bgr_frame, depth_frame, class_names)  # Pass class names to the draw_object_info function

    # cv2.imshow("depth frame", depth_frame)
    cv2.imshow("Bgr frame", bgr_frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
  """

