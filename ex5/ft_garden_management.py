class GardenManager():
    def __init__(self):
        self.plants=[]

    def add_plants(self,plant_name)->None:
        if (plant_name == ""):
            raise ValueError("Plant name cannot be empty!\n")
      
        self.plants +=[plant_name]
        print(f"Added {plant_name} successfully")

    def water_plants(self)->None:
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")
    
    def check_plant_health(self,plant_name,water,sun):
        if (water < 1  or water > 10):
            raise ValueError(f"{plant_name}: Water level {water} is too high (max 10)\n")
        if (sun < 2 or sun > 12):
            raise ValueError(f"Sunlight hours {sun} is too low (min 2)\n")
        print(f"{plant_name}: healthy (water: {water}, sun: {sun})")

def test_garden_management()->None:
    garden = GardenManager()

    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    try:
        garden.add_plants("tomato")
        garden.add_plants("lettuce")
        garden.add_plants("")
    except ValueError as error:
        print(f"Error adding plant:{error}\n")

    print("Watering plants...")
    print("Opening watering system")
    garden.water_plants()

    print("\nChecking plant health...")
    try:
        garden.check_plant_health("tomato",5,8)
        garden.check_plant_health("tomato",15,8)
    except ValueError as error :
        print(f"Error checking {error}\n")

    print("Testing error recovery...")
    garden.water_plants()
    print("System recovered and continuing...")

    print("\nGarden management system test complete!")
test_garden_management()