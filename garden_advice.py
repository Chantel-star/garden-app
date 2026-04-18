# Hardcoded values for the season and plant type
season = "summer"  # TODO: Replace with input() to allow user interaction.
plant_type = "flower"  # TODO: Replace with input() to allow user interaction.

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
def get_season_advice(season):
    """Return gardening advice based on the season."""
    if season == "summer":
        return "Water your plants regularly and provide some shade."
    elif season == "winter":
        return "Protect your plants from frost with covers."
    else:
        return "No advice for this season."

# Determine advice based on the plant type
def get_plant_advice(plant_type):
    """Return gardening advice based on plant type."""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."

season = "summer"
plant_type = "flower"

season_advice = get_season_advice(season)
plant_advice = get_plant_advice(plant_type)

# Print the generated advice
print(season_advice)
print(plant_advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
