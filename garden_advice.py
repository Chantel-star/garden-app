"""
Garden Advice Application

This program gives gardening advice based on:
- the season
- the plant type
"""

# Determines advice based on the season
def get_season_advice(season):
    """Return gardening advice based on the season."""
    if season == "summer":
        return "Water your plants regularly and provide some shade."
    elif season == "winter":
        return "Protect your plants from frost with covers."
    else:
        return "No advice for this season."

# Determines advice based on the plant type
def get_plant_advice(plant_type):
    """Return gardening advice based on plant type."""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."

season = input("Enter the season: ").strip().lower()
plant_type =  input("Enter the plant type: ").strip().lower()

season_advice = get_season_advice(season)
plant_advice = get_plant_advice(plant_type)

# Print the generated advice
print("\nGardening Advice:")
print(get_season_advice(season))
print(get_plant_advice(plant_type))

