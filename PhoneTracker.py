import os
import phonenumbers
import folium


def Phonenumber_location_tracker():
    current_path = os.getcwd()
    # modules used
    import datetime
    import phonenumbers
    from phonenumbers import geocoder
    import folium
    from phonenumbers import carrier
    from opencage.geocoder import OpenCageGeocode

    num = input("Enter a number: ")
    time_ = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    # API key
    API_key = "75ce9466458945db8008706550167c1e"
    sanNummber = phonenumbers.parse(num)
    # country Location finder
    location = geocoder.description_for_number(sanNummber, "en")
    # Service provider finder
    sea_pro = phonenumbers.parse(num)
    servise_prover = carrier.name_for_number(sea_pro, 'en')
    # Finding the latitude and longitude
    geocoder = OpenCageGeocode(API_key)
    quesry = str(location)
    resltt = geocoder.geocode(quesry)
    lat = resltt[0]['geometry']['lat']
    lng = resltt[0]['geometry']['lng']
    # creating a map with the phone number location as pointer
    mymap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(mymap)
    mymap.save(f"{current_path}\\Maps\\{num + str('-') + str(time_)}.html")

    return location, servise_prover, lat, lng


# Phonenumber_location_tracker()


'''
def Track_Phone():
    from phonenumbers import geocoder
    num = input("Enter a number: ")
    number = phonenumbers.parse(num)
    location = geocoder.description_for_number(number, "en")
    print(location)

    from phonenumbers import carrier
    service_provider = phonenumbers.parse(num)
    print(carrier.name_for_number(service_provider, "en"))

    from opencage.geocoder import OpenCageGeocode

    key = "75ce9466458945db8008706550167c1e"
    geocoder = OpenCageGeocode(key)
    query = str(location)
    results = geocoder.geocode(query)
    # print(results)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(lat, lng)

    mymap = folium.Map(location=[lat, lng], zoom_control=9)
    folium.Marker([lat, lng], popup=location).add_to(mymap)
    mymap.save("locations.html")
'''


# Track_Phone()
