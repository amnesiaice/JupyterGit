from PythonRendererCode.BasicPackage.m_color import Color


def transform_canvas_point_buffer(p_point_buffer):
    # Todo:Coordinate transformation
    o_point2_buffer = []
    for i_point in p_point_buffer:
        l_screen_x = int(i_point.get_x())
        l_screen_y = int(i_point.get_y())
        l_screen_color = i_point.get_color()
        o_point2_buffer.append([l_screen_x, l_screen_y, l_screen_color])
    return o_point2_buffer


def make_int_line(p_point_start, p_point_end):
    l_x0 = p_point_start[0]
    l_y0 = p_point_start[1]
    l_color0 = p_point_start[2]
    l_x1 = p_point_end[0]
    l_y1 = p_point_end[1]
    l_color1 = p_point_end[2]

    o_point_list = []
    delta_x = float(l_x1-l_x0)
    delta_y = float(l_y1-l_y0)
    n_iterate = max(abs(delta_x), abs(delta_y))
    xi = 0.0
    yi = 0.0
    for i in range(int(n_iterate)):
        o_color = Color.color_interpolation(l_color0, l_color1, i, n_iterate)
        o_x = int(l_x0+xi)
        o_y = int(l_y0+yi)
        o_point_list.append([o_x, o_y, o_color])
        xi += delta_x/n_iterate
        yi += delta_y/n_iterate
        if abs(xi)>abs(delta_x):
            assert True
        if abs(yi)>abs(delta_y):
            assert True

    return o_point_list
