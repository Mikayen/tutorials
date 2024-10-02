# Exercise #1
# -----------
#
# Load, resize and rotate an image. And display it to the screen.

# TODO First step is to import the opencv module which is called 'cv2'
import cv2 as cv
# TODO Check the opencv version
print(cv.__version__)
# TODO Load an image with image reading modes using 'imread'
# cv2.IMREAD_UNCHANGED  - If set, return the loaded image as is (with alpha
#                         channel, otherwise it gets cropped). Ignore EXIF
#                         orientation.

# cv2.IMREAD_GRAYSCALE  - If set, always convert image to the single channel
#                         grayscale image (codec internal conversion).

# cv2.IMREAD_COLOR      - If set, always convert image to the 3 channel BGR
#                         color image.
img = cv.imread("./tutorials/data/images/logo.png", cv.IMREAD_COLOR)
# TODO Resize image with 'resize'
img = cv.resize(img, (100, 100))
# TODO Rotate image (but keep it rectangular) with 'rotate'
img = cv.rotate(img, cv.ROTATE_180)
# TODO Save image with 'imwrite'

# TODO Show the image with 'imshow'
win_name = "FENSTER"
cv.namedWindow(win_name, cv.WINDOW_AUTOSIZE)
cv.imshow(win_name, img)
cv.waitKey(0)
