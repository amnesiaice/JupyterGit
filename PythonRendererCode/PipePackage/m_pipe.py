import PythonRendererCode.PipePackage.m_projection as m_projection


class Pipe:
    def __init__(self):
        self.input_buffer = []
        self.output_buffer = []
        self.is_output_ready = False
        self.main_camera_location = [0.0, 0.0, 0.0]

    def run_pipe(self):
        self.__convert_world_to_screen()
        self.is_output_ready = True

    def set_input_buffer(self, p_vertex_buffer):
        for i_point in p_vertex_buffer:
            self.input_buffer.append(i_point)

    def __convert_world_to_screen(self):
        for i_point in self.input_buffer:
            i_point = m_projection.convert_world_to_screen(i_point)
            self.output_buffer.append(i_point)
