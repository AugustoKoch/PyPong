import turtle
import winsound
import time

#Tela
tela = turtle.Screen()
tela.title('Py Pong')
tela.bgcolor('black')
tela.setup(width = 1280, height = 720)
tela.tracer(0)

#Barras
barra_a = turtle.Turtle()
barra_a.shape('square')
barra_a.shapesize(stretch_wid = 5,stretch_len = 1)
barra_a.color('white')
barra_a.penup()
barra_a.goto(-590, 0)

barra_b = turtle.Turtle()
barra_b.shape('square')
barra_b.shapesize(stretch_wid = 5, stretch_len = 1)
barra_b.color('white')
barra_b.penup()
barra_b.goto(590, 0)

#Bola
bola = turtle.Turtle()
bola.shape('square')
bola.color('white')
bola.penup()
bola.goto(0, 0)
bola.dx = 0.6
bola.dy = 0.6

#Linha
linha = turtle.Turtle()
linha.color('white')
linha.width(5)
linha.penup()
linha.goto(0, 340)

for n in range(0, 14):
    linha.pendown()
    linha.sety(linha.ycor() - 20)
    linha.penup()
    linha.sety(linha.ycor() - 30)

#Placar
score = [0, 0]

placar_a = turtle.Turtle()
placar_a.color('white')
placar_a.penup()
placar_a.hideturtle()
placar_a.goto(-320, 250)
placar_a.write(score[0], font=('Arial Black', 50, 'normal'))

placar_b = turtle.Turtle()
placar_b.color('white')
placar_b.penup()
placar_b.hideturtle()
placar_b.goto(320, 250)
placar_b.write(score[1], font=('Arial Black', 50, 'normal'))

#Set
set = ['', '']

placar_set_a = turtle.Turtle()
placar_set_a.color('white')
placar_set_a.penup()
placar_set_a.hideturtle()
placar_set_a.goto(-530, 270)
placar_set_a.write(set[0], font=('Arial Black', 30, 'normal'))

placar_set_b = turtle.Turtle()
placar_set_b.color('white')
placar_set_b.penup()
placar_set_b.hideturtle()
placar_set_b.goto(530, 270)
placar_set_b.write(set[1], font=('Arial Black', 30, 'normal'))

#Mensagens de fim de jogo
msg_fimdejogo = turtle.Turtle()
msg_fimdejogo.color('white')
msg_fimdejogo.penup()
msg_fimdejogo.hideturtle()
msg_fimdejogo.goto(0, 50)

opcoes = turtle.Turtle()
opcoes.color('white')
opcoes.penup()
opcoes.hideturtle()
opcoes.goto(0, -112)

#Opções do jogo
def reiniciar():
    bola.goto(0, 0)
    barra_a.goto(-590, 0)
    barra_b.goto(590, 0)
    bola.dx = 0.6
    bola.dy = 0.6
    score[0] = 0
    score[1] = 0
    set[0] = ''
    set[1] = ''
    global vez 
    vez = 2
    placar_a.clear()
    placar_b.clear()
    placar_set_a.clear()
    placar_set_b.clear()
    opcoes.clear()
    msg_fimdejogo.clear()
    placar_a.write(score[0], font=('Arial Black', 50, 'normal'))
    placar_b.write(score[1], font=('Arial Black', 50, 'normal'))

def encerrar():
    global rodando
    rodando = False

def play():
    jogar.clear()
    titulo.clear()
    global inicio
    inicio = False

#Movimento das barras
def barra_a_up():
    if barra_a.ycor() < 310 and vez == 1:
            barra_a.sety(barra_a.ycor() + 10)

def barra_a_down():
    if barra_a.ycor() > -300 and vez == 1:
            barra_a.sety(barra_a.ycor() - 10)

def barra_b_up():
    if barra_b.ycor() < 310 and vez == 2:
            barra_b.sety(barra_b.ycor() + 10)

def barra_b_down():
    if barra_b.ycor() > -300 and vez == 2:
            barra_b.sety(barra_b.ycor() - 10)

#Vinculando o teclado
tela.listen()
tela.onkeypress(barra_a_up, 'w')
tela.onkeypress(barra_a_up, 'W')
tela.onkeypress(barra_a_down, 's')
tela.onkeypress(barra_a_down, 'S')
tela.onkeypress(barra_b_up, 'Up')
tela.onkeypress(barra_b_down, 'Down')
tela.onkeypress(play, '0')
tela.onkeypress(reiniciar, '1')
tela.onkeypress(encerrar, '2')

#Inicio
titulo = turtle.Turtle()
titulo.color('white')
titulo.penup()
titulo.hideturtle()
titulo.goto(0, 0)
titulo.write('Py Pong', align=('center'), font=('Arial Black', 75, 'normal'))

jogar = turtle.Turtle()
jogar.color('white')
jogar.penup()
jogar.hideturtle()
jogar.goto(-2, -105)
jogar.write('Pressione 0 para jogar', align=('center'), font=('Arial Black', 40, 'normal'))

inicio = True
while inicio:
    tela.update()

#Loop do jogo
vez = 2
rodando = True
while rodando:
    tela.update()

    #Movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    #Colisão barra e bola
    if 570 < bola.xcor() < 570.1 and barra_b.ycor() + 60 > bola.ycor() > barra_b.ycor() -60:
        bola.dx *= -1
        vez = 1
        winsound.PlaySound('blip.wav', winsound.SND_ASYNC)
    elif 570.1 < bola.xcor() < 610 and barra_b.ycor() + 60 > bola.ycor() > barra_b.ycor() -60:
        bola.dy *= -1
        winsound.PlaySound('blip.wav', winsound.SND_ASYNC)

    elif -570 > bola.xcor() > -570.1 and barra_a.ycor() + 60 > bola.ycor() > barra_a.ycor() -60:
        bola.dx *= -1
        vez = 2
        winsound.PlaySound('blip.wav', winsound.SND_ASYNC)
    elif -570.1 > bola.xcor() > -610 and barra_a.ycor() + 60 > bola.ycor() > barra_a.ycor() -60:
        bola.dy *= -1
        winsound.PlaySound('blip.wav', winsound.SND_ASYNC)

    #Bordas Superior e inferior
    if bola.ycor() > 350:
        bola.sety(350)
        bola.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    elif bola.ycor() < -345:
        bola.sety(-345)
        bola.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    
    #Bordas laterias e pontuação
    if bola.xcor() > 650:
        vez = 1
        time.sleep(1)
        bola.goto(0, 0)
        bola.dx *= -1
        score[0] += 1
        placar_a.clear()
        placar_a.write(score[0], font=('Arial Black', 50, 'normal'))
        if score[0] == 3:
            time.sleep(0.5)
            score[0] = 0
            score[1] = 0
            placar_a.clear()
            placar_a.write(score[0], font=('Arial Black', 50, 'normal'))
            placar_b.clear()
            placar_b.write(score[1], font=('Arial Black', 50, 'normal'))
            set[0] += 'X'
            placar_set_a.clear()
            placar_set_a.write(set[0], align=('center'), font=('Arial Black', 30, 'normal'))

    elif bola.xcor() < -650:
        vez = 2
        time.sleep(1)
        bola.goto(0, 0)
        bola.dx *= -1
        score[1] += 1
        placar_b.clear()
        placar_b.write(score[1], font=('Arial Black', 50, 'normal'))
        if score[1] == 3:
            time.sleep(0.5)
            score[0] = 0
            score[1] = 0
            placar_a.clear()
            placar_a.write(score[0], font=('Arial Black', 50, 'normal'))
            placar_b.clear()
            placar_b.write(score[1], font=('Arial Black', 50, 'normal'))
            set[1] += 'X'
            placar_set_b.clear()
            placar_set_b.write(set[1], align=('center'), font=('Arial Black', 30, 'normal'))

    #Fim de jogo
    if set[0] == 'XXX':
        bola.dx = 0
        bola.dy = 0
        msg_fimdejogo.write('O jogador 1 venceu!', align=('center'), font=('Arial Black', 50, 'normal'))
        opcoes.write('1 reiniciar\n2 encerrar', align=('center'), font=('Arial Black', 25, 'normal'))

    elif set[1] == 'XXX':
        bola.dx = 0
        bola.dy = 0
        msg_fimdejogo.write('O jogador 2 venceu!', align=('center'), font=('Arial Black', 50, 'normal'))
        opcoes.write('1 reiniciar\n2 encerrar', align=('center'), font=('Arial Black', 25, 'normal'))