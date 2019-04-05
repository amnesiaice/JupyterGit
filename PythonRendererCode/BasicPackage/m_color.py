class Color:
    def __init__(self):
        # white
        self.r = 1.0
        self.g = 1.0
        self.b = 1.0
        self.a = 1.0

    def __init__(self, p_r, p_g, p_b, p_a):
        self.r = float(p_r)
        self.g = float(p_g)
        self.b = float(p_b)
        self.a = float(p_a)

    def set_color(self, p_r, p_g, p_b, p_a):
        self.r = float(p_r)
        self.g = float(p_g)
        self.b = float(p_b)
        self.a = float(p_a)

    def color_vector(self):
        return [self.r, self.g, self.b, self.a]

    @staticmethod
    def get_default_color(p_color='black'):
        if p_color == 'red':
            return [0.9, 0.0, 0.0, 1.0]
        elif p_color == 'green':
            return [0.0, 0.9, 0.0, 1.0]
        elif p_color == 'blue':
            return [0.0, 0.0, 0.9, 1.0]
        elif p_color == 'light blue':
            return [0.28, 0.72, 0.98, 1.0]
        elif p_color == 'white':
            return [1.0, 1.0, 1.0, 1.0]
        elif p_color == 'black':
            return [0.0, 0.0, 0.0, 1.0]
        else:
            print("not supported default color")
            return [1.0, 1.0, 1.0, 1.0]
