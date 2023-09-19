import geocoder
from geopy.geocoders import Nominatim


def GetYourOwnLocation():

    location = geocoder.ip('me')

    if location.ok:
        own_location = location.latlng
        latitude, longitude = own_location
        # GettingCityAndState = Get_city_And_State_From_LocationCoordinates(
        #     latitude, longitude)
        # print(GettingCityAndState)
        return {"success": True, "response": {"latitude": latitude, "longitude": longitude}}
    else:
        return {"success": False, "response": "Error In Getting Location Details"}


# def Get_city_And_State_From_LocationCoordinates(latitude, longitude):
#     geolocator = Nominatim(user_agent="location_app")
#     location = geolocator.reverse((latitude, longitude), exactly_one=True)

#     if location:
#         address = location.address
#         address_parts = address.split(", ")
#         if len(address_parts) >= 3:

#             city = address_parts[-4]
#             state = address_parts[-3]
#             return {"city": city, "state": state, "address": address_parts, latitude: latitude, longitude: longitude}

#     return None, None


GetYourOwnLocation()
# 12.969633493708795, 79.16345160304921
# testinglocation = Get_city_And_State_From_LocationCoordinates(
#     12.969633493708795, 79.16345160304921)
# print(testinglocation)


def Get_Location_coordinates_From_City(city):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city)
    print(location.latitude, location.longitude)
    if location.latitude and location.longitude:
        return {"success": True, "response": {"latitude": location.latitude, "longitude": location.longitude}}
    else:
        return {"success": False, "response": "Error In Getting Location Details"}

# print("Hello")
