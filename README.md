# Counterfeit-Currency-Detection

Countries in all parts of the world make use of paper currency to exchange goods and value. One major problem faced by many countries related to currency, is the existence of counterfeit currency in the system.


## Project Description
The process of identification is done by extracting the features such as security thread and watermark of the numeral of the given Indian currency and comparing it with the extracted features of the original currency with the help of image processing techniques like Canny edge detection, Gaussian Blur using OpenCV.

## Extracted Features
1) Watermark of the Numeral: As the watermark of the numeral is in a vertical format, so it is rotated and then by using OCR image is converted to text conversion. </br>
2) Security Thread: The image is converted into grey scale then to Gaussian blur to reduce noise from the image. The blurred image is now converted into canny for edge detection. Finally, we get the contours.
