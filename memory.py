import turtle

# ウィンドウの設定
wndw = turtle.Screen()
wndw.bgcolor("white")
wndw.setup(width=600, height=600)

# 軸を描画するペンの設定
axis_pen = turtle.Turtle()
axis_pen.speed(0)
axis_pen.pensize(1)

# X軸とY軸を描く関数
def draw_axis():
    # X軸
    axis_pen.penup()
    axis_pen.goto(-300, 0)
    axis_pen.pendown()
    axis_pen.goto(300, 0)

    # Y軸
    axis_pen.penup()
    axis_pen.goto(0, -300)
    axis_pen.pendown()
    axis_pen.goto(0, 300)

    # X軸の目盛り
    for x in range(-300, 301, 50):
        axis_pen.penup()
        axis_pen.goto(x, -5)
        axis_pen.pendown()
        axis_pen.goto(x, 5)

    # Y軸の目盛り
    for y in range(-300, 301, 50):
        axis_pen.penup()
        axis_pen.goto(-5, y)
        axis_pen.pendown()
        axis_pen.goto(5, y)

# 軸を描画
draw_axis()

# クリックでTurtle画面を閉じる
wndw.exitonclick()
