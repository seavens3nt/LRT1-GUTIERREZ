stations = [
    "Roosevelt", "Balintawak", "Monumento", "5th Avenue", "R. Papa", "Abad Santos", 
    "Blumentritt", "Tayuman", "Bambang", "Doroteo Jose", "Carriedo", "Central Terminal",
    "UN Avenue", "Pedro Gil", "Quirino", "Vito Cruz", "Gil Puyat", "Libertad", 
    "EDSA", "Baclaran"
]

distances = [
    0.59, 1.01, 0.73, 1.06, 0.83, 0.79, 0.75, 1.21, 0.73, 
    0.69, 0.65, 0.62, 0.67, 0.93, 0.66, 0.95, 1.09, 2.25, 
    1.87
]

stored_value_fares = [
    [13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 23, 24, 25, 26, 27, 28, 29, 30, 33, 35],
    [14, 13, 15, 15, 17, 18, 19, 20, 21, 22, 23, 24, 24, 25, 26, 27, 28, 29, 32, 34],
    [15, 15, 13, 14, 15, 16, 17, 18, 20, 21, 22, 22, 23, 24, 25, 26, 27, 28, 31, 33],
    [16, 15, 14, 13, 15, 16, 17, 17, 19, 20, 21, 21, 22, 23, 24, 25, 26, 27, 30, 32],
    [17, 17, 15, 15, 13, 14, 15, 16, 18, 19, 19, 20, 21, 22, 23, 24, 25, 26, 29, 31],
    [18, 18, 16, 16, 14, 13, 14, 15, 17, 18, 18, 19, 20, 21, 22, 23, 24, 25, 28, 30],
    [19, 19, 17, 17, 15, 14, 13, 14, 16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 27, 29],
    [20, 20, 18, 17, 16, 15, 14, 13, 15, 16, 16, 17, 18, 19, 20, 21, 22, 23, 26, 28],
    [22, 21, 20, 19, 18, 17, 16, 15, 13, 14, 15, 16, 17, 17, 18, 19, 20, 22, 24, 27],
    [23, 22, 21, 20, 19, 18, 17, 16, 14, 13, 14, 15, 16, 16, 18, 18, 20, 21, 24, 26],
    [23, 23, 22, 21, 19, 18, 17, 16, 15, 14, 13, 14, 15, 16, 17, 18, 19, 20, 23, 25],
    [24, 24, 22, 21, 20, 19 ,18, 17, 16, 15, 14, 13, 14, 15, 16, 17, 18, 19, 22, 24],
    [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 14, 15, 16, 17, 18, 21, 23],
    [26, 25, 24, 23, 22, 21, 20, 19, 17, 16, 16, 15, 14, 13, 14, 15, 16, 18, 20, 23],
    [27, 26, 25, 24, 23, 22, 21, 20, 18, 18, 17, 16, 15, 14, 13, 14, 15, 17, 19, 22],
    [28, 27, 26, 25, 24, 23, 22, 21, 19, 18, 18, 17, 16, 15, 14, 13, 14, 16, 18, 21],
    [29, 28, 27, 26, 25, 24, 23, 22, 20, 20, 19, 18, 17, 16, 15, 14, 13, 15, 17, 20],
    [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 18, 17, 16, 15, 13, 16, 18],
    [33, 32, 31, 30, 29, 28, 27, 26, 24, 24, 23, 22, 21, 20, 19, 18, 17, 16, 13, 16],
    [35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 23, 22, 21, 20, 18, 16, 13]
]

single_journey_fares = [
    [0, 15, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 30, 30, 30, 30, 30, 35, 35],
    [15, 0, 15, 15, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 30, 30, 30, 30, 35, 35],
    [15, 15, 0, 15, 15, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 30, 30, 30, 35, 35],
    [20, 15, 15, 0, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 30, 30, 30, 35],
    [20, 20, 15, 15, 0, 15, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 30, 30, 35],
    [20, 20, 20, 20, 15, 0, 15, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 30, 30],
    [20, 20, 20, 20, 15, 15, 0, 15, 20, 20, 20, 20, 20, 20, 25, 25, 25, 25, 30, 30],
    [20, 20, 20, 20, 20, 15, 15, 0, 15, 20, 20, 20, 20, 20, 20, 25, 25, 25, 30, 30],
    [25, 25, 20, 20, 20, 20, 20, 15, 0, 15, 15, 20, 20, 20, 20, 20, 20, 25, 25, 30],
    [25, 25, 25, 20, 20, 20, 20, 20, 15, 0, 15, 15, 20, 20, 20, 20, 20, 25, 25, 30],
    [25, 25, 25, 25, 20, 20, 20, 20, 15, 15, 0, 15, 15, 20, 20, 20, 20, 20, 25, 25],
    [25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, 0, 15, 15, 20, 20, 20, 20, 25, 25],
    [25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, 0, 15, 15, 20, 20, 20, 25, 25],
    [30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, 0, 15, 15, 20, 20, 20, 25],
    [30, 30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, 0, 15, 15, 20, 20, 25],
    [30, 30, 30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, 0, 15, 20, 20, 25],
    [30, 30, 30, 30, 25, 25, 25, 25, 20, 20, 20, 20, 20, 20, 15, 15, 0, 15, 20, 20],
    [30, 30, 30, 30, 30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 20, 15, 0, 20, 20],
    [35, 35, 35, 30, 30, 30, 30, 30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 0, 20],
    [35, 35, 35, 35, 35, 30, 30, 30, 30, 30, 25, 25, 25, 25, 25, 25, 20, 20, 20, 0]
]

discounts = {
    "regular": 0.0,
    "student": 0.20,
    "pwd": 0.30,
    "senior": 0.30
}

def get_card_type():
    print("\n♡ Select Passenger Type: Regular, Student, PWD/Senior ♡")
    card_type = input("\nʚ Enter Passenger Type: ").strip().lower()
    print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
    while card_type not in discounts:
        card_type = input("ʚ Enter Passenger Type: ").strip().lower()
        print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌\n")
    return card_type

def calculate_fare(start_idx, end_idx, fare_matrix, discount_rate):
    fare = fare_matrix[start_idx][end_idx]
    discounted_fare = fare * (1 - discount_rate)
    return discounted_fare

def main():
    total_distance = 0
    total_fare = 0
    total_stations_passed = 0
    card_type = get_card_type()
    discount_rate = discounts[card_type]

    print("\n♡ Select Card Type: Enter '1' for Beep Card or '2' Single Journey Ticket ♡")
    fare_type = input("\nʚ Enter Card Type: ").strip().upper()
    print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌\n")
    while fare_type not in ['1', '2']:
        print("\n♡ Invalid choice. Try again. ♡")
        fare_type = input("\nʚ Enter Card Type: ").strip().upper()
        print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
    
    fare_matrix = stored_value_fares if fare_type == '1' else single_journey_fares

    print("♡ List of Stations ♡")
    print("(Enter Number Only)\n")
    for idx, station in enumerate(stations):
        print(f"{idx}: {station}")

    print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")

    while True:
        try:
            initial_station_idx = int(input("\nʚ Select Initial Station: ").strip())
            if 0 <= initial_station_idx < len(stations):
                break
            else:
                print("\n♡ Invalid station number. Please select a valid station number. ♡")
        except ValueError:
            print("\n♡ Invalid input. Please enter a valid number. ♡")

    print(f"\n» You are currently at {stations[initial_station_idx]} station.")

    while True:
        while True:
            try:
                print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")
                final_station_idx = int(input("\nʚ Select Final Station: ").strip())
                if 0 <= final_station_idx < len(stations):
                    if final_station_idx != initial_station_idx:
                        break
                    else:
                        print("\n♡ Initial and final station cannot be the same. Please choose a different final station.♡")
                else:
                    print("\n♡ Invalid station number. Please select a valid station number. ♡")
            except ValueError:
                print("\n♡ Invalid input. Please enter a valid number. ♡")

        fare = calculate_fare(initial_station_idx, final_station_idx, fare_matrix, discount_rate)
        distance = sum(distances[min(initial_station_idx, final_station_idx):max(initial_station_idx, final_station_idx)])
        stations_passed = abs(final_station_idx - initial_station_idx)
        
        total_distance += distance
        total_fare += fare
        total_stations_passed += stations_passed

        print(f"\nʚ Stations traveled: {stations[initial_station_idx]} -> {stations[final_station_idx]}")
        print(f"ʚ Distance Traveled for this ride: {distance:.2f} km")
        print(f"ʚ Fare for this ride: PHP {fare:.2f}")
        print(f"\n» You have arrived at {stations[final_station_idx]} station.")
        print("\n﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌")

        ride_again = input("\n♡ Do you want to ride again? (yes/no): ").strip().lower()
        if ride_again != 'yes':
            print(f"\nʚ Total Distance Traveled: {total_distance:.2f} km")
            print(f"ʚ Total Stations Passed: {total_stations_passed} stations")
            print(f"ʚ Total Fare: PHP {total_fare:.2f}")
            print("\n♡ Thank you for riding! ♡")
            break

        initial_station_idx = final_station_idx
        print(f"\n» You are currently at {stations[initial_station_idx]} station.")

if __name__ == "__main__":
    main()