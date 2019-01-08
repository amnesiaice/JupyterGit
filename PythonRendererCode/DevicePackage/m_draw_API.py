# module used for drawing
# can be modified to use other drawing API
import matplotlib.pyplot as plt


def draw(img):
    class PlotIndex(object):
        plot_index = 1
    debug_canvas(img)
    plt.axis('off')
    plt.figure(PlotIndex.plot_index)
    plt.imshow(img)
    plt.show()
    PlotIndex.plot_index += 1


def debug_canvas(img):
    for j in range(len(img)):
        for i in range(len(img[0])):
            if img[j][i] == [0.0, 0.0, 0.0, 1.0]:
                print("color:", img[j][i])
                print("x:%s,y:%s" % (i, j))
