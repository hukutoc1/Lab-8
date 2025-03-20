import cv2
import time


def video_proc():
    cap = cv2.VideoCapture("sample.mp4")
    down_points = (640, 480)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.GaussianBlur(frame, (21, 21), 0)
        ret, thresh = cv2.threshold(frame, 110, 255,
                                    cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(thresh,
                                               cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            a = x + (w // 2)
            b = y + (h // 2)

            s = round(((a - 640 // 2) ** 2 + (b - 480 // 2) ** 2) ** 0.5, 2)
            print(s)
            cv2.putText(img=frame, text=str(s),
                        org=(0, 50),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2,
                        color=(0, 0, 0))

        cv2.imshow("video",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.05)

    cap.release()


video_proc()
cv2.waitKey(0)
cv2.destroyAllWindows()