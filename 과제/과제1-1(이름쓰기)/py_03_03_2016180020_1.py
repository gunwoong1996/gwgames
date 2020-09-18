import turtle
#이동함수
def move(length):
	turtle.penup()
	turtle.forward(length)
	turtle.pendown()
def go(x,y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	
move(-400)#초기위치
#자음함수
def bi():#ㅂ
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.penup()
    turtle.backward(100)
    turtle.right(90)
    turtle.pendown()
    turtle.backward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.penup()
    turtle.backward(100)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(180)
def gi():#ㄱ
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
def ni():#ㄴ
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)

#모음함수
def ah():#ㅏ
    turtle.right(90)
    turtle.forward(100)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(50)
def ae():#ㅓ
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.backward(100)
    turtle.right(90)

def wo():#ㅜ
    turtle.forward(160)
    turtle.backward(80)
    turtle.right(90)
    turtle.forward(80)
    turtle.left(90)

    
bi()
go(-250,100)
ah()
go(-350,-50)
gi()
go(-150,100)
gi()
go(-50,50)
ae()
go(-80,-50)
ni()
go(190,30)
turtle.circle(50)
go(110,10)
wo()
go(190,-170)
turtle.circle(50)
turtle.exitonclick()

