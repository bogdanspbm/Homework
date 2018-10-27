from math import *


def balls_collide(ball1, ball2):
    if (len(ball1) or len(ball2)) != 4:
        raise TypeError('Bad input count')

    for i in range(4):
        if (type(ball1[i]) or type(ball2[i])) != int and (type(ball1[i]) or type(ball2[i])) != float:
            raise TypeError('Wrong type')

    if ball1[3] < 0 or ball2[3] < 0:
        return ValueError('Radius should be positive')

    vecx = ball1[0] - ball2[0]  # Calc x coord

    if vecx < 0:
        vecx *= -1

    vecy = ball1[1] - ball2[1]  # Calc y coord

    if vecy < 0:
        vecy *= -1

    vecz = ball1[2] - ball2[2]  # Calc z coord

    if vecz < 0:
        vecz *= -1

    veclen = sqrt(vecx ** 2 + vecy ** 2 + vecz ** 2)

    # print(veclen)

    return veclen - (ball1[3] + ball2[3]) > 0.0000000000000000000000000001

# print(balls_collide((100, 100, 100.0, 100), (-100, -100, -100, 3)))
