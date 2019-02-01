import face_recognition
import cv2 as cv
#import sent
video_capture = cv.VideoCapture(0)
process_this_frame = True

while True:
    ret, frame = video_capture.read()

    small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame, model='cnn')
        if not face_locations:
            print("no face")
        else:
            print ("face detected")
           # cv.imwrite('img.jpg',rgb_small_frame)
            #sent.SendMail('img.jpg')
            #break
    cv.imshow('Video', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv.destroyAllWindows()
