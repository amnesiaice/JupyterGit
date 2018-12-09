import matplotlib.image as mpimg
import PythonRendererCode.ResourceEntities.canvas as canvas
# parameter used in this project
light_direct = (1, -1, 1)
radius = 100
item_color = (0.8, 0.8, 0.8, 1)
back_ground_color = (0.7, 0.3, 0.3, 1)
is_use_texture = True
cube_pivot_position = (200, 200)


# 600x600 pix target
small_target = mpimg.imread('Resource/testImage.png')
# 1920x1080 pix target
medium_target = mpimg.imread('Resource/1920Blank.png')
# current target
current_target = small_target
# texture 1
texture_mario = mpimg.imread('Resource/testTexture.png')
# canvas
current_canvas = canvas.Canvas()

# cube vetex buffer
cube_vertex_buffer = (
                        (1, 1, 0, 1),  # v0
                        (1, 1, 1, 1),  # v1
                        (1, -1, 0, 1),  # v2
                        (1, -1, 1, 1),  # v3
                        (-1, 1, 0, 1),  # v4
                        (-1, 1, 1, 1),  # v5
                        (-1, -1, 0, 1),  # v6
                        (-1, -1, 1, 1),  # v7
                      )


def load_render_target(size):
    global current_target
    if size == 'small':
        current_target = small_target
        return small_target
    elif size == 'medium':
        current_target = medium_target
        return medium_target
    else:
        print('not suitable size')

