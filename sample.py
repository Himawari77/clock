import turtle
import time
# ウィンドウの設定
wndw = turtle.Screen()
wndw.bgcolor("black")
wndw.setup(width=600, height=600)
wndw.title("アナログ時計")
wndw.tracer(0)
# ペンの設定
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)
# 時計の描画
def draw_clock(hr, mn, sec, pen):
    # 時計の円を描画
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)
    # 時間の目盛りを描画
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)
    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)
    # 時計の針を描画
    hands = [
        ("white", 80, 12),  # 時針
        ("blue", 150, 60),  # 分針
        ("red", 110, 60)    # 秒針
    ]
    time_set = (hr, mn, sec)
    for hand in hands:
        time_part = time_set[hands.index(hand)]
        angle = (time_part / hand[2]) * 360
        pen.penup()
        pen.goto(0, 0)
        pen.color(hand[0])
        pen.setheading(90)
        pen.rt(angle)
        pen.pendown()
        pen.fd(hand[1])
# 時計を更新
while True:
    hr = int(time.strftime("%I"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    draw_clock(hr, mn, sec, pen)
    wndw.update()
    time.sleep(1)
    pen.clear()
wndw.mainloop()