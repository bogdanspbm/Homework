def balls_collide(ball1, ball2):

    if (len(ball1) or len(ball2)) != 4:
        raise TypeError('Bad input count')

    for i in range(4):
        if (type(ball1[i]) or type(ball2[i])) != float:
            raise TypeError('Wrong type')

    vecx = ball1[0] - ball2[0] # Calc x coord
    vecx = vecx * sign(vecx)

    vecy = ball1[1] - ball2[1] # Calc y coord
    vecy = vecy * sign(vecy)

    vecz = ball1[2] - ball2[2] # Calc z coord
    vecz = vecz * sign(vecz)

    veclen = sqrt(vecx ** 2 + vecy ** 2 + vecz ** 2)

    return ((veclen - ball1[3] - ball2[3]) >= 0.00000001)

print(balls_collide((100,100,100,2),(-100,-100,-100,3)))
