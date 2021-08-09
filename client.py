#!/usr/bin/env python3

"""
ROS Düğümü Oluşturma
"""

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from prediction import prediction
import config
import utils

class Kamera():
    def __init__(self):
        self.model = utils.model_load()
        rospy.init_node("kamera_dugumu")
        self.bridge = CvBridge()
        rospy.Subscriber("camera/rgb/image_raw", Image, self.kameraCallback)
        rospy.spin()

    def kameraCallback(self, mesaj):
        image = self.bridge.imgmsg_to_cv2(mesaj, "bgr8") # bu dönüştürme işlemini kendi yönteminiz ile yapın bence. Ben hızlı olsun diye
                                                         # turtlebot3 üzerinden yaptım diye bu kütüphaneyi kullandım ama sonuçlar orjinal resimler kadar iyi değil bence
        transform = config.pred_transforms(image=image)
        image = transform["image"]
        classes = prediction(image, self.model)
        cv2.waitKey(1)

Kamera()