
while True: 

    city_flight = input("Please enter the city you will be flying to: (Paris, Milan or Barcelona) ")
    if city_flight.upper() in ['PARIS', 'MILAN', 'BARCELONA']:
        break
    print("Please enter a city from the options given! ")
while True:
    try: 
        num_nights = int(input("Please enter the number of nights you will be staying at the hotel: "))
        break
    except:
        print("Please enter a valid number of nights! ")
while True:
    try: 
        rental_days = int(input("Please enter the number of days you will be hiring the car: "))
        break
    except:
        print("Please enter a valid number of days! ")

def hotel_cost(num_nights):
    total_hotel_cost = num_nights*120
    return total_hotel_cost

def plane_cost(city_flight):
    flight_cost = 0
    if city_flight == 'Paris': 
        flight_cost = 75 
    elif city_flight == 'Milan': 
        flight_cost = 125 
    else: 
        flight_cost = 50          
    
    return flight_cost

def car_rental(rental_days):
    car_rental_cost = rental_days*97
    return car_rental_cost

def holiday_cost(num_nights, city_flight, rental_days):

    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city_flight)
    total_car_rental_cost = car_rental(rental_days)
    
    total_holiday_cost = total_hotel_cost + total_plane_cost + total_car_rental_cost 
    return total_holiday_cost
    
print("Your Holiday cost: ")
print("City you are travelling to is: " + city_flight.capitalize())
print("Number of nights you are statying at the hotel is: " + str(num_nights))
print("Number of days your are renting a car is: " + str(rental_days))
print("Total cost for your holiday: £" + str(holiday_cost(num_nights, city_flight, rental_days)))