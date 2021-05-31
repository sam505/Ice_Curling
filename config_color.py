import cv2
import numpy as np


def on_change():
    pass


image = cv2.imread("config_color.png")
image = cv2.resize(image, (400, 260))
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 360)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, on_change)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, on_change)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, on_change)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, on_change)
cv2.createTrackbar("VAL Min", "HSV", 0, 255, on_change)
cv2.createTrackbar("VAL Max", "HSV", 255, 255, on_change)


def main():
    while True:
        img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        h_min = cv2.getTrackbarPos("HUE Min", "HSV")
        h_max = cv2.getTrackbarPos("HUE Min", "HSV")
        s_min = cv2.getTrackbarPos("SAT Min", "HSV")
        s_max = cv2.getTrackbarPos("SAT Max", "HSV")
        v_min = cv2.getTrackbarPos("VAL Min", "HSV")
        v_max = cv2.getTrackbarPos("VAL Max", "HSV")

        min = np.array([h_min, s_min, v_min])
        max = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(img_hsv, min, max)
        result = cv2.bitwise_and(image, image, mask=mask)
        cv2.imshow("Image", image)
        cv2.imshow("Mask", mask)
        cv2.imshow("Result", result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    return None


if __name__ == "__main__":
    main()
