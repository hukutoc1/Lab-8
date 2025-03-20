import cv2


def image_proc():
    image = cv2.imread("images/variant-7.jpg")
    image = cv2.flip(image, 0)

    cv2.imshow("Image2", image)


image_proc()
cv2.waitKey(0)
cv2.destroyAllWindows()