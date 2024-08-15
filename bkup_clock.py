import turtle
import time
import webbrowser
import datetime
import requests

# ウィンドウの設定
wndw = turtle.Screen()
wndw.bgcolor("black")
wndw.setup(width=600, height=600)
wndw.title("アナログ時計")
wndw.tracer(10) # アニメーション設定

# ペンの設定
pen = turtle.Turtle()
# pen.hideturtle()
pen.speed(10)
# pen.pensize(20)

# digital_clock pen setting
digital_pen = turtle.Turtle()
digital_pen.hideturtle()
digital_pen.speed(0)
digital_pen.color('white')
digital_pen.goto(-105, -50)
digital_pen.down()

# cloud setting
def cloud():
    pen.color("green")
    pen.up()
    pen.goto(-200, 100)
    pen.setheading(135)
    pen.pendown()
    pen.circle(33, extent=200)

    pen.up()
    pen.goto(-160, 100)
    pen.setheading(135)
    pen.pendown()
    pen.circle(33, extent=90)

    pen.up()
    pen.goto(-150, 40)
    pen.setheading(0)
    pen.pendown()
    pen.circle(33, extent=200)

    pen.up()
    pen.goto(-240, 50)
    pen.setheading(-90)
    pen.pendown()
    pen.circle(40,  extent=200)


# sun setting
def sun():

    pen.color("white")
    pen.up()
    pen.goto(-100, 100)
    pen.setheading(270)
    pen.pendown()
    pen.circle(100, extent=90)



# 時計の描画
def draw_clock(hr, mn, sec, pen):
    # 時計の円を描画
    pen.up()
    # pen.goto(0, 210)
    # pen.setheading(180)
    pen.goto(0, -210)
    pen.setheading(0)
    pen.color("white")
    pen.pendown()
    pen.circle(210)
    # 時間の目盛りを描画
    pen.up()
    pen.goto(0, 210)
    # pen.setheading(90)
    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    # 時計の針を描画
    hands = [
        ("white", 100, 12, 20),  # 時針
        ("white", 160, 60, 10),  # 分針
        ("blue", 100, 60, 5)    # 秒針
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
        pen.pensize(hand[3])
        pen.pendown()
        pen.fd(hand[1])


#天気情報取得
def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 42.9172,
        "longitude": 143.2044,
        "current": "temperature_2m,relative_humidity_2m",
        "hourly": "temperature_2m",
        "daily": "weather_code",
        "timezone": "Asia/Tokyo",
        # "past_days": 7
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)  # APIからのレスポンスデータ全体を確認

    



    # # 翌日のデータを抽出
    # tomorrow_data = data['daily']['temperature_2m_max'][1], data['daily']['temperature_2m_min'][1], data['daily']['relative_humidity_2m_max'][1]

    # weather = data['daily']['weather_code'][1]  # 天気コード
    # # max_temp = tomorrow_data[0]  # 最高気温
    # # min_temp = tomorrow_data[1]  # 最低気温
    # # humidity = tomorrow_data[2]  # 湿度

    # max_temp = data['daily']['temperature_2m_max'][1]  # 最高気温
    # min_temp = data['daily']['temperature_2m_min'][1]  # 最低気温
    # humidity = data['daily']['relative_humidity_2m_max'][1]  # 湿度

    # return weather, max_temp, min_temp, humidity





# degital clock
def digital_clock():
    dt = datetime.datetime.today()
    print(dt)

    # digital_time = datetime.datetime.today()
    # digital_pen.clear()
    # digital_pen.write(digital_time, font=("Arial", 24, "normal"))

    digital_time = datetime.datetime.today()
    disp_digital_time = digital_time.strftime("%y/%m/%d/%A")
    digital_pen.clear()
    digital_pen.write(disp_digital_time, font=("Arial", 24, "normal"))

# wether_today
# def wether_today():


# url = 'https://weathernews.jp/onebox/tenki/hokkaido/01207/'
# webbrowser.open(url, new=0, autoraise=True)

# 時計を更新
while True:
    hr = int(time.strftime("%I"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    draw_clock(hr, mn, sec, pen)

    # time.sleep(1)
    # pen.clear()

    digital_clock()
    cloud()


    # 天気データを取得
    weather, max_temp, min_temp, humidity = fetch_weather_data()
    
    # デジタル時刻と天気情報を表示
    digital_time = time.strftime("%Y-%m-%d %H:%M:%S")
    weather_info = f"Weather: {weather}, Max Temp: {max_temp}°C, Min Temp: {min_temp}°C, Humidity: {humidity}%"
    digital_pen.clear()
    digital_pen.write(digital_time + ' ' + weather_info, font=("Arial", 14, "normal"))
    

    wndw.update()
    time.sleep(60)
    pen.clear()
    # wndw.update()


    
wndw.mainloop()



# url = 'https://weathernews.jp/onebox/tenki/hokkaido/01207/'
# webbrowser.open(url, new=0, autoraise=True)


# **************************************************************************
# import matplotlib.pyplot as plt

# # 円の中心座標と半径を設定
# center_x = 0.5
# center_y = 0.5
# radius = 0.4

# fig, ax = plt.subplots()
# # 円を描画
# circle = plt.Circle((center_x, center_y), radius, color='blue', fill=False)
# ax.add_patch(circle)

# # グラフのアスペクト比を1に設定
# ax.set_aspect('equal', adjustable='datalim')
# plt.plot()  # 空のプロットで座標系を表示
# plt.show()

# **************************************************************************
