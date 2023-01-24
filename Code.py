import cv2
import pytesseract as tess
import matplotlib.pyplot as plt
import numpy as np

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def empty(a):
    pass

# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars", 640, 240)
# cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
# cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
# cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
# cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
# cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
# cv2.createTrackbar("Val Max", "TrackBars", 219, 255, empty)

def getContours(img):
    cont_count = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 100:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)

            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cont_count += 1

    return (cont_count)

count = 0
#For printing (once) if note is Real of fake

Note = int(input("Enter which Note to choose: "))

while True:
    # Reading the Image
    if Note == 100:
        img = cv2.imread(r'og100.JPG')
    elif Note == 500:
        img = cv2.imread(r'duplicate500.jpeg')
    elif Note == 2000:
        img = cv2.imread(r'og2000.JPG')

    img_resize = cv2.resize(img, (600, 250))

    #NUMBER
    if Note == 100:
        imgCropped_no = img_resize[135:175, 510:532]
        lower_no = np.array([0, 0, 0])
        upper_no = np.array([179, 255, 215])
    elif Note == 500:
        imgCropped_no = img_resize[117:161, 503:524]
        lower_no = np.array([0, 0, 0])
        upper_no = np.array([179, 255, 178])
    elif Note == 2000:
        imgCropped_no = img_resize[111:175, 510:544]
        lower_no = np.array([0, 0, 0])
        upper_no = np.array([179, 255, 203])

    imgHSV_no = cv2.cvtColor(imgCropped_no, cv2.COLOR_BGR2HSV)
    # h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    # h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    # s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    # s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    # v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    # v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    # print(h_min, h_max, s_min, s_max, v_min, v_max)
    # lower_no = np.array([h_min, s_min, v_min])
    # upper_no = np.array([h_max, s_max, v_max])
    mask_no = cv2.inRange(imgHSV_no, lower_no, upper_no)
    imgResult_no = cv2.bitwise_and(imgCropped_no, imgCropped_no, mask=mask_no)

    # cv2.imshow("Original",img)
    # cv2.imshow("HSV",imgHSV_no)
    # cv2.imshow("Mask", mask_no)
    # cv2.imshow("Result", imgResult_no)

    Titles1= ["Cropped Part", "HSV", "Mask", "Final Image"]
    images1 = [imgCropped_no, imgHSV_no, mask_no, imgResult_no]
    count2 = 4

    for i in range(count2):
        plt.subplot(2, 2, i + 1)
        plt.title(Titles1[i])
        plt.imshow(images1[i])
    plt.show()

    imgRotate_no = cv2.rotate(imgResult_no, cv2.cv2.ROTATE_90_CLOCKWISE)
    imgRotate_no = cv2.resize(imgRotate_no, (600, 250))
    cv2.imshow("Rotated", imgRotate_no)

    output = tess.image_to_string(imgRotate_no)

    # STRIP
    if Note == 100:
        imgCropped_strip = img_resize[:, 324:365]
        lower_strip = np.array([0, 0, 108])
        upper_strip = np.array([179, 205, 235])
    elif Note == 500:
        imgCropped_strip = img_resize[:, 322:360]
        lower_strip = np.array([0, 11, 98])
        upper_strip = np.array([179, 255, 255])
    elif Note == 2000:
        imgCropped_strip = img_resize[:, 330:365]
        lower_strip = np.array([0, 0, 100])
        upper_strip = np.array([179, 255, 255])

    imgHSV_strip = cv2.cvtColor(imgCropped_strip, cv2.COLOR_BGR2HSV)
    mask_strip = cv2.inRange(imgHSV_strip, lower_strip, upper_strip)
    imgResult_strip = cv2.bitwise_and(imgCropped_strip, imgCropped_strip, mask=mask_strip)

    Titles2 = ["Cropped Strip", "HSV", "Mask", "Final Strip"]
    images2 = [imgCropped_strip, imgHSV_strip, mask_strip, imgResult_strip]
    count3 = 4

    for i in range(count3):
        plt.subplot(2, 2, i + 1)
        plt.title(Titles2[i])
        plt.imshow(images2[i])
    plt.show()

    # STRIP DETECTION

    imgContour = imgResult_strip.copy()
    imgGray = cv2.cvtColor(imgResult_strip, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(7, 7),0)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    cont_count = getContours(imgCanny)

    Titles1= ["Cropped Strip", "Gray Img", "Blur Img", "Canny Img ", "Contour Img"]
    images1 = [imgCropped_strip, imgGray, imgBlur, imgCanny, imgContour]
    count1 = 5

    for i in range(count1):
        plt.subplot(2, 3, i + 1)
        plt.title(Titles1[i])
        plt.imshow(images1[i])
    plt.show()

    #OUTPUT

    output_list = output.split()
    if ((len(output_list) != 0) and (count == 0) and (cont_count <=1)):
        note1 = cv2.imread(r'REAL.jpeg')
        cv2.imshow('image', note1)
        count = 1
    elif ((count != 1) or ((cont_count > 1) and count != 1)):
        note2 = cv2.imread(r'FAKE.jpeg')
        cv2.imshow('image', note2)
        count = 1

    cv2.waitKey(0)