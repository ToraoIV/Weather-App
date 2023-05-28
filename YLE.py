key = "020b34c04693340a08b26d7640165ec2"
bu = f"http://api.openweathermap.org/geo/1.0/direct?q=london&appid={key}"
so = requests.get(bu)
js = so.json()
lat1 = js[0]["lat"]
lon1 = js[0]["lon"]
hava = f"https://api.openweathermap.org/data/2.5/weather?lat={lat1}&lon={lon1}&appid={key}"
os = requests.get(hava)