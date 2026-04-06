from PIL import Image,ImageTk # Image = open image , Imagetk= show in tkinder 
from io import BytesIO # convert internet data into usable form
import tkinter as tk
import requests

current_temp=0
forecast_temp=[]
forecast_time=[]
def get_weather():
    city=city_entry.get()
    API_key= "your_api_key_here"#  I am protect my API key here

    if city=="":
        result_label.config(text="Please enter the city name")
        return
    
    data=requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}&units=metric").json() # forecast predict future

    if data['cod']!="200":# 200 means the city name is correct
        result_label.config(text="City not found!")
        return
    temp=data['list'][0]['main']['temp']
    global current_temp,forecast_temp,forecast_time
    current_temp=temp
   
    temp1=data['list'][0]['main']['temp']
    temp2=data['list'][1]['main']['temp']
    temp3=data['list'][2]['main']['temp']
    time1=data['list'][0]['dt_txt'][11:16]
    time2=data['list'][1]['dt_txt'][11:16]
    time3=data['list'][2]['dt_txt'][11:16]

    forecast_temp=[temp1,temp2,temp3]
    forecast_time=[time1,time2,time3]

    condition=data['list'][0]['weather'][0]['description']
    speed=data['list'][0]['wind']['speed']
    icon_code=data['list'][0]['weather'][0]['icon']
    icon_url=f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

    result_label.config(
        text=f"🌡 Temp: {round(temp)}°C\n"
             f"☁ Condition: {(condition.title())}\n"
             f"🌬 Wind: {round(speed)} m/s\n"
             "\n"
             f"🔮 Forecast:\n"
             "\n"
             f"{time1} -> {round(temp1)}°C\n"
             f"{time2} -> {round(temp2)}°C\n"
             f"{time3} -> {round(temp3)}°C\n"
             )

    response=requests.get(icon_url) # to download the image
    img_data=response.content       # to get the raw data 
    img=Image.open(BytesIO(img_data)) # to convert raw data into image
    img=ImageTk.PhotoImage(img)         # convert for tkinter
    icon_label.config(image=img)      # show image
    icon_label.image=img              # without this image can't shown

def convert_temp():
    if current_temp==0:
        result_label.config(text="NO data to convert")
        return
    f_current=(current_temp*9/5)+32
   
    f1=(forecast_temp[0]*9/5)+32
    f2=(forecast_temp[1]*9/5)+32
    f3=(forecast_temp[2]*9/5)+32
    result_label.config(
        text=f"🌡temp: {round(f_current)}°F\n"
        "\n"
        f"🔮 Forecast:\n"
        "\n"
        f"{forecast_time[0]} -> {round(f1)}°F\n"
        f"{forecast_time[1]} -> {round(f2)}°F\n"
        f"{forecast_time[2]} -> {round(f3)}°F\n"
        ) 

window=tk.Tk()
window.title("Weather App using API")
window.geometry("500x700")
window.config(bg="lightblue")

tk.Label(window,text="Enter the City Name:",bg="lightblue", fg="black",font=("Arial",12,"bold")).pack(pady=20)
city_entry=tk.Entry(window,width=25,font=("Arial",12))
city_entry.pack()

tk.Button(window,text="ENTER", command=get_weather ,bg="navy",fg="white",font="bold").pack(pady=30)

tk.Label(window,text="HERE IS YOUR RESULT",bg="lightblue",fg="darkblue",font=("Arial",12,"bold")).pack(pady=10)
result_label=tk.Label(window,text="",font=("Arial",14),bg="white",fg="black",justify="center")
result_label.pack(pady=5)

icon_label=tk.Label(window,bg="lightblue")
icon_label.pack(pady=15)

tk.Button(window,text="Convert °C to °F",command=convert_temp,bg="navy", fg="white",font="bold").pack(pady=30)

tk.mainloop()
