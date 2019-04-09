from PythonRendererCode import config_warehouse
import m_math_API


class Pipe:
    def __init__(self):
        self.input_buffer = []
        self.output_buffer = []
        self.is_output_ready = False

        # camera
        self.main_camera_location = [100.0, 0.0, 100.0]
        self.main_camera_look_at = [0.0, 1.0, 0.0]
        self.main_camera_top = [0.0, 0.0, 1.0]
        assert m_math_API.is_perpendicular(self.main_camera_look_at, self.main_camera_top)

        # viewport
        l_viewport_config = Pipe.__read_viewport_config()
        self.viewport_width = l_viewport_config['width']
        self.viewport_height = l_viewport_config['height']
        self.viewport_min_depth = l_viewport_config['min_depth']
        self.viewport_max_depth = l_viewport_config['max_depth']
        self.viewport_center = [self.viewport_width/2, self.viewport_height/2]

    def run_pipe(self):
        for i_point in self.input_buffer:
            # directly use x,y coord position
            # i_point = m_projection.convert_world_to_screen(i_point)

            # projection to camera
            l_point = self.__convert_world_to_camera(i_point)
            l_point = self.__convert_camera_to_screen(l_point)
            o_point = l_point
            self.output_buffer.append(o_point)
        self.is_output_ready = True

    def set_input_buffer(self, p_vertex_buffer):
        for i_point in p_vertex_buffer:
            self.input_buffer.append(i_point)

    def set_viewport(self, p_min_depth, p_max_depth, p_width, p_height):
        self.viewport_width = p_width
        self.viewport_height = p_height
        self.viewport_min_depth = p_min_depth
        self.viewport_max_depth = p_max_depth

    def __convert_world_to_camera(self, p_point):
        transform_matrix = m_math_API.make_world2camera_matrix(
            self.main_camera_location, self.main_camera_look_at, self.main_camera_top)
        l_point = m_math_API.point_transform(transform_matrix, p_point)
        l_point.append(p_point[3])
        o_point = l_point
        return o_point

    def __convert_camera_to_screen(self, p_point):
        self.main_camera_location
        o_x = p_point[0]
        o_y = p_point[1]
        o_c = p_point[3]
        return [int(o_x), int(o_y), o_c];

    # ============================================================
    # config function
    # ============================================================
    @staticmethod
    def __read_viewport_config():
        o_viewport_width = config_warehouse.viewport_width_config
        o_viewport_height = config_warehouse.viewport_height_config
        o_viewport_min_depth = config_warehouse.viewport_min_depth_config
        o_viewport_max_depth = config_warehouse.viewport_max_depth_config
        o_viewport_top_left_x = config_warehouse.viewport_top_left_x
        o_viewport_top_left_y = config_warehouse.viewport_top_left_y
        return {
            'width': o_viewport_width,
            'height': o_viewport_height,
            'min_depth': o_viewport_min_depth,
            'max_depth': o_viewport_max_depth,
            'top_left_x': o_viewport_top_left_x,
            'top_left_y': o_viewport_top_left_y,
                }

