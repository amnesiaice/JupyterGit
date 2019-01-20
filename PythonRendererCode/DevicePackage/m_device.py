from enum import Enum
from m_canvas import Canvas
import PythonRendererCode.BasicPackage.m_debug_info as dbg
from PythonRendererCode.BasicPackage.m_point import Color
import m_draw_API
import m_tool_set


class Device:
    class DrawMode(Enum):
        POINT = 1
        LINE = 2
        STANDARD = 3

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
            assert True

    def set_draw_mode(self, p_draw_mode):
        if p_draw_mode == "point":
            self.current_draw_mode = self.DrawMode.POINT
        elif p_draw_mode == "line":
            self.current_draw_mode = self.DrawMode.LINE
        elif p_draw_mode == "standard":
            self.current_draw_mode = self.DrawMode.STANDARD
        else:
            self.current_draw_mode = p_draw_mode

    def get_draw_mode(self):
        return self.current_draw_mode

    def show(self):
        m_draw_API.draw(self.device_canvas.target)

    def __set_buffer_point(self):
        l_point2_buffer = m_tool_set.transform_canvas_point_buffer(self.vertex_buffer)
        for i in range(len(l_point2_buffer)):
            l_screen_position = l_point2_buffer[i]
            l_screen_x = l_screen_position[0]
            l_screen_y = l_screen_position[1]
            l_screen_color = l_screen_position[2]
            self.device_canvas.set_point(l_screen_x, l_screen_y, l_screen_color)

    def __set_buffer_line(self):
        l_point2_buffer = m_tool_set.transform_canvas_point_buffer(self.vertex_buffer)
        l_start_point = l_point2_buffer[0]
        for i in range(1, len(l_point2_buffer)):
            l_end_point = l_point2_buffer[i]
            l_line_buffer = m_tool_set.make_int_line(l_start_point, l_end_point)
            self.device_canvas.set_point_buffer(l_line_buffer)
            l_start_point = l_end_point
