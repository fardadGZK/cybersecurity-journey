length_units = {"m": 1, "km": 1000, "cm": 0.01, "mm": 0.001, "mile": 1609.34, "foot": 0.3048, "inch": 0.0254}
weight_units = {"g": 1, "kg": 1000, "mg": 0.001, "lb": 453.592, "oz": 28.3495}
temperature_units = ("c", "f", "k")

def length(number, from_unit, to_unit):
    meters = number * length_units[from_unit]
    result = meters / length_units[to_unit]
    return result

def weight(number, from_unit, to_unit):
    grams = number * weight_units[from_unit]
    result = grams / weight_units[to_unit]
    return result

def temperature(number, from_unit, to_unit):
    if from_unit == "f":
        celsius = (number - 32) * 5/9
    elif from_unit == "k":
        celsius = number - 273.15
    elif from_unit == "c":
        celsius = number

    if to_unit == "c":
        result = celsius
    elif to_unit == "f":
        result = celsius * 9/5 + 32
    elif to_unit == "k":
        result = celsius + 273.15

    return result


while True:
    choice = input("What do you want to convert: ").lower()

    if choice not in ("length", "weight", "temp"):
        print("Invalid conversion type!")
        continue

    while True:
        try:
            number = float(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        from_unit = input("Convert from: ").lower()
        to_unit = input("Convert to: ").lower()

        if choice == "length":
            if from_unit in length_units and to_unit in length_units:
                break
            else:
                print("Invalid length unit!")
        elif choice == "weight":
            if from_unit in weight_units and to_unit in weight_units:
                break
            else:
                print("Invalid weight unit!")
        elif choice == "temp":
            if from_unit in temperature_units and to_unit in temperature_units:
                break
            else:
                print("Invalid temperature unit!")

    if choice == "length":
        result = length(number, from_unit, to_unit)
        print(f"{number:g} {from_unit} = {result:g} {to_unit}")

    elif choice == "weight":
        result = weight(number, from_unit, to_unit)
        print(f"{number:g} {from_unit} = {result:g} {to_unit}")

    elif choice == "temp":
        result = temperature(number, from_unit, to_unit)
        if result is not None:
            print(f"{number:g} {from_unit} = {result:g} {to_unit}")

    again = input("Do you want to convert again? ").lower()
    if again == "no":
        break