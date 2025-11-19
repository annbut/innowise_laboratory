"""Mini-profile generator CLI script."""

CURRENT_YEAR = 2025


def generate_profile(age: int) -> str:
    """Return a string describing the life stage for a given age.

    Rules:
        - If age is between 0 and 12 (inclusive), return "Child".
        - If age is between 13 and 19 (inclusive), return "Teenager".
        - If age is 20 or older, return "Adult".

    Args:
        age: User's age in full years.

    Returns:
        Life stage description: "Child", "Teenager", or "Adult".
    """
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"


def main() -> None:
    """Run the interactive mini-profile generator."""
    # 1. Get basic user input.
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")

    # Convert birth year to integer and calculate current age.
    birth_year = int(birth_year_str)
    current_age = CURRENT_YEAR - birth_year

    # 2. Gather hobbies until the user types 'stop' (case-insensitive).
    hobbies: list[str] = []
    while True:
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ")

        # Stop collecting hobbies if user enters 'stop' in any case.
        if hobby.lower() == "stop":
            break

        hobbies.append(hobby)

    # 3. Process and generate the profile.
    life_stage = generate_profile(current_age)

    user_profile = {
        "name": user_name,
        "age": current_age,
        "stage": life_stage,
        "hobbies": hobbies,
    }

    # 4. Display the output in a clean, well-formatted summary.
    print("\n---")
    print("Profile Summary:")
    print(f"Name: {user_profile['name']}")
    print(f"Age: {user_profile['age']}")
    print(f"Life Stage: {user_profile['stage']}")

    if user_profile["hobbies"]:
        print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
        for hobby in user_profile["hobbies"]:
            print(f"- {hobby}")
    else:
        print("You didn't mention any hobbies.")
    print("---")


if __name__ == "__main__":
    main()
