import matplotlib.pyplot as plt
import numpy as np

def draw(ax: plt.Axes):
    circle_rad = [0.5, 0.3]
    circle_y_coords = [1.3, 2.1]
    theta = np.linspace(0, 2 * np.pi, 100)

    bottom_circle = [0.8 * np.cos(theta), 0.8 * np.sin(theta) + 0.2]
    ax.fill(bottom_circle[0], bottom_circle[1] * 0.8, color='lightblue', edgecolor='black')  # Заливка

    for i in range(2):
        x = circle_rad[i] * np.cos(theta)
        y = circle_rad[i] * np.sin(theta) + circle_y_coords[i]
        ax.fill(x, y, color='lightblue', edgecolor='black')

    hat_width = 0.6
    hat_height = 0.3
    hat_x = [-hat_width / 2, hat_width / 2, hat_width / 2, -hat_width / 2, -hat_width / 2]
    hat_y = [circle_y_coords[1] + circle_rad[1], circle_y_coords[1] + circle_rad[1],
             circle_y_coords[1] + circle_rad[1] + hat_height,
             circle_y_coords[1] + circle_rad[1] + hat_height,
             circle_y_coords[1] + circle_rad[1]]
    ax.fill(hat_x, hat_y, color='#826c34', edgecolor='black')

def main():
    _, ax = plt.subplots(figsize=(6, 8))
    ax.set_axis_off()
    draw(ax)
    ax.set_aspect('equal')
    plt.show()

if __name__ == '__main__':
    main()