# module used for drawing
# can be modified to use other drawing API
import matplotlib.pyplot as plt


def draw(img):
    class PlotIndex(object):
        plot_index = 1
    plt.axis('off')
    plt.figure(PlotIndex.plot_index)
    plt.imshow(img)
    plt.show()
    PlotIndex.plot_index += 1
