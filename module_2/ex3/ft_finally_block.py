def watering_system(plants: list):

    print("Opening water system")
    try:
        for i in range(len(plants)):
            if plants[i] is None:
                raise ValueError("Error: Cannot water None - invalid plant!")
            else:
                print(f"Watering {plants[i]}")
        print("Watering completed successfully!")

    except ValueError as ve:
        print(ve)

    finally:
        print("Closing watering system (cleanup)")


def main():
    print("=== Garden Watering System ===")

    plants_correct = ["tomato", "lettuce", "carrots"]
    plants_error = ["tomato", None]

    print("\nTesting normal watering...")
    watering_system(plants_correct)

    print("\nTesting with error...")
    watering_system(plants_error)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
