# module used for drawing
# can be modified to use other drawing API
import matplotlib.pyplot as plt


def draw_canvas(img):
    plt.axis('off')
    plt.imshow(img)
    plt.show()
