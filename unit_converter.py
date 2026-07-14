conversions = {
    "Länge": {
        ("m", "yd"): lambda x: x * 1.094,
        ("yd", "m"): lambda x: x / 1.094,
    },
    "Gewicht": {
        ("kg", "lbs"): lambda x: x * 2.205,
        ("lbs", "kg"): lambda x: x / 2.205,
    },
    "Temperatur": {
        ("°C", "°F"): lambda x: (x * (9 / 5)) + 32,
        ("°F", "°C"): lambda x: (x - 32) * (5 / 9),
    },
    
}
while True:
    conversion_type = input("Gib die Art der Umrechnug ein! (Gewicht, Länge, Temperatur)")
    unit_input = input("Welche Einheit möchtest du umrechnen? (kg, lbs, m, yd, °C, °F)")
    unit_output = input("In welche Einheit möchtest du umrechnen? (kg, lbs, m, yd, °C, °F)")
    value = float(input("Gib den Wert ein der Umgerechnet werden soll!"))

    output = conversions[conversion_type][(unit_input, unit_output)](value)
    print(f"{value} {unit_input} = {output} {unit_output}")