import cv2

# read the QR code image
img = cv2.imread("1.png")

# Luckily for us, OpenCV already got QR code detector built in:
# initialize the cv2 QR code detector
detector = cv2.QRCodeDetector()

# We have the image and the detector, let's detect and decode that data:

# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)

# detectAndDecode() function takes an image as an input and decodes it to
# return a tuple of 3 values:
# the data decoded from the QR code,
# the output array of vertices of the found QR code quadrangle
# and the output image containing rectified and binarized QR code.
#
# We just need data and bbox here, bbox will help us draw the quadrangle in
# the image and data will be printed to the console!


# if there is a QR code

if bbox is not None:
    print(f"QR code data is:\n{data}")
    # display the image with lines
    # length of bounding box

    n_lines = len(bbox)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i + 1) % n_lines][0])
        cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)

# cv2.line() function draws a line segment connecting two points,
# we retrieve these points from bbox array that was decoded by
# detectAndDecode() previously. we specified a blue color ( (255, 0, 0)
# is blue as OpenCV uses BGR colors ) and thickness of 2.

# display the result
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
