import cv2

image_path = '' #Path to image
image = cv2.imread(image_path)

cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow('Kamera', frame)

    key = cv2.waitKey(1)
    if key == ord('x'):
        print('Zapisywanie obrazu na dysku')
        cv2.imwrite('Zapisane_zdjecie.jpg', frame)
        break
    elif key == ord('q'):
        print('Opuszczanie programu')
        break

cap.release()
cv2.destroyAllWindows()