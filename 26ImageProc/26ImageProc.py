import cv2
import glob
import re
import os

# img = cv2.imread("galaxy.jpg", 1)
#
# print(type(img))
# print(img.shape)
# print(img.ndim)
#
# # resized_img = cv2.resize(img, (1000,500))
# # resized_img = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
# resized_img = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
# cv2.imwrite("resized_galaxy.jpg", resized_img)
# cv2.imshow("Galaxy",resized_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# available_files = glob.glob("images\*.jpg")
# print(available_files)
# available_filenames = [(re.search(r'images\\(.*).jpg', x)).group(1) for x in available_files]
# if not os.path.isdir('resized'):
#     os.mkdir('resized')
#
# for img_file in available_files:
#     img = cv2.imread(img_file, 1)
#     resized_img = cv2.resize(img, (100,100))
#     result_file_path = img_file.replace('images', 'resized')
#     print(result_file_path)
#
#     cv2.imwrite(result_file_path, resized_img)
# #
# file_path = f"quotes\{input}.txt"
# with open(file_path, encoding="UTF-8")


# one face

# face_cascade = cv2.CascadeClassifier("26haacascades/haarcascade_frontalface_default.xml")
#
# img = cv2.imread("26haacascades/photo.jpg")
#
# gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#
# faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
# print(type(faces))
# print(faces)
#
# for x, y, w, h in faces:
#     face_img = cv2.rectangle( img,pt1=(x,y), pt2=(x+w, y+h), color=(0,255,0), thickness=3)
#     # cv2.imshow("Face", face_img)
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()
#
# resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
# cv2.imshow("Face", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# many faces

face_cascade = cv2.CascadeClassifier("26haacascades/haarcascade_frontalface_default.xml")

img = cv2.imread("26haacascades/news.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)
print(type(faces))
print(faces)

for x, y, w, h in faces:
    face_img = cv2.rectangle( img,pt1=(x,y), pt2=(x+w, y+h), color=(0,255,0), thickness=3)
    cv2.imshow("Face", face_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
# cv2.imshow("Face", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()