# module used for drawing
# can be modified to use other drawing API
import matplotlib.pyplot as plt
import PythonRendererCode.BasicPackage.m_debug_info as dbg


def draw(img):
    class PlotIndex(object):
        plot_index = 1
    dbg.debug_img(img)
    plt.axis('off')
    plt.figure(PlotIndex.plot_index)
    plt.imshow(img)
    plt.show()
    PlotIndex.plot_index += 1
