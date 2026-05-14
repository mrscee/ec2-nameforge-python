# Several departments share this AWS environment.
# This name generator will be used to ensure that the EC2s are uniquely named, 
# so team members can easily tell who the instances belong to.
# The only departments that should use this Name Generator are the Marketing, Accounting, and FinOps.

# EC2 Random Name Generator 


# Which departments are allowed?
allowed_departments = ["marketing", "accounting", "finops"]

# Ask the user for their department.
department = input("Please enter your department name: ")

# Allow for uppercase and lowercase variations.
department = department.lower()

# Print specific reply based on if department entered is allowed to use the generator
if department in allowed_departments:
    print(f"\nThe {department.capitalize()} department is approved to use this generator.\n")


    ###### After department vetting, keep this section indented to finish the approved process.

    # Import Python's random library so the program can randomly choose letters and numbers. 
    # In the future, note that imports are usually placed at the top of code file
    import random

    # Ask the approved user how many EC2 instance names they need.
    # The int() function converts the user's answer from text into a whole number.
    number_of_instances = int(input(f"How many unique EC2 instance names do you need for the {department.capitalize()} department? "))

    # Create a string of letters and numbers that Python can randomly choose from.
    # These characters will be used to create the unique ending for each EC2 name.
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # Print a heading before showing the generated EC2 names.
    print("\nPlease find below requested EC2 name(s):\n")

    # This loop runs once for each EC2 instance name the user requested.
    # Example: If the user enters 3, this loop will run 3 times.
    for instance in range(number_of_instances):

        # Start with an empty random_part for each new EC2 name.
        # This prevents the random characters from the previous name from carrying over.
        random_part = ""

        # This nested loop runs 5 times to create a 5-character random ending.
        for i in range(5):

            # Each time the loop runs, randomly choose one character and add it to random_part.
            random_part = random_part + random.choice(characters)

        # Print the completed EC2 name using the department name, EC2 label, and random ending.
        print(f"{department.upper()}-EC2-{random_part}")
    print("\n")


else:
    print(f"\nThe {department.capitalize()} department is NOT APPROVED to use this EC2 name generator.")

    # Additional reiteration for the unapproved departments:
    print("\nThe only departments APPROVED to use this EC2 name generator are Marketing, Accounting and FinOps.\n")
