import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open('PythonRendererCode/pyrender_config.ini'))

g_debug_enable_config = config.getboolean('debug', 'g_debug_enable')

width_config = config.getint('main', 'width')
height_config = config.getint('main', 'height')
