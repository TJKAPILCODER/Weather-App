# program c5eated by: TJ Kapil
# 3 packages used:
# 1. Tinker (UI)
import tkinter as tk
# 2. requests (JASON files)
import requests
# 3. time (format variables)
import time
# function to get data from the API (OpenWeather`s API)) used postman for confirmation. Pass the canvas
def getWeather(canvas):
  # get city name from the textfield
  city = textfield.get()
  # make api variable with call to the API (use city variable)
  api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=ce4a136a35dfc4f66c12aa954fb9e240"
  # call JSON data using the requests
  json_data = requests.get(api).json()
  # extract weather from weather and main key index = 0 and temp
  condition = json_data['weather'][0]['main']
  # the temp is in kelvin, convert to fahrenheit
  # data is in float format so convert to int
  temp = int(json_data['main']['temp'] - 273.15)
  # extract the min and max temp
  min_temp = int(json_data['main']['temp_min'] - 273.15)
  max_temp = int(json_data['main']['temp_max'] - 273.15)
  # extract the pressure data
  pressure = json_data['main']['pressure']
  # extract the humidity data
  humidity = json_data['main']['humidity']
  # extract the wind speed data
  wind_speed = json_data['wind']['speed']
  # extract the sun rise and set data
  # convert seconds to hours and minutes using the time module
  # add or subtract time zone to get correct time GMT 7 Seattle subtracts 7 hours from time
  sunrise = time.strftime("%I:%M %S", time.gmtime(json_data['sys']['sunrise'] - 25200))
  sunset = time.strftime("%I:%M %S", time.gmtime(json_data['sys']['sunset'] - 25200))

  # print the data to the screen, store data in final_info variable
  final_info = condition + "\n" + str(temp) + "°C"
  final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind_speed) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset:" + sunset
  # attach to labels created.
  label_1.config(text=final_info)
  label_2.config(text=final_data)

# Define our UI (User Interface)
canvas = tk.Tk()
# Define geometry size of canvas
canvas.geometry("600x500")
# Define color of canvas --> yellow
canvas.configure(bg='yellow')
# Set the title of the canvas
canvas.title("TJ's Weather App")
# Define fonts for canvas (size, name, type) store into variable f and into variable t
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")
# Define a text field to get the city name from the USER as input in canvas with font t.
textfield = tk.Entry(canvas, justify="center" ,font = t)
# pack the entry given
textfield.pack(pady = 20)
# make it so that the user can enter directly. (no need to move cursor
textfield.focus()
# when ever user enters city name and hits the enter button. It will load the
# weather data/info of that particular city from the API. (getWeather function) is called everytime the user hits enter.
textfield.bind("<Return>", getWeather)
# Create lables to show the data on canavas with font f.
label_1 = tk.Label(canvas, font = t)
# pack the labels
label_1.pack()
label_2 = tk.Label(canvas, font = f)
# pack the labels
label_2.pack()
# Loop to start the canvas
canvas.mainloop()
