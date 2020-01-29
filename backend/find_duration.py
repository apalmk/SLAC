import cv2
import math

def find_duration(path):
    cap = cv2.VideoCapture(path)
    tfc = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fr = cap.get(5)
    fr = math.floor(fr)
    duration = math.floor(tfc / fr)
    return duration

# print(find_duration("E://projectImplementation//projectFiles//frames//FYP//test_case2.mp4"))
