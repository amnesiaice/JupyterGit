import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open('PythonRendererCode/pyrender_config.ini'))

# debug
g_debug_enable_config = config.getboolean('debug', 'g_debug_enable')

# main window
width_config = config.getint('main', 'width')
height_config = config.getint('main', 'height')

# viewport
viewport_width_config = config.getfloat('viewport', 'viewport_width')
viewport_height_config = config.getfloat('viewport', 'viewport_height')
viewport_min_depth_config = config.getfloat('viewport', 'viewport_min_depth')
viewport_max_depth_config = config.getfloat('viewport', 'viewport_max_depth')
viewport_top_left_x = config.getfloat('viewport', 'viewport_top_left_x')
viewport_top_left_y = config.getfloat('viewport', 'viewport_top_left_y')
