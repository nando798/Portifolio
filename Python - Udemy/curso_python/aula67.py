def soma(x, y, z=None):

    if z is not None:
        print(f"{x=}, {y=}, {z=} = {x+z+y}")
    else:
        print(f"{x=}, {y=} = {x+y}")


soma(2, 6)
soma(4, 8)
soma(2, 7, 9)
soma(y=9, x=6, z=5)
