print('''
import turtle
def draw_tree(length, left_angle, right_angle, depth, factor):
    if depth == 0:
        return
    turtle.forward(length)
    turtle.left(left_angle)
    draw_tree(length * factor, left_angle, right_angle, depth - 1, factor)
    turtle.right(left_angle + right_angle)
    draw_tree(length * factor, left_angle, right_angle, depth - 1, factor)
    turtle.left(right_angle)
    turtle.backward(length)

turtle.speed(0)
turtle.left(90)
turtle.up()
turtle.backward(100)
turtle.down()
draw_tree(100, 20, 25, 5, 0.7)
turtle.hideturtle()
turtle.done()
turtle.hideturtle()
turtle.done()

# This prevents the window from closing immediately
import time
time.sleep(100)

''')
