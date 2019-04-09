from enum import Enum
from m_canvas import Canvas
from PythonRendererCode.DevicePackage.m_pipe import Pipe
from PythonRendererCode.PRDebugPackage.m_pr_debug import PRDebug
from PythonRendererCode.PRDebugPackage.m_pr_debug import LogLevel
from PythonRendererCode import config_warehouse
import m_draw_API


class DrawMode(Enum):
    NONE = 0
    POINT = 1
    LINE = 2
    STANDARD = 3


class Device:
    def __init__(self):
        self.device_canvas = Canvas()
        self.device_pipe = Pipe()
        self.vertex_buffer = []
        self.current_draw_mode = DrawMode.POINT

        # init debug object
        self.pr_debug = PRDebug()

        # read from config
        l_canvas_size = self.__read_window_size_config()
        self.default_width = l_canvas_size['width']
        self.default_height = l_canvas_size['height']

    def init_device(self,
                    # parameter used for canvas
                    p_canvas_color,
                    p_canvas_width=None,
                    p_canvas_height=None
                    ):
        if p_canvas_width is None:
            p_canvas_width = self.default_width
            p_canvas_height = self.default_height
        # initialize canvas
        self.device_canvas.init_canvas(p_width=p_canvas_width,
                                       p_height=p_canvas_height,
                                       p_color=p_canvas_color)

    # ============================================================
    # draw config
    # ============================================================
    def append_vertex_buffer(self, p_point):
        self.vertex_buffer.append(p_point)

    def set_buffer_to_canvas(self):
        if self.current_draw_mode == DrawMode.NONE:
            self.pr_debug.debug_print(LogLevel.ERROR, "draw mode not set yet")
            assert False
        elif self.current_draw_mode == DrawMode.POINT:
            self.__set_buffer_point()
        elif self.current_draw_mode == DrawMode.LINE:
            self.__set_buffer_line()
        elif self.current_draw_mode == DrawMode.STANDARD:
            self.__set_buffer_standard()
        else:
            self.pr_debug.debug_print(LogLevel.ERROR, "draw mode not supported yet")
            assert False

    def set_draw_mode(self, p_draw_mode):
        if p_draw_mode == "point":
            self.current_draw_mode = DrawMode.POINT
        elif p_draw_mode == "line":
            self.current_draw_mode = DrawMode.LINE
        elif p_draw_mode == "standard":
            self.current_draw_mode = DrawMode.STANDARD
        else:
            self.current_draw_mode = p_draw_mode

    def get_draw_mode(self):
        return self.current_draw_mode

    # ============================================================
    # draw function
    # ============================================================
    def show(self):
        img = self.device_canvas.target
        # debug
        if self.pr_debug.get_debug_enable():
            self.pr_debug.set_debug_info_img(img)
            self.pr_debug.debug_img()

        m_draw_API.draw(img)

    # ============================================================
    # private function
    # ============================================================
    def __set_buffer_point(self):
        self.device_pipe.set_input_buffer(self.vertex_buffer)
        self.device_pipe.run_pipe()

        assert self.device_pipe.is_output_ready
        l_point2_buffer = self.device_pipe.output_buffer
        for i in range(len(l_point2_buffer)):
            l_screen_position = l_point2_buffer[i]
            l_screen_x = l_screen_position[0]
            l_screen_y = l_screen_position[1]
            l_screen_color = l_screen_position[2]
            self.device_canvas.set_point(l_screen_x, l_screen_y, l_screen_color)

    def __set_buffer_line(self):
        self.device_pipe.set_input_buffer(self.vertex_buffer)
        self.device_pipe.run_pipe()

        assert self.device_pipe.is_output_ready
        l_point2_buffer = self.device_pipe.output_buffer
        l_start_point = l_point2_buffer[-1]
        for i in range(0, len(l_point2_buffer)):
            l_end_point = l_point2_buffer[i]
            l_line_buffer = Canvas.make_int_line(l_start_point, l_end_point)
            self.device_canvas.set_point_buffer(l_line_buffer)
            l_start_point = l_end_point

    def __set_buffer_standard(self):
        self.device_pipe.set_input_buffer(self.vertex_buffer)
        self.device_pipe.run_pipe()

        assert self.device_pipe.is_output_ready
        l_point2_buffer = self.device_pipe.output_buffer

        assert len(l_point2_buffer) % 3 == 0  # make sure each three points construct a triangle
        for i in range(0, len(l_point2_buffer)/3):
            l_first_point = l_point2_buffer[3*i]
            l_second_point = l_point2_buffer[3*i+1]
            l_third_point = l_point2_buffer[3*i+2]
            l_triangle_buffer = Canvas.make_int_triangle(l_first_point, l_second_point, l_third_point)
            self.device_canvas.set_point_buffer(l_triangle_buffer)

    @staticmethod
    def __read_window_size_config():
        o_width = config_warehouse.width_config
        o_height = config_warehouse.height_config
        return {'width': o_width, 'height': o_height}
