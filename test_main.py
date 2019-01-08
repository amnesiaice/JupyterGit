import PythonRendererCode.user_interface as ui
from PythonRendererCode.BasicPackage import *
# g_max_test_list = [0, 1, 2]
g_max_test_list = [2]


def test_case(p_case):
    if p_case == 0:
        print_test_info(p_case)
        l_background_color = m_color.Color.get_default_color("light blue")
        ui.create_empty_canvas(800, 600, l_background_color)
    if p_case == 1:
        print_test_info(p_case)
        l_background_color = m_color.Color.get_default_color("white")
        point1 = m_point.Point(200, 400, 0)
        point2 = m_point.Point(400, 400, 0)
        point3 = m_point.Point(200, 100, 0)
        ui.draw_triangle_point_mode(800, 600, l_background_color,
                                    point1, point2, point3)
    if p_case == 2:
        print_test_info(p_case)
        l_background_color = m_color.Color.get_default_color("light blue")
        point1 = m_point.Point(200, 400, 0)
        point2 = m_point.Point(400, 400, 0)
        point3 = m_point.Point(200, 100, 0)
        ui.draw_triangle_line_mode(800, 600, l_background_color,
                                   point1, point2, point3)


def print_test_info(p_case):
    print('test_case:%d' % p_case)
    if p_case == 0:
        print("Test: initialize empty canvas with")
    if p_case == 1:
        print("Test: draw triangle in point mode")
    if p_case == 2:
        print("Test: draw triangle in line mode")


for i in g_max_test_list:
    test_case(i)
