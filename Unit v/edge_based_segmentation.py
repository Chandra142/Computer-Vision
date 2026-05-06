from pathlib import Path

import cv2
import numpy as np


image_path = Path(__file__).resolve().with_name("e_bsd_sgmnt.jpg")
image = cv2.imread(str(image_path))

if image is None:
    print(f"error : image not found: {image_path}")
else:
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)

    sobel_combined = cv2.magnitude(sobel_x, sobel_y)

    sobel_final = np.uint8(np.absolute(sobel_combined))

    output_path = image_path.with_name("sobel_magnitude.png")
    cv2.imwrite(str(output_path), sobel_final)
    print(f"saved sobel magnitude to: {output_path}")