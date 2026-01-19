def water_plants(plant_list) -> None:
    plant_list
    print("Opening watering system")

    for plant in plant_list:
        if plant is None:
            raise ValueError(f"Cannot water {plant} - invalid plant!")
        print(f"Watering {plant}")
    print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    plant_list = ["tomato", "lettuce", "carrots"]
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")

    try:
        water_plants(plant_list)
        print("Watering completed successfully!")
    except ValueError as error:
        print(f"Error : {error}")

    print("\nTesting with error...")
    plant_list_error = ["tomato", None, "carrots"]
    try:
        water_plants(plant_list_error)
    except ValueError as error:
        print(f"Error : {error}")

    finally:
        print("Closing watering system (cleanup)\n")
        print("\nCleanup always happens, even with errors!")


test_watering_system()
