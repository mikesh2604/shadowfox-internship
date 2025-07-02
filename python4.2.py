#to determine which country a city belongs to
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name:")

if city in Australia:
  print(f"{city} is in Australia")
elif city in UAE:
  print(f"{city} is in UAE")
elif city in India:
  print(f"{city} is in India")
else:
  print(f"{city} is not in the list")