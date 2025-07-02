#to check if two cities belong to the same country or not

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "chennai", "Delhi"]

city1 = input("Enter the first city:")
city2 = input("Enter the second city:")
if city1 in Australia:
  country1 = "Australia"
elif city1 in UAE: 
  country1 = "UAE"
elif city1 in India:
  country1 = "India"
else:
  country1 = "none"
if city2 in Australia:
  country2 = "Australia"
elif city2 in UAE:
  country2 = "UAE"
elif city2 in India:
  country2 = "India"
else:
 country1 = "none"
if country1 == country2:
  print(f"Both cities are in same country {country1}")
else:
  print(f"They don't belong to the same country")