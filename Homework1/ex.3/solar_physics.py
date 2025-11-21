from random import randint

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""

class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    
    type = "star"
    """Признак объекта звезды"""
    def __init__(self):
        self.m = 0
        self.x = 0
        """Координата по оси **x**"""

        self.y = 0
        """Координата по оси **y**"""

        self.Vx = 0
        """Скорость по оси **x**"""

        self.Vy = 0
        """Скорость по оси **y**"""

        self.Fx = 0
        """Сила по оси **x**"""

        self.Fy = 0
        """Сила по оси **y**"""

        self.R = 5
        """Радиус звезды"""

        self.color = "red"
        """Цвет звезды"""

        self.image = None
        """Изображение звезды"""


class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    def __init__(self):
        """Признак объекта планеты"""

        self.m = 0
        """Масса планеты"""

        self.x = 0
        """Координата по оси **x**"""

        self.y = 0
        """Координата по оси **y**"""

        self.Vx = 0
        """Скорость по оси **x**"""

        self.Vy = 0
        """Скорость по оси **y**"""

        self.Fx = 0
        """Сила по оси **x**"""

        self.Fy = 0
        """Сила по оси **y**"""

        self.R = 5
        """Радиус планеты"""

        self.color = "green"
        """Цвет планеты"""

        self.image = None
        """Изображение планеты"""
    
    
def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue
        rx = obj.x-body.x
        ry = obj.y - body.y
        rr=rx**2+ry**2
        r = (rr)**0.5
        F = gravitational_constant*body.m*obj.m/rr
        Fx = F*rx/r
        Fy = F*ry/r
        body.Fx+=Fx
        body.Fy+=Fy


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    ax = body.Fx/body.m
    ay = body.Fy/body.m
    body.Vx += ax*dt
    body.Vy += ay*dt
    body.x += body.Vx*dt
    body.y += body.Vy*dt

    '''ax = 'ya'
    body.x = 'ne'
    body.Vx = 'znayu'
    ay = 'kinematiku'
    body.y += 'kak'
    body.Vy += 'mne'
    zhitь ( ͡ಥ ͜ʖ ͡ಥ)'''


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")