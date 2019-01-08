# =================
# user interface list:
# create_empty_canvas()
# =================
from PythonRendererCode.DevicePackage.m_device import Device


def create_empty_canvas(p_width, p_height, p_background_color):
    print("create empty %sx%s canvas with %s color" % (p_width, p_height, p_background_color))
    l_device = Device()
    l_device.init_device(p_width, p_height, p_background_color)
    l_device.show()


def draw_triangle_point_mode(p_width, p_height, p_background_color,
                             p_point1, p_point2, p_point3):
    print("draw triangle in point mode at %s %s %s" % (p_point1, p_point2, p_point3))
    l_device = Device()
    l_device.init_device(p_width, p_height, p_background_color)
    l_device.append_vertex_buffer(p_point1)
    l_device.append_vertex_buffer(p_point2)
    l_device.append_vertex_buffer(p_point3)

    l_device.set_draw_mode(l_device.DrawMode.POINT)
    l_device.set_vertex_buffer()
    l_device.show()


def draw_triangle_line_mode(p_width, p_height, p_background_color,
                            p_point1, p_point2, p_point3):
    print("draw triangle in line mode at %s %s %s" % (p_point1, p_point2, p_point3))
    l_device = Device()
    l_device.init_device(p_width, p_height, p_background_color)
    l_device.append_vertex_buffer(p_point1)
    l_device.append_vertex_buffer(p_point2)
    l_device.append_vertex_buffer(p_point3)

    l_device.set_draw_mode(l_device.DrawMode.LINE)
    l_device.set_vertex_buffer()
    l_device.show()
