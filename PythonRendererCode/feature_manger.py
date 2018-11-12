import matplotlib.pyplot as plt

import PythonRendererCode.graphic_manager as graphic_manager
import PythonRendererCode.resource_manager as resource_manager


# first feature to transplantation from the demo, without the texture
def display_sphere():
    l_graph_buffer = resource_manager.load_render_target('small')
    __display(l_graph_buffer)


# private method for feature_manager module
# display the graph buffer
def __display(img):
    plt.axis('off')
    plt.imshow(img)
    plt.show()


# map coord since the graphic_manager is coord independent method
def __map_coord(p_graph_buffer, p_origin):
    i = 0