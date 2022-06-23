import turtle as tt

# 书面体
class BasicTunicLineFormal:
    """
    draw_symbol：输入笔画位置编号可以画出相应符号
    full_symbol： 画一个完整的基本符号
    """

    def __init__(self, font_size, pensize=4, pencolor='black'):
        self.G3 = 1.73205 * font_size
        self.UNIT = 1 * font_size
        self.pensize = pensize
        self.pencolor = pencolor
        tt.penup()
        self.vowel_dic = {

        }
        self.consonant_func_list = []
        self.func_list = [self._draw0, self._draw1, self._draw2, self._draw3, self._draw4, self._draw5,
                          self._draw6, self._draw7, self._draw8, self._draw9, self._draw10, self._draw11,
                          self._circle]

    def _drawline(self, end, start=None):
        tt.speed(0)
        tt.pensize(self.pensize)
        tt.pencolor(self.pencolor)
        tt.hideturtle()
        if start != None:
            tt.setpos(start)
        tt.pendown()
        tt.setpos(end)

        tt.penup()

    def _draw0(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1]), (base_point[0] + self.G3, base_point[1]))  # 中     No.0

    def _draw1(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1] + 2 * self.UNIT),
                       (base_point[0], base_point[1] + 3 * self.UNIT))  # 上左    No.1

    def _draw2(self, base_point):
        self._drawline((base_point[0] + self.G3, base_point[1] + 2 * self.UNIT),
                       (base_point[0], base_point[1] + 3 * self.UNIT))  # 上右    No.2

    def _draw3(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1] + 2 * self.UNIT),
                       (base_point[0], base_point[1] + self.UNIT))  # 中上左   No.3

    def _draw4(self, base_point):
        self._drawline((base_point[0] + self.G3, base_point[1] + 2 * self.UNIT),
                       (base_point[0], base_point[1] + self.UNIT))  # 中上右   No.4

    def _draw5(self, base_point):
        self._drawline((base_point[0], base_point[1] + 3 * self.UNIT), (base_point[0], base_point[1]))  # 中上中   No.5

    def _draw6(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1] - 2 * self.UNIT),
                       (base_point[0], base_point[1] - 3 * self.UNIT))  # 下左    No.6

    def _draw7(self, base_point):
        self._drawline((base_point[0] + self.G3, base_point[1] - 2 * self.UNIT),
                       (base_point[0], base_point[1] - 3 * self.UNIT))  # 下有    No.7

    def _draw8(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1] - 2 * self.UNIT),
                       (base_point[0], base_point[1] - self.UNIT))  # 中下左   No.8

    def _draw9(self, base_point):
        self._drawline((base_point[0] + self.G3, base_point[1] - 2 * self.UNIT),
                       (base_point[0], base_point[1] - self.UNIT))  # 中下右   No.9

    def _draw10(self, base_point):
        self._drawline((base_point[0], base_point[1] + self.UNIT), (base_point[0], base_point[1]))  # 中下中.1 No.10
        self._drawline((base_point[0], base_point[1] - 3 * self.UNIT),
                       (base_point[0], base_point[1] - self.UNIT))  # 中下中.2

    def _draw11(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1] + 2 * self.UNIT),
                       (base_point[0] - self.G3, base_point[1]))  # 左.1   No.11
        self._drawline((base_point[0] - self.G3, base_point[1] - self.UNIT),
                       (base_point[0] - self.G3, base_point[1] - 2 * self.UNIT))  # 左.2

    def _circle(self, base_point):
        tt.setpos((base_point[0], base_point[1] - 4 * self.UNIT))
        tt.pendown()
        tt.circle(0.5 * self.UNIT)
        tt.penup()

    def full_symbol(self, base_point=(0, 0)):
        self.draw_symbol([i for i in range(13)], base_point)

    def draw_symbol(self, num_list, base_point):
        for num in num_list:
            self.func_list[num](base_point)

# 手写体
class BasicTunicLineHandwriting:
    """
    draw_symbol：输入笔画位置编号可以画出相应符号
    full_symbol： 画一个完整的基本符号
    """

    def __init__(self, font_size, pensize=4, pencolor='black'):
        self.G3 = 1.73205 * font_size
        self.UNIT = 1 * font_size
        self.pensize = pensize
        self.pencolor = pencolor
        tt.penup()
        self.vowel_dic = {

        }
        self.consonant_func_list = []
        self.func_list = [self._draw0, self._draw1, self._draw2, self._draw3, self._draw4, self._draw5,
                          self._draw6, self._draw7, self._draw8, self._draw9, self._draw10, self._draw11,
                          self._circle]

    def _drawline(self, end, start=None):
        tt.speed(0)
        tt.pensize(self.pensize)
        tt.pencolor(self.pencolor)
        tt.hideturtle()
        if start != None:
            tt.setpos(start)
        tt.pendown()
        tt.setpos(end)

        tt.penup()

    def _draw0(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1]), (base_point[0] + self.G3, base_point[1]))  # 中     No.0

    def _draw1(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1] + 2 * self.UNIT),
                       (base_point[0], base_point[1] + 3 * self.UNIT))  # 上左    No.1

    def _draw2(self, base_point):
        self._drawline((base_point[0] + self.G3, base_point[1] + 2 * self.UNIT),
                       (base_point[0], base_point[1] + 3 * self.UNIT))  # 上右    No.2

    def _draw3(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1] + 2 * self.UNIT),
                       (base_point[0], base_point[1] + self.UNIT))  # 中上左   No.3

    def _draw4(self, base_point):
        self._drawline((base_point[0] + self.G3, base_point[1] + 2 * self.UNIT),
                       (base_point[0], base_point[1] + self.UNIT))  # 中上右   No.4

    def _draw5(self, base_point):
        self._drawline((base_point[0], base_point[1] + 3 * self.UNIT), (base_point[0], base_point[1]-self.UNIT))
        # 中上中   No.5

    def _draw6(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1] - 2 * self.UNIT),
                       (base_point[0], base_point[1] - 3 * self.UNIT))  # 下左    No.6

    def _draw7(self, base_point):
        self._drawline((base_point[0] + self.G3, base_point[1] - 2 * self.UNIT),
                       (base_point[0], base_point[1] - 3 * self.UNIT))  # 下有    No.7

    def _draw8(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1] - 2 * self.UNIT),
                       (base_point[0], base_point[1] - self.UNIT))  # 中下左   No.8

    def _draw9(self, base_point):
        self._drawline((base_point[0] + self.G3, base_point[1] - 2 * self.UNIT),
                       (base_point[0], base_point[1] - self.UNIT))  # 中下右   No.9

    def _draw10(self, base_point):
        self._drawline((base_point[0], base_point[1] - 3 * self.UNIT),
                       (base_point[0], base_point[1] + self.UNIT))  # 中下中 No.10

    def _draw11(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1] + 2 * self.UNIT),
                       (base_point[0] - self.G3, base_point[1] - 2 * self.UNIT))  # 左   No.11

    def _circle(self, base_point):
        tt.setpos((base_point[0], base_point[1] - 4 * self.UNIT))
        tt.pendown()
        tt.circle(0.5 * self.UNIT)
        tt.penup()

    def full_symbol(self, base_point=(0, 0)):
        self.draw_symbol([i for i in range(1, 13)], base_point)

    def draw_symbol(self, num_list, base_point):
        for num in num_list:
            self.func_list[num](base_point)


class BasicTunicLineOriginal:
    """
    draw_symbol：输入笔画位置编号可以画出相应符号
    full_symbol： 画一个完整的基本符号
    """

    def __init__(self, font_size, pensize=4, pencolor='black'):
        self.G3 = 1.73205 * font_size
        self.UNIT = 1 * font_size
        self.pensize = pensize
        self.pencolor = pencolor
        tt.penup()
        self.vowel_dic = {

        }
        self.consonant_func_list = []
        self.func_list = [self._draw0, self._draw1, self._draw2, self._draw3, self._draw4, self._draw5,
                          self._draw6, self._draw7, self._draw8, self._draw9, self._draw10, self._draw11,
                          self._circle]

    def _drawline(self, end, start=None):
        tt.speed(0)
        tt.pensize(self.pensize)
        tt.pencolor(self.pencolor)
        tt.hideturtle()
        if start != None:
            tt.setpos(start)
        tt.pendown()
        tt.setpos(end)

        tt.penup()

    def _draw0(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1]), (base_point[0] + self.G3, base_point[1]))  # 中     No.0

    def _draw1(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1] + 2 * self.UNIT),
                       (base_point[0], base_point[1] + 3 * self.UNIT))  # 上左    No.1

    def _draw2(self, base_point):
        self._drawline((base_point[0] + self.G3, base_point[1] + 2 * self.UNIT),
                       (base_point[0], base_point[1] + 3 * self.UNIT))  # 上右    No.2

    def _draw3(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1] + 2 * self.UNIT),
                       (base_point[0], base_point[1] + self.UNIT))  # 中上左   No.3

    def _draw4(self, base_point):
        self._drawline((base_point[0] + self.G3, base_point[1] + 2 * self.UNIT),
                       (base_point[0], base_point[1] + self.UNIT))  # 中上右   No.4

    def _draw5(self, base_point):
        self._drawline((base_point[0], base_point[1] + 3 * self.UNIT), (base_point[0], base_point[1]))  # 中上中   No.5

    def _draw6(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1] - 2 * self.UNIT),
                       (base_point[0], base_point[1] - 3 * self.UNIT))  # 下左    No.6

    def _draw7(self, base_point):
        self._drawline((base_point[0] + self.G3, base_point[1] - 2 * self.UNIT),
                       (base_point[0], base_point[1] - 3 * self.UNIT))  # 下有    No.7

    def _draw8(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1] - 2 * self.UNIT),
                       (base_point[0], base_point[1] - self.UNIT))  # 中下左   No.8

    def _draw9(self, base_point):
        self._drawline((base_point[0] + self.G3, base_point[1] - 2 * self.UNIT),
                       (base_point[0], base_point[1] - self.UNIT))  # 中下右   No.9

    def _draw10(self, base_point):
        self._drawline((base_point[0], base_point[1] + self.UNIT), (base_point[0], base_point[1]))  # 中下中.1 No.10
        self._drawline((base_point[0], base_point[1] - 3 * self.UNIT),
                       (base_point[0], base_point[1] - self.UNIT))  # 中下中.2

    def _draw11(self, base_point):
        self._drawline((base_point[0] - self.G3, base_point[1] + 2 * self.UNIT),
                       (base_point[0] - self.G3, base_point[1]))  # 左.1   No.11
        self._drawline((base_point[0] - self.G3, base_point[1] - self.UNIT),
                       (base_point[0] - self.G3, base_point[1] - 2 * self.UNIT))  # 左.2

    def _circle(self, base_point):
        tt.setpos((base_point[0], base_point[1] - 4 * self.UNIT))
        tt.pendown()
        tt.circle(0.5 * self.UNIT)
        tt.penup()

    def full_symbol(self, base_point=(0, 0)):
        self.draw_symbol([i for i in range(13)], base_point)

    def draw_symbol(self, num_list, base_point):
        for num in num_list:
            self.func_list[num](base_point)


if __name__ == '__main__':
    a = BasicTunicLineFormal(15, pensize=5)
    a.full_symbol()
    tt.exitonclick()
