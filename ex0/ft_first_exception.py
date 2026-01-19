def check_temperature(temp_str) -> None:
    try:
        temp = int(temp_str)
    except Exception:
        print(f"Error:'{temp_str}' is not a valid number")
        return
    if (temp < 0):
        print(f"Error:{temp}°C is too cold for plants (min 0°C)")
    elif (temp > 40):
        print(f"Error:{temp}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {temp}°C is perfect for plants!")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print("\n")

    arr = ["25", "abc", "100", "-50"]
    for i in arr:
        print(f"Testing temperature: {i}")
        check_temperature(i)
        print("\n")

    print("All tests completed - program didn't crash!")


test_temperature_input()
