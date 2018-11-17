import numpy as np

import PythonRendererCode.resource_manager as resource_manager

# local const
l_pi = np.pi


def make_sphere(p_img, p_radius):
    l_height = len(p_img)
    l_width = len(p_img[0])
    l_center_x = int(l_width/2)
    l_center_y = int(l_height/2)
    l_item_color = resource_manager.item_color
    l_radius = resource_manager.radius
    l_light_direct = resource_manager.light_direct
    l_back_ground_color = resource_manager.back_ground_color
    for j in range(0, l_width-1):
        for i in range(0, l_height-1):
            if np.square(j-l_center_x)+np.square(i-l_center_y) < np.square(p_radius):
                l_item_light = __sphere_norm_light(j-l_center_x, i-l_center_y, l_radius, l_light_direct)
                p_img[i][j] = np.multiply(l_item_color, l_item_light)
                p_img[i][j][3] = 1
            else:
                p_img[i][j] = l_back_ground_color
    return p_img


def __sphere_norm_light(p_x, p_y, p_radius, p_light):
    l_norm = (p_x, p_y, np.sqrt(np.square(p_radius)-np.square(p_x)-np.square(p_y)))
    out = np.dot(p_light, l_norm)/__vector_length(p_light)/__vector_length(l_norm)*0.5+0.5
    return out


def __vector_length(p_vector):
    return np.sqrt(np.dot(p_vector, p_vector))