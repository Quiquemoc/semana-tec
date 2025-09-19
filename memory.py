from random import shuffle
from turtle import *
from freegames import path

car = path('car.gif')
# CAMBIO: Usamos letras en lugar de números
tiles = list('ABCDEFGHIJKLMNOP') * 2
state = {'mark': None, 'taps': 0}
hide = [True] * 64  # La cuadrícula sigue siendo 8x8
found_all = False

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    state['taps'] += 1  # CAMBIO: contar taps

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    global found_all
    hidden_count = 0  # Para saber si el juego ya se terminó

    for count in range(64):
        x, y = xy(count)
        if hide[count]:
            square(x, y)
            hidden_count += 1
        else:
            up()
            goto(x + 25, y + 5)  # CAMBIO: centrado del texto
            color('black')
            write(tiles[count], align='center', font=('Arial', 30, 'normal'))

    mark = state['mark']
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 5)  # CAMBIO: centrado del texto
        color('black')
        write(tiles[mark], align='center', font=('Arial', 30, 'normal'))

    # CAMBIO: Mostrar número de taps
    up()
    goto(-190, 190)
    color('blue')
    write(f'Taps: {state["taps"]}', font=('Arial', 14, 'normal'))

    # CAMBIO: Detectar si se terminó el juego
    if hidden_count == 0 and not found_all:
        found_all = True
        up()
        goto(0, -220)
        color('green')
        write('¡Juego terminado!', align='center', font=('Arial', 18, 'bold'))

    update()
    ontimer(draw, 100)

# INICIO
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
