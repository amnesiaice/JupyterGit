from PythonRendererCode.GraphEntities.Entity import Entity


class Triangle(Entity):
    def __init__(self):
        self.num_point = 3

    def set_point(self, p_point1, p_point2, p_point3):
        self.point_buffer = [p_point1, p_point2, p_point3]
