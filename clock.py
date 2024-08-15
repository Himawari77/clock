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
wndw.tracer() # アニメーション設定

# ペンの設定
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# digital_clock pen setting
digital_pen = turtle.Turtle()
digital_pen.hideturtle()
digital_pen.speed(0)
digital_pen.color('white')
# digital_pen.down()
# digital_pen.goto(-105, -50)

# 時計の描画
def draw_clock(hr, mn, sec, pen):
    # 時計の円を描画
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("red")
    pen.pendown()
    pen.circle(210)
    
    # 時間の目盛りを描画
    # pen.up()
    # pen.goto(0, 210)
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
        ("blue", 150, 60, 5)    # 秒針
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


# degital clock
def digital_clock():
    dt = datetime.datetime.today()
    print(dt)

    digital_time = datetime.datetime.today()
    disp_digital_time = digital_time.strftime("%y/%m/%d/%A")
    digital_pen.clear()
    digital_pen.goto(-105, -50)
    digital_pen.write(disp_digital_time, font=("Arial", 24, "normal"))


#天気情報取得
def fetch_weather_data():
    # weather_pen.down()

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 42.9172,
        "longitude": 143.2044,
        "current": "temperature_2m,relative_humidity_2m",
        "daily": "weather_code",
        "timezone": "Asia/Tokyo",
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)  # APIからのレスポンスデータ全体を確認
    print("data----------------------------------")

    # 翌日のデータを抽出
    # tomorrow_data = data['daily']['temperature_2m_max'][1], data['daily']['temperature_2m_min'][1], data['daily']['relative_humidity_2m_max'][1]
    weather = data['daily']['weather_code'][1]  # 天気コード
    print(weather)  # APIからのレスポンスデータ全体を確認
    # humidity = tomorrow_data[2]  # 湿度
    temp = data['current']['temperature_2m'] # 気温
    print(temp)

    # デジタル時刻と天気情報を表示
    return [weather, temp]
    # return f"Weather: {weather}, Temp: {temp}°C"
    # digital_pen.clear()


# 天気データ
weather_info =  fetch_weather_data()    

# tommorow's weather
def weather_picture(weather_info):
    # tommorows'weather pen setting
    t_weather_pen = turtle.Turtle()
    t_weather_pen.hideturtle()

    t_weather_pen.goto(-105, -100)

    print("weather_picture%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(weather_info)
    print(weather_info[0])
    print(weather_info[1])

    if weather_info[0] <= 40:
        t_weather_pen.write("HAER!!!")
    elif weather_info[0] > 40 and weather_info[0] <=80:
        t_weather_pen.color('gray')
        t_weather_pen.write("CLOUD")
    else :
        t_weather_pen.color('blue')
        t_weather_pen.write("RAIN")



weather_picture(weather_info)

# 時計を更新
while True:
    hr = int(time.strftime("%I"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    draw_clock(hr, mn, sec, pen)

    # time.sleep(0)
    # pen.clear()

   # デジタル時刻を表示
    digital_clock()
    # wndw.update()
    weather_pen = turtle.Turtle()
    weather_pen.hideturtle()
    weather_pen.color('green')
    weather_pen.up()
    weather_pen.goto(-105, -80)
    weather_pen.write("Weather:" + str(weather_info[0]) + " Temp:" + str(weather_info[1])+ "°C", font=("Arial", 14, "normal"))    
    # weather_pen.write("Weather:" + weather_info[0], "Temp:" + weather_info[1] + "°C", font=("Arial", 14, "normal"))    

    time.sleep(1)
    pen.clear()


wndw.mainloop()