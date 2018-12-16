import PythonRendererCode.ResourceEntities.draw_API as drawAPI
from PythonRendererCode.GraphEntities.Point import Point
from DrawMode import DrawMode
"""
Canvas class used for resource_manager
"""


class Canvas:
    def __init__(self):
        self.ratio = 1.0
        self.width = 600.0
        self.height = 600.0
        self.target = [[[]]]
        self.final_target = [[[]]]
        self.default_draw_mode = DrawMode.standard

    # set a p_width p_height original color picture
    def init_canvas(self, p_width, p_height, p_color):
        # =================
        # prepare parameter
        # =================
        p_color = self.__get_color(p_color)
        p_width = int(p_width)
        p_height = int(p_height)

        # =================
        # init canvas and related attribute
        # =================
        self.width = p_width
        self.height = p_height
        self.ratio = p_width / p_height
        # use this way to init 2-dim list to avoid shallow copy
        self.target = [[p_color]*p_width for i in range(p_height)]

        # =================
        # init final_target z_buffer and others
        # =================
        self.final_target = [[p_color]*p_width for i in range(p_height)]

    def set_entity(self, p_entity, p_pivot_point, p_draw_mode):
        # =================
        # prepare the point
        # =================
        l_screen_point_buffer = self.__projection_to_screen(p_entity,p_pivot_point)
        if p_draw_mode == DrawMode.point:
            for i in range(0, p_entity.num_point):
                l_screen_x = int(l_screen_point_buffer[i].get_position_x())
                l_screen_y = int(l_screen_point_buffer[i].get_position_y())
                l_screen_color = l_screen_point_buffer[i].get_color()
                # for the target the second bracket is the x position
                self.target[l_screen_y][l_screen_x] = l_screen_color

    def draw_canvas(self):
        self.__convert_axis()
        drawAPI.draw_canvas(self.final_target)

    # converting y axis to use the 
    def __convert_axis(self):
        for j in range(0, self.height):
            for i in range(0, self.width):
                self.final_target[-j][i] = self.target[j][i]

    @staticmethod
    def __projection_to_screen(p_entity, p_pivot_position):
        o_point_buffer = []
        for i_point in p_entity.point_buffer:
            o_point = Point()
            l_x = int(i_point.get_position_x()+p_pivot_position[0])
            l_y = int(i_point.get_position_y()+p_pivot_position[1])
            # hard code the screen position to the integer to make it fit the target data structure
            o_point.set_position([l_x, l_y, 0])
            o_point.set_color(i_point.get_color())
            o_point_buffer.append(o_point)
        return o_point_buffer

    @staticmethod
    def __get_color(p_color):
        if p_color == 'red':
            return [0.9, 0.0, 0.0, 1.0]
        elif p_color == 'green':
            return [0.0, 0.9, 0.0, 1.0]
        elif p_color == 'blue':
            return [0.0, 0.0, 0.9, 1.0]
        elif p_color == 'light blue':
            return [0.28, 0.72, 0.98, 1]
        elif p_color == 'white':
            return [1.0, 1.0, 1.0, 1.0]
        elif p_color == 'black':
            return [0.0, 0.0, 0.0, 1.0]
        else:
            # enable the int 0 to display as black
            # as python will regard the int 0 as null
            p_color[0] = float(p_color[0])
            p_color[1] = float(p_color[1])
            p_color[2] = float(p_color[2])
            return p_color

