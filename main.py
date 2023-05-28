import requests
import customtkinter as ctk
import tkinter as tk


window = ctk.CTk()
sa = ctk.set_appearance_mode("light")
window.title("Weather Condition")
window.geometry("400x500")
window.resizable(False, False)
frame = ctk.CTkFrame(window)
frame.pack()

key = "020b34c04693340a08b26d7640165ec2"

cloud = tk.PhotoImage(file="Images/cloud.png")
few_cloud = tk.PhotoImage(file="Images/few clouds.png")
mist = tk.PhotoImage(file="Images/mist.png")
rain = tk.PhotoImage(file="Images/rain.png")
snow = tk.PhotoImage(file="Images/snow.png")
sun = tk.PhotoImage(file="Images/Sun.png")
thunder = tk.PhotoImage(file="Images/thunder.png")
hummid = tk.PhotoImage(file="Images/hummid.png")
wind = tk.PhotoImage(file="Images/wind.png")

canvas = ctk.CTkCanvas(frame, bg="black", width=400, height=500)
canvas.pack()

background = tk.PhotoImage(file="Images/bg.png")
canvas.create_image(200, 250, image=background)

search_bar = tk.PhotoImage(file="Images/search.png")
canvas.create_image(160, 50, image=search_bar)

entry = tk.Entry(frame, border=0, font=("Noto Sans CJK JP", 20, "bold"), width=13, fg="#606266", justify="center")
entry.place(x=50, y=33)

button1 = tk.PhotoImage(file="Images/not hover.png")
button2 = tk.PhotoImage(file="Images/button.png")
tagname = "event"



def enter():
    canvas.config(cursor="hand2")
    canvas.itemconfig(button, image=button2)


def leave():
    canvas.config(cursor="")
    canvas.itemconfig(button, image=button1)


def cmd(event):
    global name, temp_c, humidity, wind_kmh, description
    city = entry.get()
    data = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}"
    data_req = requests.get(data).json()
    lat = data_req[0]["lat"]
    lon = data_req[0]["lon"]
    weather_data = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
    weather_req = requests.get(weather_data).json()
    description = weather_req["weather"][0]["main"]
    temp_k = weather_req["main"]["temp"]
    temp = temp_k - 273,15
    temp_c = round(temp[0])
    name = weather_req["name"]
    humidity = weather_req["main"]["humidity"]
    wind_kmh = round(weather_req["wind"]["speed"])
    print(weather_req)
    update()


button = canvas.create_image(330, 50, image=button1, tag=tagname)
canvas.tag_bind(button, "<Button-1>", cmd)
canvas.tag_bind(tagname, "<Enter>", lambda event: enter())
canvas.tag_bind(tagname, "<Leave>", lambda event: leave())


weather = canvas.create_image(200, 180, image=sun)


celcius = canvas.create_text(200, 320, text=f"0°C", font=("Noto Sans CJK JP", 40, "bold"), fill="white")
city = canvas.create_text(200, 370, text="None", font=("Noto Sans CJK JP", 25, "bold"), fill="white")

hummid_img = canvas.create_image(40, 450, image=hummid)
hummid_prc = canvas.create_text(88, 447, text="0%", font=("Noto Sans CJK JP", 15, "bold"), fill="white")
hummid_text = canvas.create_text(96, 466, text="Humidity", font=("Noto Sans CJK JP", 10, "bold"), fill="white")
wind_img = canvas.create_image(240, 450, image=wind)
wind_spd = canvas.create_text(315, 447, text="0 km/h", font=("Noto Sans CJK JP", 15, "bold"), fill="white")
wind_text = canvas.create_text(316, 466, text="Wind Speed", font=("Noto Sans CJK JP", 10, "bold"), fill="white")


def update():
    canvas.itemconfig(city, text=name)
    canvas.itemconfig(celcius, text=f"{temp_c}°C")
    canvas.itemconfig(hummid_prc, text=f"{humidity}%")
    canvas.itemconfig(wind_spd, text=f"{wind_kmh} km/h")
    if description == "Clear":
        canvas.itemconfig(weather, image=sun)
    elif description == "Clouds":
        canvas.itemconfig(weather, image=cloud)
    elif description == "Drizzle":
        canvas.itemconfig(weather, image=rain)
    elif description == "Rain":
        canvas.itemconfig(weather, image=rain)
    elif description == "Thunderstorm":
        canvas.itemconfig(weather, image=thunder)
    elif description == "Snow":
        canvas.itemconfig(weather, image=snow)
    elif description == "Mist":
        canvas.itemconfig(weather, image=mist)
    print(description)


window.mainloop()
