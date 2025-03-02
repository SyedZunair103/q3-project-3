def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "meter": 1, "kilometer": 0.001, "centimeter": 100, "mile": 0.000621371, "yard": 1.09361, "foot": 3.28084
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        "kilogram": 1, "gram": 1000, "pound": 2.20462, "ounce": 35.274
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    else:
        return "Invalid Conversion"