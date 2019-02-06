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
        o_color = __color_interpolation(l_color0, l_color1, i, n_iterate)
        o_x = int(l_x0+xi)
        o_y = int(l_y0+yi)
        o_point_list.append([o_x, o_y, o_color])
        xi += delta_x/n_iterate
        yi += delta_y/n_iterate
        if abs(xi)>abs(delta_x):
            assert False
        if abs(yi)>abs(delta_y):
            assert False

    return o_point_list


def make_int_triangle(p_point1, p_point2, p_point3):
    l_x1 = p_point1[0]
    l_y1 = p_point1[1]
    l_color1 = p_point1[2]
    l_x2 = p_point2[0]
    l_y2 = p_point2[1]
    l_color2 = p_point2[2]
    l_x3 = p_point3[0]
    l_y3 = p_point3[1]
    l_color3 = p_point3[2]
    o_point_list = []
    l1 = make_int_line(p_point1, p_point2)
    l2 = make_int_line(p_point2, p_point3)
    l3 = make_int_line(p_point3,p_point1)
    o_point_list += l1
    o_point_list += l2
    o_point_list += l3

    l_loop_x0 = min(l_x1, l_x2, l_x3)
    l_loop_x1 = max(l_x1, l_x2, l_x3)
    l_loop_y0 = min(l_y1, l_y2, l_y3)
    l_loop_y1 = max(l_y1, l_y2, l_y3)
    for y0 in range(l_loop_y0, l_loop_y1):
        l_x_list = __find_y(y0, l1, l2, l3)
        if len(l_x_list) == 1:
            continue
        if len(l_x_list) != 2:
            assert False
        for x0 in range(l_loop_x0, l_loop_x1):
            if l_x_list[0] < x0 < l_x_list[1]:
                # Todo: color interpolation
                o_color = l_color1
                o_point_list.append([x0, y0, o_color])

    return o_point_list


# ============================================================
# private tool
# ============================================================
def __find_y(p_y, p_l1, p_l2, p_l3):
    o_x_list = []
    for point in p_l1+p_l2+p_l3:
        if point[1] == p_y:
            o_x_list.append(point[0])
    o_x_list.sort()
    return o_x_list


def __color_interpolation(p_color_ori, p_color_fin, i, max_i):
    fraction = float(i)/float(max_i)
    l_r = (p_color_fin[0] - p_color_ori[0]) * fraction + p_color_ori[0]
    l_g = (p_color_fin[1] - p_color_ori[1]) * fraction + p_color_ori[1]
    l_b = (p_color_fin[2] - p_color_ori[2]) * fraction + p_color_ori[2]
    o_interpolated_color = [l_r, l_g, l_b, 1.0]
    return o_interpolated_color

