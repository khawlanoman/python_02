def  water_plants(plant_list):
    plant_list
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise 
            print(f"Watering {plant}")
    except:
         print(f"Error: Cannot water {plant} - invalid plant!")
    print("Closing watering system (cleanup)")


def test_watering_system():
    plant_list={"tomato","lettuce","carrots"}
    print("Testing normal watering...")
   
    try:
        water_plants(plant_list)
        print("Watering completed successfully!")
    except:
        print("Error")
   
    print("\nTesting normal watering...")
    try:
        plant_list_error={"tomato",None,"carrots"}
        water_plants(plant_list_error)

    finally:
        print("\nCleanup always happens, even with errors!")

test_watering_system()