def display_menu():
    print("Fitness Tracker Menu")
    print("1. Add activity")
    print("2. View statistics")
    print("3. Exit")

def add_activity(fitness_log):
    activity = input("Enter the activity (e.g., Running, Cycling, etc.): ")
    distance = float(input("Enter the distance covered (in km): "))
    duration = float(input("Enter the duration (in minutes): "))
    calories = float(input("Enter the calories burned: "))

    fitness_log.append({
        "activity": activity,
        "distance": distance,
        "duration": duration,
        "calories": calories
    })

    print(f"Added {activity} with {distance:.1f} km, {duration:.1f} minutes, and {calories:.1f} calories burned.\n")

def view_statistics(fitness_log):
    if not fitness_log:
        print("No data available.\n")
        return

    total_distance = sum(activity['distance'] for activity in fitness_log)
    total_duration = sum(activity['duration'] for activity in fitness_log)
    total_calories = sum(activity['calories'] for activity in fitness_log)

    print("\nStatistics:")
    print(f"Total distance covered: {total_distance:.1f} km")
    print(f"Total duration: {total_duration:.1f} minutes")
    print(f"Total calories burned: {total_calories:.1f} calories\n")

def main():
    fitness_log = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_activity(fitness_log)
        elif choice == "2":
            view_statistics(fitness_log)
        elif choice == "3":
            print("Exiting Fitness Tracker. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if _name_ == "_main_":
    main()
