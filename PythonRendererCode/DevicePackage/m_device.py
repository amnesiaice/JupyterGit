from enum import Enum
from m_canvas import Canvas
import PythonRendererCode.BasicPackage.m_debug_info as dbg
from PythonRendererCode.BasicPackage.m_point import Color
import m_draw_API


class Device:
    class DrawMode(Enum):
        POINT = 1
        LINE = 2
        STRIP = 3

    def __init__(self):
        self.device_canvas = Canvas()
        self.vertex_buffer = []
        self.current_draw_mode = self.DrawMode.POINT

    def init_device(self,
                    # parameter used for canvas
                    p_canvas_width, p_canvas_height,  p_canvas_color):
        # initialize canvas
        self.device_canvas.init_canvas(p_width=p_canvas_width,
                                       p_height=p_canvas_height,
                                       p_color=p_canvas_color)

    def append_vertex_buffer(self, p_point):
        self.vertex_buffer.append(p_point)

    def set_buffer_to_canvas(self):
        if self.current_draw_mode == self.DrawMode.POINT:
            self.__set_buffer_point()
        elif self.current_draw_mode == self.DrawMode.LINE:
            self.__set_buffer_line()
        else:
            dbg.debug_print(dbg.LogLevel.ERROR, "draw mode not supported yet")

    def set_draw_mode(self, p_draw_mode):
        self.current_draw_mode = p_draw_mode

    def get_draw_mode(self):
        return self.current_draw_mode

    def show(self):
        m_draw_API.draw(self.device_canvas.target)

    def __set_buffer_point(self):
        dbg.debug_print(dbg.LogLevel.INFO, "draw in point mode")
        for i_point in self.vertex_buffer:
            l_screen_position = self.__transform_canvas_point(i_point)
            l_screen_x = l_screen_position[0]
            l_screen_y = l_screen_position[1]
            self.device_canvas.set_point(l_screen_x, l_screen_y, i_point.get_color())

    def __set_buffer_line(self):
        self.__set_buffer_point()
        dbg.debug_print(dbg.LogLevel.INFO, "draw in line mode")
        l_last_position = self.__transform_canvas_point(self.vertex_buffer[0])
        if len(self.vertex_buffer) == 1:
            dbg.debug_print(dbg.LogLevel.ERROR, "cannot draw line with one point")
            return
        for i in range(1, len(self.vertex_buffer)):
            i_point = self.vertex_buffer[i]
            l_current_position = self.__transform_canvas_point(i_point)
            if l_current_position[0] == l_last_position[0]:
                for line_y in range(l_last_position[1]+1, l_current_position[1]):
                    l_screen_x = l_last_position[0]
                    l_screen_y = line_y
                    self.device_canvas.set_point(l_screen_x, l_screen_y, i_point.get_color())
            elif l_current_position[0] > l_last_position[0]:
                l_k = float((l_current_position[1]-l_last_position[1]))/float((l_current_position[0]-l_last_position[0]))
                for line_x in range(l_last_position[0]+1, l_current_position[0]):
                    l_screen_x = line_x
                    l_screen_y = int(l_k*(line_x-l_last_position[0])+l_last_position[1])
                    self.device_canvas.set_point(l_screen_x, l_screen_y, i_point.get_color())
            elif l_current_position[0] < l_last_position[0]:
                l_k = float((l_current_position[1]-l_last_position[1]))/float((l_current_position[0]-l_last_position[0]))
                for line_x in range(l_last_position[0]-1, l_current_position[0], -1):
                    l_screen_x = line_x
                    l_screen_y = int(l_k*(line_x-l_last_position[0])+l_last_position[1])
                    self.device_canvas.set_point(l_screen_x, l_screen_y, i_point.get_color())
            l_last_position = l_current_position

    @staticmethod
    def __transform_canvas_point(point):
        # Todo:Coordinate transformation
        l_screen_x = int(point.get_x())
        l_screen_y = int(point.get_y())
        return [l_screen_x, l_screen_y]
