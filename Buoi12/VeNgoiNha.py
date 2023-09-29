"""Bài tập vẽ ngôi nhà"""
import turtle
t = turtle.Turtle()
t.hideturtle()

def veHinhChuNhat(w, h, color, fill_color):
    t.pensize = 5
    t.fillcolor(fill_color)
    t.begin_fill()
    t.pencolor(color)
    t.forward(w)
    t.right(90)
    t.forward(h)
    t.right(90)
    t.forward(w)
    t.right(90)
    t.forward(h)
    t.right(90)
    t.end_fill()
    
def veMotO(x_distance, y_distance, fill_color):
    # Hàm vẽ 1 ô (gồm 2 HCN con)
    t.penup() 
    t.setx(x_distance)
    t.sety(y_distance)
    t.pendown()
    veHinhChuNhat(big_w, big_h, 'red', fill_color)    

    t.penup() 
    # t.goto(distance_x, - distance_y)
    t.setx(x_distance + distance_x)
    t.sety(y_distance - distance_y)
    t.pendown()

    veHinhChuNhat(small_w, small_h, 'blue', 'white')
    
def veOCuaChinh(x_distance, y_distance, fill_color):
    t.penup() 
    t.setx(x_distance)
    t.sety(y_distance)
    t.pendown()
    veHinhChuNhat(big_w + 50, big_h, 'red', fill_color) 

big_w = 150
big_h = 250
small_w = 80
small_h = 100
distance_x = (big_w - small_w) // 2
distance_y = (big_h - small_h) // 2

veMotO(0, 0, 'green')
veMotO(0, big_h, 'magenta')
veMotO(-big_w, 0, 'purple')
veMotO(-big_w, big_h, 'yellow')
veOCuaChinh(0 + big_w, 0, 'LightPink')

turtle.done()