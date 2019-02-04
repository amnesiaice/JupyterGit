# =================
# user interface list:
# create_empty_canvas()
# draw_triangle_point_mode
# draw_triangle_line_mode
# =================
from PythonRendererCode.DevicePackage.m_device import Device
from PythonRendererCode.DevicePackage.m_device import DrawMode
# debug import
from PythonRendererCode.PRDebugPackage.m_pr_debug import LogLevel
from PythonRendererCode.PRDebugPackage.m_pr_debug import DebugConfig


# ============================================================
# test case function
# ============================================================
def create_empty_canvas(p_width, p_height, p_background_color):
    l_device = Device()
    l_device.init_device(p_width, p_height, p_background_color)
    l_debug_config = DebugConfig(
        p_is_debug_enable=True,
        p_current_log_level=LogLevel.ALL,
        p_debug_filter_location="PythonRendererCode/PRDebugPackage/DebugFilter/",
        p_debug_filter_name="create_empty_canvas.txt",
    )
    set_debug_config(l_device, l_debug_config)
    l_device.show()


def draw_triangle_point_mode(p_width, p_height, p_background_color,
                             p_point1, p_point2, p_point3):
    l_device = Device()
    l_device.init_device(p_width, p_height, p_background_color)
    l_device.append_vertex_buffer(p_point1)
    l_device.append_vertex_buffer(p_point2)
    l_device.append_vertex_buffer(p_point3)

    l_device.set_draw_mode(DrawMode.POINT)
    l_device.set_buffer_to_canvas()

    l_debug_config = DebugConfig(
         p_is_debug_enable=True,
         p_current_log_level=LogLevel.ALL,
         p_debug_filter_location="PythonRendererCode/PRDebugPackage/DebugFilter/",
         p_debug_filter_name="draw_triangle_point_mode.txt",
    )
    set_debug_config(l_device, l_debug_config)

    l_device.show()


def draw_triangle_line_mode(p_width, p_height, p_background_color,
                            p_point1, p_point2, p_point3, p_point4):
    l_device = Device()
    l_device.init_device(p_width, p_height, p_background_color)
    l_device.append_vertex_buffer(p_point1)
    l_device.append_vertex_buffer(p_point2)
    l_device.append_vertex_buffer(p_point3)
    l_device.append_vertex_buffer(p_point4)

    l_device.set_draw_mode(DrawMode.LINE)
    l_device.set_buffer_to_canvas()

    # set debug config
    l_debug_config = DebugConfig(
         p_is_debug_enable=True,
         p_current_log_level=LogLevel.ALL,
         p_debug_filter_location="PythonRendererCode/PRDebugPackage/DebugFilter/",
         p_debug_filter_name="draw_triangle_line_mode.txt",
    )
    set_debug_config(l_device, l_debug_config)

    l_device.show()


# ============================================================
# tool function
# ============================================================
def print_test_case_info(*args):
    print("============================================================")
    print("Test Case")
    print("".join(str(i) for i in args))
    print("============================================================")


def set_debug_config(p_device,
                     p_debug_config
                     ):
    l_device = p_device
    l_device.pr_debug.set_debug_config(p_debug_config)
