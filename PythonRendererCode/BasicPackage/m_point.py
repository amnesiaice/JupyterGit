from PythonRendererCode.BasicPackage.m_color import Color


# this class is just for user interface, when deliver to device, please use the get_vector to make it a  list
class Point:
    def __init__(self, p_x=0.0, p_y=0.0, p_z=0.0, p_color=Color.get_default_color("black")):
        self.position_x = p_x
        self.position_y = p_y
        self.position_z = p_z
        self.point_color = p_color

    def get_x(self):
        return self.position_x

    def get_y(self):
        return self.position_y

    def get_z(self):
        return self.position_z

    def get_color(self):
        return self.point_color

    def get_position(self):
        return [self.position_x, self.position_y, self.position_z]

    def get_vector(self):
        return [self.position_x, self.position_y, self.position_z, self.point_color]
