import cv2


def main():
    video = "data/2.mp4"
    cap = cv2.VideoCapture(video)
    if cap.isOpened():
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()
    return None


if __name__ == "__main__":
    main()
