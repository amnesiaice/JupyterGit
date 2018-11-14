import numpy as np

import PythonRendererCode.resource_manager as resource_manager

# local const
l_pi = np.pi


def make_sphere(p_img,p_radius):
    l_height = len(p_img)
    l_width = len(p_img[0])
    l_center_x = int(l_width/2)
    l_center_y = int(l_height/2)
    for j in range(0, l_width-1):
        for i in range(0, l_height-1):
            if np.square(j-l_center_x)+np.square(i-l_center_y) < np.square(p_radius):
                p_img[i][j] = resource_manager.item_color
            else:
                p_img[i][j] = resource_manager.back_ground_color
    return p_img

