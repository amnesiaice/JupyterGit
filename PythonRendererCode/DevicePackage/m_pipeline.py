# this module is used to convert point from vertex buffer to the canvas pixel


class Pipeline:
    def __init__(self):
        self.point2_buffer = []
        self.out_buffer = []

    def transform_vertex_buffer(self, p_vertex_buffer):
        # Todo:Coordinate transformation
        for i_point in p_vertex_buffer:
            l_screen_x = int(i_point.get_x())
            l_screen_y = int(i_point.get_y())
            l_screen_color = i_point.get_color()
            self.point2_buffer.append([l_screen_x, l_screen_y, l_screen_color])
