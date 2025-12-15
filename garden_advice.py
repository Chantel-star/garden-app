"""
Garden Advice Application
-------------------------
This program gives gardening advice based on:
1. The user's selected season
2. The user's selected plant type

Features:
- Uses functions for better structure and readability.
- Stores advice in dictionaries, making it easy to update or extend.
- Includes a plant recommendation system for each season.
"""

def get_season_advice(season):
    """
    Returns gardening advice based on the given season.
    """
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.",
        "winter": "Protect your plants from frost with covers.",
        "spring": "Start planting new seeds and prepare soil.",
        "autumn": "Rake leaves and prepare plants for the colder months."
    }
    return season_advice.get(season.lower(), "No advice available for this season.")


def get_plant_advice(plant_type):
    """
    Returns gardening advice based on the plant type.
    """
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
        "herb": "Trim regularly to encourage new growth."
    }
    return plant_advice.get(plant_type.lower(), "No advice available for this plant type.")


def get_recommended_plants(season):
    """
    Returns a list of recommended plants for the given season.
    """
    recommendations = {
        "summer": ["Sunflowers", "Tomatoes", "Lavender"],
        "winter": ["Kale", "Winter Cabbage", "Pansies"],
        "spring": ["Daisies", "Carrots", "Mint"],
        "autumn": ["Pumpkins", "Chrysanthemums", "Spinach"]
    }
    return recommendations.get(season.lower(), [])


def main():
    """
    Main program logic:
    - Asks the user for inputs.
    - Generates advice.
    - Displays recommendations.
    """
    # User input for season and plant type
    season = input("Enter the current season (summer, winter, spring, autumn): ")
    plant_type = input("Enter your plant type (flower, vegetable, herb): ")

    # Gather advice
    advice = get_season_advice(season) + "\n" + get_plant_advice(plant_type)

    # Display advice
    print("\n--- Gardening Advice ---")
    print(advice)

    # Show recommended plants
    recommended = get_recommended_plants(season)
    if recommended:
        print("\nRecommended plants for this season:")
        for plant in recommended:
            print(f" - {plant}")
    else:
        print("\nNo plant recommendations for this season.")


# Run the program
if __name__ == "__main__":
    main()

