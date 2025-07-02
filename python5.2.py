total = 100
set_size = 10

for completed in range(set_size, total+1, set_size):
    print(f"You have completed {completed} jumping jacks.")

    if completed == total:
       print("Congratulations! You completed the workout.")
       break

    tired = input("Are you tired? (yes/no): ").strip().lower()

    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break
        else:
            print(f"{total-completed} jumping jacks remaining.")
    else:
        print(f"{total - completed} jumping jacks remaining.")
