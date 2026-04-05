# 🌦 Weather App using API (Tkinter)

A simple and interactive **Weather Application** built using **Python and Tkinter** that fetches real-time weather data and forecast using the OpenWeatherMap API.

---

## 🚀 Features

* 🌡 Get current temperature of any city
* ☁ Displays weather condition (Clear, Clouds, Rain, etc.)
* 🌬 Shows wind speed
* 🔮 Shows forecast for next 3 time intervals
* 🖼 Displays weather icon dynamically
* 🔄 Convert temperature from Celsius (°C) to Fahrenheit (°F)
* ⚠ Handles errors (invalid city, empty input)
* 🎨 Clean and simple GUI

---

## 🛠 Technologies Used

* Python
* Tkinter (GUI)
* Requests (API handling)
* PIL (Pillow for images)
* OpenWeatherMap API

---

## 📦 Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/tarang-rastogi/Weather_App_API.git
```

### 2️⃣ Install Dependencies

```
pip install requests pillow
```

### 3️⃣ Run the Application

```
python Weather_App.py
```

---

## 🔑 API Configuration

This project uses **OpenWeatherMap API**.

Replace your API key in the code:

```
API_key = "your_api_key_here"
```

Get your API key from:
https://openweathermap.org/api

---

## 🧠 How It Works

1. User enters city name
2. App sends request to API
3. API returns weather data in JSON format
4. Data is extracted:

   * Temperature
   * Weather condition
   * Wind speed
   * Forecast data
5. Data is displayed in GUI
6. Convert button changes °C → °F

---

## ⚠ Error Handling

* ❌ Empty input → "Please enter the city name"
* ❌ Invalid city → "City not found!"
* ❌ No data → Conversion blocked

---

## 📈 Future Improvements

* Add 7-day forecast
* Add graphs using matplotlib
* Add auto location detection
* Add dark mode UI

---

## 👨‍💻 Author

**Tarang Rastogi**
BCA Student | Python Developer

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
