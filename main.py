import cv2
import numpy as np
from ORBFeature import ORBFeature, show_match


def read_image(image_name: str, folder: str) -> np.ndarray:
    image = cv2.imread(folder + image_name)
    # cv2.imshow("bird.jpg", image)
    # cv2.waitKey(0)
    return image


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    image_data1 = read_image('house1.jpg', '')
    # print(image_data.shape)
    # print(type(image_data))
    gray_image_data1 = cv2.cvtColor(image_data1, cv2.COLOR_BGR2GRAY)
    # fast = OrientedFast(gray_image_data, 9, 0.2)
    # fast.detector()
    # fast.show_interest_points(image_data)
    orb1 = ORBFeature(gray_image_data1, 12, 4, 0.2)
    orb1.detector()
    # orb1.show_corner_points(image_data1)

    image_data2 = read_image('house2.jpg', '')
    gray_image_data2 = cv2.cvtColor(image_data2, cv2.COLOR_BGR2GRAY)
    orb2 = ORBFeature(gray_image_data2, 12, 4, 0.2)
    orb2.detector()
    # orb2.show_corner_points(image_data2)

    show_match(orb1, orb2, image_data1, image_data2)


