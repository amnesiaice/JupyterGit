# class used for GraphEntities
class Point:
    def __init__(self):
        self.position = [0.0, 0.0, 0.0]
        self.color = [0.0, 0.0, 0.0, 1.0]

    def set_color(self, p_color):
        self.color = p_color

    def set_position(self, p_position):
        self.position = p_position

    def set_point(self, p_color, p_position):
        self.color = p_color
        self.position = p_position

    def get_position_x(self):
        return self.position[0]

    def get_position_y(self):
        return self.position[1]

    def get_position_z(self):
        return self.position[2]

    def get_color(self):
        return self.color
