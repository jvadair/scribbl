def zfill(s):
    if type(s) is int:
        s = str(s)
    return s if len(s) > 1 else '0' + s