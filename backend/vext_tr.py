import cv2
import  math
cap = cv2.VideoCapture('E://projectImplementation//projectFiles//frames//trial//single_person_all.mp4')
imagesloc = "E://projectImplementation//projectFiles//frames//testt//"

frame_number = 0
tfc= cap.get(cv2.CAP_PROP_FRAME_COUNT)
fr = cap.get(5) #gets the frame rate of the video
fr= math.floor(fr)
duration=math.floor(tfc/fr)
print(duration)
print(tfc)
print(fr)
i=1
while frame_number<= tfc and i<=duration:
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    success, frame = cap.read()
    filename=imagesloc+"frame_"+str(i)+".jpg"
    cv2.imwrite(filename, frame)
    frame_number=frame_number+fr
    i=i+1

imgg=cv2.imread(imagesloc+"frame_"+str(duration-1)+".jpg")
cv2.imwrite(imagesloc+"frame_"+str(duration)+".jpg",imgg)