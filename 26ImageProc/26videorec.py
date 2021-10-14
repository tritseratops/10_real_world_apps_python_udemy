import cv2
import time

#
class VideoRecorder:
    def __init__(self):
        pass

    def start_recording(self):
        video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        video_in_progress = True
        start_counter = 0
        while video_in_progress:
            # cv2.imshow("Frame", frame)
            # time.sleep(2)
            video_in_progress, frame = video.read()
            cv2.imshow("Video", frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                video.release()
                cv2.destroyAllWindows()
                break
        pass

    def end_recording(self):
        pass

    def write_motion_episode(self):
        pass


vr = VideoRecorder()
vr.start_recording()

# video =cv2.VideoCapture(0, cv2.CAP_DSHOW)
# video_in_progress = True
# start_counter=0
# while video_in_progress:
#     # cv2.imshow("Frame", frame)
#     # time.sleep(2)
#     video_in_progress, frame = video.read()
#     cv2.imshow("Video", frame)
#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         video.release()
#         cv2.destroyAllWindows()
#         break
#
#     start_counter +=1
#     # if start_counter>5:
#     #     video.release()
#     #     video_in_progress = False
#
# print(start_counter)
# print(video_in_progress)
# print(frame)

# cv2.imshow("Frame", frame)
# time.sleep(2)
# video.release()
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# gray_img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

# face_cascade = cv2.CascadeClassifier("26haacascades\haarcascade_frontalface_default.xml")

# faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

# for x, y, w, h in faces:
#     face_img = cv2.rectangle( frame,pt1=(x,y), pt2=(x+w, y+h), color=(0,255,0), thickness=3)
#     cv2.imshow("Face", face_img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()