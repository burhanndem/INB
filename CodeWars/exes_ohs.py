def xo(s):
    amountx = 0
    amounto = 0
    for i in range(0, len(s), 1):
        if s[i] == "x":
            amountx += 1
        elif s[i] == "o":
            amounto += 1
    if amountx == amounto:
        return True
    elif amountx == 0 and amounto == 0:
        return True
    return False


xo("xoxoxxo")
