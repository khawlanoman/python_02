class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def error_plant() -> None:
    plant = "tomato"

    if (plant != "banana"):
        raise PlantError("The tomato plant is wilting")


def error_water():
    water = 0
    if (water != 1):
        raise WaterError("Not enough water in the tank!")


def handle_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        error_plant()
    except PlantError as error:
        print(f"Caught PlantError:{error}")

    print("\nTesting WaterError...")
    try:
        error_water()
    except WaterError as error:
        print(f"Caught PlantError:{error}")
    print("\nTesting catching all garden errors...")
    try:
        error_plant()
    except PlantError as error:
        print(f"Caught PlantError:{error}")

    try:
        error_water()
    except WaterError as error:
        print(f"Caught PlantError:{error}")

    print("\nAll custom error types work correctly!")


handle_errors()
