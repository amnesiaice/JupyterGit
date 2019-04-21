from PythonRendererCode.BasicPackage import *


class Canvas:
    def __init__(self):
        self.width = 800.0
        self.height = 600.0
        self.back_ground_color_vector = m_color.Color.get_default_color()
        self.target = [[[]]]

    def init_canvas(self, p_width, p_height, p_color=m_color.Color.get_default_color()):
        # =================
        # prepare parameter
        # =================
        p_width = int(p_width)
        p_height = int(p_height)
        p_color = [float(i) for i in p_color]
        # =================
        # init canvas and related attribute
        # =================
        self.width = p_width
        self.height = p_height
        self.back_ground_color_vector = p_color
        # use this way to init 2-dim list to avoid shallow copy
        self.target = [[self.back_ground_color_vector for i in range(p_width)] for j in range(p_height)]

    def set_point(self, p_x, p_y, p_color):
        if p_x >= len(self.target[0]) or p_x<0 or p_y >= len(self.target) or p_y < 0:
            return
        self.target[p_y][p_x] = p_color

    def set_point_buffer(self, p_point2_buffer):
        for i_point2 in p_point2_buffer:
            self.set_point(i_point2[0], i_point2[1], i_point2[2])

    @staticmethod
    def make_int_line(p_point_start, p_point_end):
        l_x0 = p_point_start[0]
        l_y0 = p_point_start[1]
        l_color0 = p_point_start[2]
        l_x1 = p_point_end[0]
        l_y1 = p_point_end[1]
        l_color1 = p_point_end[2]

        o_point_list = []
        delta_x = float(l_x1 - l_x0)
        delta_y = float(l_y1 - l_y0)
        n_iterate = max(abs(delta_x), abs(delta_y))
        xi = 0.0
        yi = 0.0
        for i in range(int(n_iterate)):
            o_color = Canvas.__color_interpolation(l_color0, l_color1, i, n_iterate)
            o_x = int(l_x0 + xi)
            o_y = int(l_y0 + yi)
            o_point_list.append([o_x, o_y, o_color])
            xi += delta_x / n_iterate
            yi += delta_y / n_iterate
            assert abs(xi) - abs(delta_x) < 1e-8
            assert abs(yi) - abs(delta_y) < 1e-8
        return o_point_list

    @staticmethod
    def make_int_triangle(p_point1, p_point2, p_point3):
        l_x1 = p_point1[0]
        l_y1 = p_point1[1]
        l_x2 = p_point2[0]
        l_y2 = p_point2[1]
        l_x3 = p_point3[0]
        l_y3 = p_point3[1]
        o_point_list = []
        l1 = Canvas.make_int_line(p_point1, p_point2)
        l2 = Canvas.make_int_line(p_point2, p_point3)
        l3 = Canvas.make_int_line(p_point3, p_point1)
        o_point_list += l1
        o_point_list += l2
        o_point_list += l3

        l_loop_x0 = min(l_x1, l_x2, l_x3)
        l_loop_x1 = max(l_x1, l_x2, l_x3)
        l_loop_y0 = min(l_y1, l_y2, l_y3)
        l_loop_y1 = max(l_y1, l_y2, l_y3)
        for y0 in range(l_loop_y0, l_loop_y1):
            l_x_list = Canvas.__find_y(y0, l1, l2, l3)
            if len(l_x_list) == 1:
                continue
            assert len(l_x_list) == 2
            for x0 in range(l_loop_x0, l_loop_x1):
                if l_x_list[0] < x0 < l_x_list[1]:
                    o_color = Canvas.__triangle_color_interpolation(x0, y0, p_point1, p_point2, p_point3)
                    o_point_list.append([x0, y0, o_color])

        return o_point_list

    # ============================================================
    # private tool
    # ============================================================
    @staticmethod
    def __find_y(p_y, p_l1, p_l2, p_l3):
        o_x_list = []
        for point in p_l1 + p_l2 + p_l3:
            if point[1] == p_y:
                o_x_list.append(point[0])
        o_x_list.sort()
        if len(o_x_list) > 2:
            return [o_x_list[0], o_x_list[-1]]
        else:
            return o_x_list

    @staticmethod
    def __color_interpolation(p_color_ori, p_color_fin, i, max_i):
        fraction = float(i) / float(max_i)
        l_r = (p_color_fin[0] - p_color_ori[0]) * fraction + p_color_ori[0]
        l_g = (p_color_fin[1] - p_color_ori[1]) * fraction + p_color_ori[1]
        l_b = (p_color_fin[2] - p_color_ori[2]) * fraction + p_color_ori[2]
        o_interpolated_color = [l_r, l_g, l_b, 1.0]
        return o_interpolated_color

    @staticmethod
    def __triangle_color_interpolation(p_x, p_y, p_point1, p_point2, p_point3):
        # calculate barycentric coordinate
        p1x = p_point1[0]
        p1y = p_point1[1]
        p2x = p_point2[0]
        p2y = p_point2[1]
        p3x = p_point3[0]
        p3y = p_point3[1]
        l_area = Canvas.__triangle_area(p1x, p1y, p2x, p2y, p3x, p3y)
        u = Canvas.__triangle_area(p_x, p_y, p2x, p2y, p3x, p3y)/l_area
        v = Canvas.__triangle_area(p1x, p1y, p_x, p_y, p3x, p3y)/l_area
        w = Canvas.__triangle_area(p1x, p1y, p2x, p2y, p_x, p_y)/l_area
        assert u >= 0 and v >= 0 and w >= 0 #and abs(u+v+w-1) < 0.1

        # use barycentric coordinate interpolate the color
        p1c = p_point1[2]
        p2c = p_point2[2]
        p3c = p_point3[2]
        o_interpolated_color = [0.0, 0.0, 0.0, 1.0]
        for i in range(3):
            o_interpolated_color[i] = u*p1c[i]+v*p2c[i]+w*p3c[i]
        return o_interpolated_color

    @staticmethod
    def __triangle_area(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y,):
        o_area = 0.5*(p1_x*(p2_y-p3_y)+p2_x*(p3_y-p1_y)+p3_x*(p1_y-p2_y))
        return abs(o_area)
