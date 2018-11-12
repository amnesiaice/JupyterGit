import matplotlib.image as mpimg

# parameter used in this project
light_direct = (1, 1, 1)

# 600x600 pix target
small_target = mpimg.imread('Resource/testImage.png')
# texture 1
texture_mario = mpimg.imread('Resource/testTexture.png')


def load_render_target(size):
    if size == 'small':
        return small_target
    else:
        print('not suitable size')

