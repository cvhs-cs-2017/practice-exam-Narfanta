def poopEncrypt(phrase):
    result = ''
    for ch in phrase:
        if ch == 'a':
            result = result + 'poop'
        elif ch == 'A':
            result = result + 'Poop'
        elif ch == 'b':
            result = result + 'pOop'
        elif ch == 'B':
            result = result + 'poOp'
        elif ch == 'c':
            result = result + 'pooP'
        elif ch == 'C':
            result = result + 'POop'
        elif ch == 'd':
            result = result + 'PoOp'
        elif ch == 'D':
            result = result + 'PooP'
        elif ch == 'e':
            result = result + 'pOOp'
        elif ch == 'E':
            result = result + 'pOoP'
        elif ch == 'f':
            result = result + 'poOp'
        elif ch == 'F':
            result = result + 'poOP'
        elif ch == 'g':
            result = result + 'POOp'
        elif ch == 'G':
            result = result + 'POoP'
        elif ch == 'h':
            result = result + 'PoOP'
        elif ch == 'H':
            result = result + 'pOOP'
        elif ch == 'i':
            result = result + 'POOP'
        elif ch == 'I':
            result = result + 'p0op'
        elif ch == 'j':
            result = result + 'P0op'
        elif ch == 'J':
            result = result + 'p0Op'
        elif ch == 'k':
            result = result + 'p0oP'
        elif ch == 'K':
            result = result + 'P0Op'
        elif ch == 'l':
            result = result + 'P0oP'
        elif ch == 'L':
            result = result + 'p0OP'
        elif ch == 'm':
            result = result + 'P0OP'
        elif ch == 'M':
            result = result + 'po0p'
        elif ch == 'n':
            result = result + 'Po0p'
        elif ch == 'N':
            result = result + 'pO0p'
        elif ch == 'o':
            result = result + 'po0P'
        elif ch == 'O':
            result = result + 'PO0p'
        elif ch == 'p':
            result = result + 'Po0P'
        elif ch == 'P':
            result = result + 'pO0P'
        elif ch == 'q':
            result = result + 'PO0P'
        elif ch == 'Q':
            result = result + 'p00p'
        elif ch == 'r':
            result = result + 'P00p'
        elif ch == 'R':
            result = result + 'p00P'
        elif ch == 's':
            result = result + 'P00P'
        elif ch == 'S':
            result = result + 'p*op'
        elif ch == 't':
            result = result + 'P*op'
        elif ch == 'T':
            result = result + 'p*Op'
        elif ch == 'u':
            result = result + 'p*oP'
        elif ch == 'U':
            result = result + 'P*Op'
        elif ch == 'v':
            result = result + 'P*oP'
        elif ch == 'V':
            result = result + 'p*OP'
        elif ch == 'w':
            result = result + 'P*OP'
        elif ch == 'W':
            result = result + 'po*p'
        elif ch == 'x':
            result = result + 'Po*p'
        elif ch == 'X':
            result = result + 'pO*p'
        elif ch == 'y':
            result = result + 'po*P'
        elif ch == 'Y':
            result = result + 'PO*p'
        elif ch == 'z':
            result = result + 'pO*P'
        elif ch == 'Z':
            result = result + 'RIPDavid'
        else:
            result = result + ch
    return result
print(poopEncrypt('Ziggy\'s sweets are mine'))
