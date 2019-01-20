import PythonRendererCode.user_interface as ui
from PythonRendererCode.BasicPackage import m_color
from PythonRendererCode.BasicPackage import m_point
import PythonRendererCode.BasicPackage.m_debug_info as dbg
# g_max_test_list = [0, 1, 2, 3]
g_max_test_list = [2]


def test_case(p_case):
    dbg.debug_print(dbg.LogLevel.INFO, '# test_case:%d' % p_case)
    if p_case == 0:
        # print test case info
        dbg.debug_print(dbg.LogLevel.INFO, "Test: initialize empty canvas")

        l_background_color = m_color.Color.get_default_color("light blue")
        ui.create_empty_canvas(800, 600, l_background_color)
    if p_case == 1:
        # print test case info
        dbg.debug_print(dbg.LogLevel.INFO, "Test: draw triangle in point mode")

        l_background_color = m_color.Color.get_default_color("white")
        point1 = m_point.Point(200, 400, 0)
        point2 = m_point.Point(400, 400, 0)
        point3 = m_point.Point(200, 100, 0)
        ui.draw_triangle_point_mode(800, 600, l_background_color,
                                    point1, point2, point3)
    if p_case == 2:
        # print test case info
        dbg.debug_print(dbg.LogLevel.INFO, "Test: draw triangle in line mode")

        l_background_color = m_color.Color.get_default_color("white")
        point1 = m_point.Point(200, 400, 0, m_color.Color.get_default_color("light blue"))
        point2 = m_point.Point(400, 400, 0, m_color.Color.get_default_color("red"))
        point3 = m_point.Point(200, 100, 0, m_color.Color.get_default_color("green"))
        point4 = m_point.Point(200, 400, 0, m_color.Color.get_default_color("light blue"))
        ui.draw_triangle_line_mode(800, 600, l_background_color,
                                   point1, point2, point3, point4)
    if p_case == 3:
        # print test case info
        dbg.debug_print(dbg.LogLevel.INFO, "Test: draw triangle in standard mode")


for i in g_max_test_list:
    test_case(i)
