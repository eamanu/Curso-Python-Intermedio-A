def suma_1(x):
    if not isinstance(x, int):
        raise ValueError("no se puede usar otro tipo que no sea int")
    return x + 1
