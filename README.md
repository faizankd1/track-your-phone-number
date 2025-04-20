📍 Track Your Phone Number

This Python script allows you to track a phone number’s location and carrier information using the [`phonenumbers`](https://pypi.org/project/phonenumbers/) library and the [OpenCage Geocoding API](https://opencagedata.com/api). It fetches the approximate **GPS coordinates** of the number and plots it on an interactive map using Folium, which is saved as an HTML file.

---

 🌟 Features

- ✅ Extracts country, region, and service provider from the phone number
- 🌍 Uses OpenCage Geocode API to convert location to latitude and longitude
- 🗺️ Visualizes the location using Folium on an interactive map
- 💾 Outputs a `location.html` file you can open in your browser

---

 📦 Installation

Install the required libraries:

```bash
pip install phonenumbers opencage folium
```

---

🔑 Get an API Key

1. Sign up at [OpenCage Data](https://opencagedata.com/api).
2. Copy your API key from the dashboard.
3. Paste it into the script where indicated (e.g., `YOUR_API_KEY_HERE`).

---

 🚀 Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/faizankd1/track-your-phone-number.git
   cd track-your-phone-number
   ```

2. Run the script:
   ```bash
   python tracker.py
   ```

3. Enter the phone number in international format, e.g., `+914155552671`.

4. After execution, open `location.html` to view the location on the map.

 📌 Example

- Phone Number: +914155552671  
- Carrier: VI , airtel  
- Location: India  
- Output: Opens `location.html` showing the location on a world map

---

🛑 Disclaimer

This tool is for educational and ethical purposes only. Do not use it to track individuals without proper consent. Location accuracy is approximate and based on publicly available metadata.

---
 📄 License

MIT License – free to use, modify, and distribute with attribution.

---
 🙌 Contributing

Pull requests and issues are welcome! If you'd like to improve accuracy, UI, or add map overlays, feel free to fork and build.

```
