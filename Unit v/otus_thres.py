from pathlib import Path

import cv2


image_path = Path(__file__).resolve().with_name("tof2.png")
image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)


if image is None:
    print(f"img not found: {image_path}")
else:
    val, thresh_otsu = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    print(f"otsu's calculated threshold: {val}")
    output_path = image_path.with_name("otsu_threshold.png")
    cv2.imwrite(str(output_path), thresh_otsu)
    cv2.imshow("Otsu Threshold", thresh_otsu)


