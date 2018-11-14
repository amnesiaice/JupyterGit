import matplotlib.pyplot as plt

import PythonRendererCode.graphic_manager as graphic_manager
import PythonRendererCode.resource_manager as resource_manager


# first feature to transplantation from the demo, without the texture
def display_sphere():
    l_graph_buffer = resource_manager.load_render_target('small')
    l_origin_sphere = graphic_manager.make_sphere(l_graph_buffer, resource_manager.radius)

    __display(l_origin_sphere)


# private method for feature_manager module
# display the graph buffer
def __display(p_img):
    plt.axis('off')
    plt.imshow(p_img)
    plt.show()

