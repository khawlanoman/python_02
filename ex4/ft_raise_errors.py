def check_plant_health(plant_name, water_level, sunlight_hours) -> None:
    if (plant_name == ""):
        print("\nTesting empty plant name...")
        raise ValueError("Plant name cannot be empty!\n")
    elif (water_level < 1 or water_level > 10):
        print("\nTesting bad water level...")
        raise ValueError(f"Water level {water_level} is too high (max 10)\n")
    elif (sunlight_hours < 2 or sunlight_hours > 12):
        print("\nTesting bad sunlight hours...")
        raise ValueError(
            f"Sunlight hours {sunlight_hours}"
            " is too low (min 2)\n"
            )
    elif (plant_name != ""):
        print("\nTesting good values...")
        print("Plant 'tomato' is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    try:
        check_plant_health("tomato", 1, 10)
    except ValueError as error:
        print(f"Error: {error}")

    try:
        check_plant_health("", 1, 10)
    except ValueError as error:
        print(f"Error: {error}")

    try:
        check_plant_health("tomato", 15, 10)
    except ValueError as error:
        print(f"Error: {error}")

    try:
        check_plant_health("tomato", 1, 0)
    except ValueError as error:
        print(f"Error: {error}")

    print("\nAll error raising tests completed!")


test_plant_checks()
