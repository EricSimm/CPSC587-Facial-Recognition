# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 18:22:42 2017

@author: Administrator
"""

import dlib
import cv2
import numpy as np
from sklearn import preprocessing, cross_validation, neighbors, svm
import os
import csv
#ap = argparse.ArgumentParser()
#ap.add_argument("-p", "--shape-predictor", metavar="D:\\用户目录\\下载\\shape_predictor_68_face_landmarks.dat\\shape_predictor_68_face_landmarks.dat", required=True,
#	help="path to facial landmark predictor")
#ap.add_argument("-r", "--picamera", type=int, default=-1,
	#help="whether or not the Raspberry Pi camera should be used")
#args = vars(ap.parse_args())
motherfucker = "C:\\Users\\Administrator\\shape_predictor_68_face_landmarks.dat"
face_recognition_model= "C:\\Users\\Administrator\\dlib_face_recognition_resnet_model_v1 (1).dat"
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(motherfucker)
face_encoder = dlib.face_recognition_model_v1(face_recognition_model)

print("[INFO] camera sensor warming up...")
#vs = VideoStream().start()
#video_capture = cv2.VideoCapture(0)
#time.sleep(2.0)

path = "E:\\faces"
s = os.listdir(path)

people = []
names = ["Eric Simmons", "Tiffany Lin", "Viraj Deshwal", "Zenan Li"]
count = 1
for i in s:
    for name in names:
        if str(i).find(name)>-1:
            document = os.path.join(path,i)
            pics = os.listdir(document)
            for index in pics:
                pic = os.path.join(document,index)
                print(pic)
                image = cv2.imread(pic)
                try:
                    faceDetect = detector(image, 1)
                    shape = predictor(image, faceDetect[0])
                    face_encoding = face_encoder.compute_face_descriptor(image, shape, 1)
                    features = list(face_encoding)
                    features.insert(0,name)
                    people.append(features)
                    print(features)
                except:
                    pass
csvfile = open("E:\\test.csv","w",newline='')
writer = csv.writer(csvfile)
writer.writerows(people)
csvfile.close()
"""measurement = open("E:\\data.txt", 'w')
for person in people:
    measurement.writelines(str(person)+'\n')
measurement.flush()
measurement.close()
"""
"""
    chris_image = cv2.imread('E:\\TiffanyFace-preprocessed\\tiffany_lin_5.png')
#chris_image_gray = cv2.cvtColor(chris_image, cv2.COLOR_GRAY2RGB)
chris = detector(chris_image, 1)
chris_shape = predictor(chris_image, chris[0])
chris_face_encoding = face_encoder.compute_face_descriptor(chris_image, chris_shape, 1)
hey = list(chris_face_encoding)
f = open('E:\\blogCblog.txt', 'w')
print(hey)
chris_image = cv2.imread('E:\\49.png')
#chris_image_gray = cv2.cvtColor(chris_image, cv2.COLOR_GRAY2RGB)
chris = detector(chris_image, 1)
chris_shape = predictor(chris_image, chris[0])
chris_face_encoding = face_encoder.compute_face_descriptor(chris_image, chris_shape, 1)
print("chrisli:"+str(chris_face_encoding))
"""