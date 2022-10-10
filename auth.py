from threading import BrokenBarrierError
from unicodedata import name
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

#takes the path
path = 'users'
images = []
personNames = []
#array to store the Files (img/jpg with file extension)
myList = os.listdir(path)
print(myList)
#for loop to trip the extension and store at personName array and also to read the img using .imread and store at current_Img then passes it to images array
for cu_img in myList:
    current_Img = cv2.imread(f'{path}/{cu_img}')
    images.append(current_Img)
    personNames.append(os.path.splitext(cu_img)[0])
print(personNames)

print ('Starting Encodings This may take while')
#a fuction to convert from BGR to RGB as read img from cv2.imread which read in BGR and all so encode img and store at encode the pass over encodeList Array
# returns encodeList (faces are encoded using face_recognition)
def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

#we are passing the faceencoding fuction to a variable
encodeListKnown = faceEncodings(images)
print('All Encodings Complete!!!')
#starting camera using cv2.VideoCapture
#now the fun fact is i also dont know id to system's cam to i test it with 0-2 as it would be somewhere with in it
# a inifite loop (exits with press of enter)
def auth():
    cap = cv2.VideoCapture(0)
    while True:
        #reading the frame of input
        ret , frame = cap.read()
        #since we don't what will the resolution or the spec of the system it will be runned we are recuding the image quality by 1/4th 
        #faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        #faces = frame
        # again converting BGR to RGB for camera frame
        faces = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # extracting or croping the faces in a frame
        # encoding the frames of capture
        facesCurrentFrame = face_recognition.face_locations(faces)
        encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)
        #loop to compare the faces and get cords of them
        #zip in funtion of python to passs multiple params
        for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            #using numpy to find the nearest face
            # print(faceDis)
            matchIndex = np.argmin(faceDis)
            #mathing the index number of nearnest face to display the face
            if matches[matchIndex]:
                name = personNames[matchIndex].upper()
                #print(name)
                #truth : this portions is copied from a github code
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                ##
            #displaying the cam than exit key is set to [enter]
        cv2.imshow("Jarvis Auth-System", mat=frame)
        if name == "RUDRANIL" or name == "DIPROJYOTI" or name == "SOMODIP":
            break
    cap.release()
    return(name)
auth()
print(auth())
#relaese of camerna port
# and cliose the window
