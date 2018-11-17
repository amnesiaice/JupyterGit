import matplotlib.image as mpimg

# parameter used in this project
light_direct = (1, -1, 1)
radius = 100
item_color = (0.8, 0.8, 0.8, 1)
back_ground_color = (0.7, 0.3, 0.3, 1)

# 600x600 pix target
small_target = mpimg.imread('Resource/testImage.png')
# texture 1
texture_mario = mpimg.imread('Resource/testTexture.png')


def load_render_target(size):
    if size == 'small':
        return small_target
    else:
        print('not suitable size')

