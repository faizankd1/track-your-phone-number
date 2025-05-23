import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode

user_number = input("Enter phone number with country code (e.g., +919876543210): ").strip()

try:
    check_number = phonenumbers.parse(user_number, None)
except phonenumbers.phonenumberutil.NumberParseException:
    print("Invalid phone number format. Please try again.")
    exit()

number_location = geocoder.description_for_number(check_number, "en")
service_provider = carrier.name_for_number(check_number, "en")

print("\n📍 Location:", number_location)
print("📞 Service Provider:", service_provider)

api_key = "YOUR_OPENCAGE_API_KEY"
geocoder = OpenCageGeocode(api_key)

results = geocoder.geocode(number_location)

if results:
    lat, lng = results[0]['geometry']['lat'], results[0]['geometry']['lng']
    print(f"🌍 Latitude: {lat}, Longitude: {lng}")

    my_map = folium.Map(location=[lat, lng], zoom_start=10)
    folium.Marker([lat, lng], popup=f"Location: {number_location}\nProvider: {service_provider}").add_to(my_map)

    map_filename = "phone_location.html"
    my_map.save(map_filename)
    print(f"🗺️ Map saved as {map_filename}. Open it in your browser.")
else:
    print("⚠️ Could not find latitude/longitude for the given location.")
