import cv2, pandas
import datetime

background_frame = None
video =cv2.VideoCapture(0, cv2.CAP_DSHOW)
video_in_progress = True
# check, background_frame = video.read()
motion_start = None
motions = []
while video_in_progress:
    motion_detected = False
    video_in_progress, frame = video.read()
    gray_frame = cv2.cvtColor(src=frame, code=cv2.COLOR_RGB2GRAY)
    gray_frame = cv2.GaussianBlur(src=gray_frame, ksize=(21,21), sigmaX=0)
    if background_frame is None:
        background_frame = gray_frame
        continue

    delta_frame = cv2.absdiff(background_frame, gray_frame)

    sug_thresh, threshhold_delta_frame = cv2.threshold(src=delta_frame, thresh=30, maxval=25, type=cv2.THRESH_BINARY)

    # smoth delta
    threshhold_delta_frame = cv2.dilate(src=threshhold_delta_frame, kernel=None, iterations=2)

    contours, _ = cv2.findContours(image=threshhold_delta_frame.copy(), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour)<10000:
            continue
        # check if motion started
        if motion_start is None:
                motion_start = datetime.datetime.now()
        motion_detected = True
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(img=frame, pt1=(x,y), pt2=(x+w,y+h), color=(0,255,0),thickness=3)

    # check if motion stopped
    if not motion_detected and not motion_start is None:
        motion_end= datetime.datetime.now()
        motions.append({"Start": str(motion_start), "End": str(motion_end)})
        motion_start = None
    cv2.imshow("Video", gray_frame)
    cv2.imshow("Delta", delta_frame)
    cv2.imshow("Threshhold", threshhold_delta_frame)
    cv2.imshow("Motion", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        # check for last motion
        if not motion_start is None:
            motions.append({"Start": str(motion_start), "End": str(datetime.datetime.now())})
        break
    # print(motion_detected)

# print(motions)
df = pandas.DataFrame(columns=["Start", "End"])
for motion in motions:
    print(motion)
    df = df.append(motion, ignore_index=True)
print(df)
df.to_csv("motions.csv")
video.release()
cv2.destroyAllWindows()
