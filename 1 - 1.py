def temperature_converter(temperature):
  fahrenheit = (temperature*(9/5) + 32)
  return fahrenheit


graus = float(input("Temperatura em C°: "))
fahrenheit = temperature_converter(graus)
print(f"{graus}° em Fahrenheit é {fahrenheit}°F")
