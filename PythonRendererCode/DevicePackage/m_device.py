from enum import Enum
from m_canvas import Canvas
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

    def set_vertex_buffer(self):
        if self.current_draw_mode == self.DrawMode.POINT:
            print("draw in point mode")
            for i_point in self.vertex_buffer:
                # Coordinate transformation
                l_screen_x = int(i_point.get_x())
                l_screen_y = int(i_point.get_y())
                self.device_canvas.set_point(l_screen_x, l_screen_y, i_point.get_color())
        else:
            print("draw mode not supported yet")

    def set_draw_mode(self, p_draw_mode):
        self.current_draw_mode = p_draw_mode

    def get_draw_mode(self):
        return self.current_draw_mode

    def show(self):
        m_draw_API.draw(self.device_canvas.target)
