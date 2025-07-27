# Election candidates
candidates = {
    "1": "Candidate A",
    "2": "Candidate B",
    "3": "Candidate C"
}

# Voting data storage
votes = {
    "Candidate A": 0,
    "Candidate B": 0,
    "Candidate C": 0
}

# Function to display candidates
def show_candidates():
    print("\n--- Election Candidates ---")
    for key, value in candidates.items():
        print(f"{key}. {value}")
    print()

# Function to cast vote
def cast_vote():
    while True:
        show_candidates()
        choice = input("Enter the number of the candidate you want to vote for (or 'exit' to stop): ")

        if choice == 'exit':
            print("\nExiting the election booth. Thank you!")
            break
        
        if choice in candidates:
            voted_for = candidates[choice]
            votes[voted_for] += 1
            print(f"Your vote has been successfully cast for {voted_for}.\n")
        else:
            print("Invalid choice, please select a valid candidate or type 'exit' to stop.\n")

# Function to display results
def display_results():
    print("\n--- Election Results ---")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")
    print()

# Main program loop
def election_booth():
    print("Welcome to the Election Booth!")

    while True:
        print("\n1. Cast a vote")
        print("2. View Election Results")
        print("3. Exit")
        
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\nInvalid input! Please enter a number between 1 and 3.")
            continue
        
        if choice == 1:
            cast_vote()
        elif choice == 2:
            display_results()
        elif choice == 3:
            print("\nThank you for visiting the Election Booth!")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.")

# Running the program
if __name__ == "__main__":
    election_booth()
