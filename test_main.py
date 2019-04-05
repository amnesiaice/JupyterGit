import PythonRendererCode.user_interface as ui
from PythonRendererCode.BasicPackage import m_color
from PythonRendererCode.BasicPackage import m_point
g_max_test_list = [0, 1, 2, 3, 4, 5]
# g_max_test_list = [5]


def test_case(p_case):
    if p_case == 0:
        # print test case info
        ui.print_test_case_info("Test 0: initialize empty canvas")

        l_background_color = m_color.Color.get_default_color("light blue")
        ui.create_empty_canvas(800, 600, l_background_color)
    if p_case == 1:
        # print test case info
        ui.print_test_case_info("Test 1: draw triangle in point mode")

        l_background_color = m_color.Color.get_default_color("white")
        point1 = m_point.Point(200, 400, 0)
        point2 = m_point.Point(400, 400, 0)
        point3 = m_point.Point(200, 100, 0)
        ui.draw_triangle_point_mode(l_background_color,
                                    point1, point2, point3)
    if p_case == 2:
        # print test case info
        ui.print_test_case_info("Test 2: draw triangle in line mode")

        l_background_color = m_color.Color.get_default_color("white")
        point1 = m_point.Point(200, 400, 0, m_color.Color.get_default_color("light blue"))
        point2 = m_point.Point(400, 400, 0, m_color.Color.get_default_color("red"))
        point3 = m_point.Point(200, 100, 0, m_color.Color.get_default_color("green"))
        ui.draw_triangle_line_mode(l_background_color,
                                   point1, point2, point3)
    if p_case == 3:
        # print test case info
        ui.print_test_case_info("Test 3: draw triangle in standard mode")
        l_background_color = m_color.Color.get_default_color("white")
        point1 = m_point.Point(200, 400, 0, m_color.Color.get_default_color("light blue"))
        point2 = m_point.Point(400, 400, 0, m_color.Color.get_default_color("red"))
        point3 = m_point.Point(200, 100, 0, m_color.Color.get_default_color("green"))
        ui.draw_triangle_standard_mode(l_background_color,
                                       point1, point2, point3)

    if p_case == 4:
        # print test case info
        ui.print_test_case_info("Test 4: draw point buffer in standard mode")
        l_background_color = m_color.Color.get_default_color("white")
        l_point_buffer = [
            m_point.Point(100, 400, 0, m_color.Color.get_default_color("light blue")),
            m_point.Point(300, 300, 0, m_color.Color.get_default_color("red")),
            m_point.Point(150, 100, 0, m_color.Color.get_default_color("green")),
            m_point.Point(450, 400, 0, m_color.Color.get_default_color("light blue")),
            m_point.Point(600, 100, 0, m_color.Color.get_default_color("light blue")),
            m_point.Point(750, 400, 0, m_color.Color.get_default_color("light blue")),
        ]
        ui.draw_point_buffer_standard_mode(l_background_color, l_point_buffer)

    if p_case == 5:
        # print test case info
        ui.print_test_case_info("Test 5: draw cube in standard mode")


if __name__ == "__main__":
    for i in g_max_test_list:
        test_case(i)
