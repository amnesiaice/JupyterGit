import matplotlib.pyplot as plt
"""
Canvas class used for resource_manager
"""


class Canvas:
    def __init__(self):
        self.ratio = 1.0
        self.width = 600.0
        self.height = 600.0
        self.target = [[[1, 1, 1, 1]]]
        self.final_target = [[[]]]

    # set a p_width p_height original color picture
    def set_canvas(self, p_width, p_height, p_color):
        p_color = self.__get_color(p_color)
        p_width = int(p_width)
        p_height = int(p_height)
        self.width = p_width
        self.height = p_height
        self.ratio = p_width / p_height
        self.target[0][0] = p_color
        for i in range(0, p_width-1):
            self.target[0].append(p_color)
        for j in range(0, p_height-1):
            self.target.append(self.target[0])

    def draw_canvas(self):
        self.__convert_axis()
        # prepare paint
        plt.axis('off')
        plt.imshow(self.final_target)
        plt.show()

    # converting y axis to use the 
    def __convert_axis(self):
        self.final_target = self.target
        for j in range(0, self.height-1):
            for i in range(0, self.width-1):
                self.final_target[-j][i] = self.target[j][i]

    @staticmethod
    def __get_color(p_color):
        if p_color == 'red':
            return [0.9, 0.0, 0.0, 1.0]
        elif p_color == 'green':
            return [0.0, 0.9, 0.0, 1.0]
        elif p_color == 'blue':
            return [0.0, 0.0, 0.9, 1.0]
        elif p_color == 'light blue':
            return [0.28, 0.72, 0.98, 1]
        elif p_color == 'white':
            return [1.0, 1.0, 1.0, 1.0]
        elif p_color == 'black':
            return [0.0, 0.0, 0.0, 1.0]
        else:
            p_color[0] = float(p_color[0])
            p_color[1] = float(p_color[1])
            p_color[2] = float(p_color[2])
            return p_color

