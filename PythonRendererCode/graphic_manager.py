import numpy as np

import PythonRendererCode.resource_manager as resource_manager

# local const
l_pi = np.pi

def make_cube(p_img,p_vertex_buffer,pivot_position):
    p_vertex_buffer[0]

def make_sphere(p_img, p_radius):
    l_height = len(p_img)
    l_width = len(p_img[0])
    l_center_x = int(l_width/2)
    l_center_y = int(l_height/2)
    if resource_manager.is_use_texture :
        l_current_texture = resource_manager.texture_mario
    else:
        l_item_color = resource_manager.item_color
    l_radius = resource_manager.radius
    l_light_direct = resource_manager.light_direct
    l_back_ground_color = resource_manager.back_ground_color
    l_texture_start_x = 270
    l_texture_start_y = 280
    l_texture_length = 800
    for j in range(0, l_width-1):
        for i in range(0, l_height-1):
            if np.square(j-l_center_x)+np.square(i-l_center_y) < np.square(p_radius):
                # draw the sphere
                if resource_manager.is_use_texture:
                    l_item_color = __read_sphere_texture(l_current_texture, l_texture_start_x, l_texture_start_y,
                                                         l_texture_length, l_radius, j-l_center_x, i-l_center_y)
                l_item_light = __sphere_norm_light(j-l_center_x, i-l_center_y, l_radius, l_light_direct)
                p_img[i][j] = np.multiply(l_item_color, l_item_light)
                p_img[i][j][3] = 1
            else:
                # draw background color
                p_img[i][j] = l_back_ground_color
    return p_img


# calculate the light information
def __sphere_norm_light(p_x, p_y, p_radius, p_light):
    l_norm = (p_x, p_y, np.sqrt(np.square(p_radius)-np.square(p_x)-np.square(p_y)))
    out = np.dot(p_light, l_norm)/__vector_length(p_light)/__vector_length(l_norm)*0.5+0.5
    return out


def __vector_length(p_vector):
    return np.sqrt(np.dot(p_vector, p_vector))


# map the sphere texture, p_x and p_y is the coord related to the center of circle
def __read_sphere_texture(p_texture, p_start_x, p_start_y, p_texture_length, p_radius, p_x, p_y):
    # coord related to the center of the texture
    p_x = float(p_x)
    p_y = float(p_y)
    if p_x == 0.0:
        l_tex_x = 0
    else:
        # l_tex_x=arccos(x/r)*r/r*texture_length/2
        l_tex_x = (np.pi/2-np.arccos(abs(p_x) / p_radius)) / np.pi * 2 * p_texture_length / 2 * p_x / abs(p_x)

    if p_y == 0.0:
        l_tex_y = 0
    else:
        l_tex_y = (np.pi/2-np.arccos(abs(p_y) / p_radius)) / np.pi * 2 * p_texture_length / 2 * p_y / abs(p_y)

    l_mapped_x = p_start_x+l_tex_x+p_texture_length/2
    l_mapped_y = p_start_y+l_tex_y+p_texture_length/2
    l_mapped_x = int(l_mapped_x)
    l_mapped_y = int(l_mapped_y)
    out = p_texture[l_mapped_y][l_mapped_x]

    # in case some texture file has no alpha value
    if len(out) == 3:
        out = np.append(out, 1)
    return out
