#!/usr/bin/env python3

"""
ROS Düğümü Oluşturma
"""

import rospy
import cv2
import PIL
from sensor_msgs.msg import Image
from prediction import prediction
import config
import utils
import time
import numpy as np

class Kamera():
    def __init__(self):
        self.model = utils.model_load()
        rospy.init_node("kamera_dugumu")
        rospy.Subscriber("/cart/front_camera/image_raw", Image, self.kameraCallback)
        rospy.spin()

    def kameraCallback(self, mesaj):
        time.sleep(0.5)
        image = np.frombuffer(mesaj.data, dtype=np.uint8).reshape(mesaj.height, mesaj.width, 3)[..., ::-1]
        cv2.imwrite("obj_det_im.jpg", image)
        image = np.array(PIL.Image.open("obj_det_im.jpg").convert("RGB"))    
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)                                     
        transform = config.pred_transforms(image=image)
        image = transform["image"]
        classes = prediction(image, self.model) # sahnede tespit edilen nesneleri liste olarak döner.
        print(classes)
        cv2.waitKey(1)

Kamera()