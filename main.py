from LocationModule import *
from AirQualityModule import *
import datetime
current_datetime = datetime.datetime.now()
three_years_ago = current_datetime - datetime.timedelta(days=100)
Still_Asking = True
while(Still_Asking):
    print('''REAL TIME AIR QUALITY DETECTION ACTIVATED\n\n
          \t 1.Press 1 To Check The Air Quality Around You \n
          \t 2.Press 2 To Enter a City Manually\n
          \t 3.Press 3 To Exit
          ''')
    takingInput = int(input())
    if takingInput == 3:
        print("thankyou")
        Still_Asking = False
        break
    elif takingInput == 1:
        print("Fetching Location Details")
        GettingLocationDetails = GetYourOwnLocation()
        print(GettingLocationDetails["success"])
        if GettingLocationDetails["success"] == True:
            print('''Location Fetched Successfully\n
                  Analysing the Air Quality Near You Generating Reports In A Few Minutes......
                  ''')
            GettingTheCurrentAirQualitydetails = Get_PastAirQualityDetailsForTheLocation(
                GettingLocationDetails["response"]["latitude"],
                GettingLocationDetails["response"]["longitude"],
                int(three_years_ago.timestamp()),
                int(current_datetime.timestamp())
            )

            # ......FURTHER FUNCTION FOR ANALYSING AND PREDICTING
            print("Data Analysed Successfully")
        else:
            print("Error Getting Your Location Details")
            break

    elif takingInput == 2:
        EnteredCity = input("Enter A City You Want The Air Quality Of\n")
        GettingLocationDetails = Get_Location_coordinates_From_City(
            EnteredCity)
        if GettingLocationDetails["success"] == True:
            print('''Location Fetched Successfully\n
                  Analysing the Air Quality Near You Generating Reports In A Few Minutes......
                  ''')
            GettingTheCurrentAirQualitydetails = Get_PastAirQualityDetailsForTheLocation(
                GettingLocationDetails["response"]["latitude"],
                GettingLocationDetails["response"]["longitude"],
                int(three_years_ago.timestamp()),
                int(current_datetime.timestamp())
            )
            print("Data Analysed Successfully")

        else:
            print("Error Getting Your Location Details")
            break
