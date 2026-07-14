"""

JEBISHA THAPA
"""



# temperature
def farenheit_to_celsius(farenheit: float):
    
    """
    Converts a temperature measurement from farenheit to celsius.

    Parameters:
    farenheit(float): Temperature in farenheit

    Returns:
    float: Temperature in celsius


    """
    celsius = (farenheit - 32)* 5 / 9
    return celsius

def celsius_to_farenheit(celsius: float):
    """
    Converts a temperature measurement from celsius to farenheit.

    Parameters:
    celsius(float): Temperature in celsius

    Returns:
    float: Temperature in farenheit

     """
    
    farenheit = (celsius * 1.8) + 32

    return farenheit


def celsius_to_kelvin(celsius: float):
    """
    Converts a temperature measurement from celsius to kelvin.

    Parameters:
    farenheit(float): Temperature in celsius

    Returns:
    float: Temperature in kelvin

     """
    
    kelvin = celsius + 273.15

    return kelvin


def farenheit_to_kelvin(farenheit: float):
    """
    Converts a temperature measurement from farenheit to kelvin.

    Parameters:
    farenheit(float): Temperature in ferenheit

    Returns:
    float: Temperature in kelvin

     """
    
    kelvin = ((farenheit - 32) /1.8) + 273.15

    return kelvin

def kelvin_to_celsius(kelvin: float):
    """
    Converts a temperature measurement from kelvin to celsius.

    Parameters:
    kelvin(float): Temperature in kelvin

    Returns:
    float: Temperature in celsius

     """
    
    celsius = kelvin - 273.15

    return celsius

def kelvin_to_fahrenheit(kelvin: float):
    """
    Converts a temperature measurement from kelvin to fahrenheit.

    Parameters:
    kelvin(float): Temperature in kelvin

    Returns:
    float: Temperature in fahrenheit

     """
    
    fahrenheit = (kelvin  - 273.15) * 1.8 + 32

    return fahrenheit


#distance

def kilometer_to_meter(kilometer:float):
    """
    Converts a distance measurement from Kilometers to meter.

    Parameters:
    kilometer (float): Distance in kilometer..

    Returns:
    float: Distance in meters.

    """

    meter = kilometer * 1000

    return meter

def meter_to_kilometer(meter:float):
    """
    Converts a distance measurement from meter to Kilometer.

    Parameters:
    meter (float): Distance in meter.

    Returns:
    float: Distance in kilometers.

    """

    kilometer = meter / 1000

    return kilometer

def miles_to_kilometers(miles: float) :
    """
    Converts a distance measurement from Miles to Kilometers.

    Parameters:
    miles (float): Distance in miles.

    Returns:
    float: Distance in kilometers.
    """
    kilometer = miles * 1.60934
    return kilometer


def kilometers_to_miles(kilometers: float) :
    """
    Converts a distance measurement from Miles to Kilometers.

    Parameters:
    miles (float): Distance in miles.

    Returns:
    float: Distance in kilometers.
    """
    miles= kilometers / 1.60934

    return miles

def meter_to_foot(meter:float) -> float:
    """
    Converts Meter into Foot

    Parameters:
        meter: Distance in meters.
    
    Returns:
        float: distance in feet.
    """
    foot = meter * 3.281

    return foot

def foot_to_meter(foot:float) -> float:
    """
    Converts Foot into Meter

    Parameters:
        foot: Distance measure in feet.
    
    Returns:
        float: distance in meters.
    """
    meter = foot / 3.281

    return meter


def pounds_to_kilograms(pounds: float):
    """
    Converts a mass/weight measurement from Pounds (lbs) to Kilograms (kg).

    Parameters:
    pounds (float): Weight in pounds.

    Returns:
    float: Weight in kilograms.
    """
    kilograms = pounds * 0.45359237

    return kilograms

def kilograms_to_pounds(kilograms: float):
    """
    Converts a mass/weight measurement from Kilograms to pounds..

    Parameters:
    kilograms(float): Weight in kilogram.

    Returns:
    float: Weight in pounds.
    """
    pounds = kilograms * 2.20462262

    return pounds


#menus
while True:

    print("\nMAIN MENU")
    print("1. Temperature")
    print("2. Distance")
    print("3. Weight")
    print("4. Exit")

    category = input("Enter what do you want to convert: ")

    if category == "1":

        print("\nTEMPERATURE")
        print("1. Fahrenheit → Celsius")
        print("2. Celsius → Fahrenheit")
        print("3. Celsius → Kelvin")
        print("4. Fahrenheit → Kelvin")
        print("5. Kelvin → Celsius")
        print("6. Kelvin → Fahrenheit")

        choice = input("Choose conversion: ")

        value = float(input("Enter value: "))

        if choice == "1":
            result = farenheit_to_celsius(value)

        elif choice == "2":
            result = celsius_to_farenheit(value)

        elif choice == "3":
            result = celsius_to_kelvin(value)

        elif choice == "4":
            result = farenheit_to_kelvin(value)

        elif choice == "5":
            result = kelvin_to_celsius(value)

        elif choice == "6":
            result = kelvin_to_fahrenheit(value)

        else:
            print("Invalid choice")
            continue

        print("Result:", result)

    elif category == "2":

        print("\nDISTANCE")
        print("1. Miles → Kilometers")
        print("2. Kilometers → Miles")
        print("3. Meter → Foot")
        print("4. Foot → Meter")
    

        choice = input("Choose conversion: ")

        value = float(input("Enter value: "))

        if choice == "1":
            result = miles_to_kilometers(value)

        elif choice == "2":
            result = kilometers_to_miles(value)

        elif choice == "3":
            result = meter_to_foot(value)

        elif choice == "4":
            result = foot_to_meter(value)

        else:
            print("Invalid choice")
            continue

        print("Result:", result)

    elif category == "3":

        print("\nWEIGHT")
        print("1. Pounds → Kilograms")
        print("2. Kilograms → Pounds")

        choice = input("Choose conversion: ")

        value = float(input("Enter value: "))

        if choice == "1":
            result = pounds_to_kilograms(value)

        elif choice == "2":
            result = kilograms_to_pounds(value)

        else:
            print("Invalid choice")
            continue

        print("Result:", result)

    elif category == "4":
        break

    else:
        print("Invalid menu choice")