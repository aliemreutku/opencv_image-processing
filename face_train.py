import os
import cv2 as cv
import numpy as np


people = ['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']
DIR = r'C:\Users\ALIEMREXE\Desktop\opencv-course-master\Resources\Faces\train'

features = []
labels = []

def crate_train():
    for person in people:
