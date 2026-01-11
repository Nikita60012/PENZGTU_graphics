import cv2
import numpy as np

def draw(img: np.ndarray, width: int, height: int) -> np.ndarray:
    lightblue = (240, 230, 200)
    brown = (30, 70, 90)
    black = (1, 1, 1)

    r_bottom = 180
    r_middle = 110
    r_top = 60

    y_bottom = height - r_bottom
    ellipse_height = int(r_bottom * 0.8)
    y_middle = y_bottom - (ellipse_height + r_middle)
    y_top = y_middle - (r_middle + r_top)

    cv2.ellipse(img, (width // 2, y_bottom), (r_bottom, ellipse_height), 0, 0, 360, black, 3)
    cv2.ellipse(img, (width // 2, y_bottom), (r_bottom, ellipse_height), 0, 0, 360, lightblue, -1)

    cv2.circle(img, (width // 2, y_middle), r_middle, black, 3)
    cv2.circle(img, (width // 2, y_middle), r_middle, lightblue, -1)

    cv2.circle(img, (width // 2, y_top), r_top, black, 3)
    cv2.circle(img, (width // 2, y_top), r_top, lightblue, -1)

    hat_width = r_top * 2
    hat_height = 60
    hat_x1 = width // 2 - hat_width // 2
    hat_y1 = y_top - r_top
    hat_x2 = hat_x1 + hat_width
    hat_y2 = hat_y1 - hat_height

    cv2.rectangle(img, (hat_x1, hat_y1), (hat_x2, hat_y2), black, 3)
    cv2.rectangle(img, (hat_x1, hat_y1), (hat_x2, hat_y2), brown, -1)

    return img

def main():
    width, height = 800, 900
    img = np.full((height, width, 3), 255, dtype=np.uint8)
    snowman = draw(img, width, height)
    cv2.imshow("Snowman", snowman)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()