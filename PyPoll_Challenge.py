# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# --- Start of Challenge Code Section, Part 1 of 3--- 

# County options and county votes, creating a dictionary
# where the county is the key and the votes cast for each
# county in the election are the values. 
county_options = []
county_votes = {}

# Creating an empty string that will hold the county name
# that had the largest amount. Tracking largest county, 
# vote count, and percentage. 
largest_turnout_county = ""
county_count = 0 
county_percentage = 0

# --- End of Challenge Code Section --- 


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# --- Start of Challenge Code Section, Part 2 of 3 --- 

        # --- Collecting County Votes ---

        # Get county name from each row. 
        county_name = row[1]

        # Creating list of counties. If the county does not match any 
        # existing county, add it to the county list. 
        if county_name not in county_options:

            # Add the county name to the county list.
            county_options.append(county_name)

            # Start tracking the county voter count. 
            county_votes[county_name] = 0

        # Adding a vote to the county's count.
        county_votes[county_name] += 1

# --- End of Challenge Code Section --- 

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

# --- Start of Challenge Code Section, Part 3 of 3 --- 

    # --- Printing County Results --- 

    # Printing header in both Terminal and in text file.
    print("County Votes:\n")
    txt_file.write("\nCounty Votes:\n")

    # Calculating and printing county turnout. 
    for county in county_votes: 

        # Get county vote count and percentage.
        turnout_votes = county_votes[county]
        turnout_vote_percentage = float(turnout_votes) / float(total_votes) * 100

        # Printing each county, voter count, and percentage to 
        # the terminal. 
        county_results = (f"{county}: {turnout_vote_percentage:.1f}% ({turnout_votes:,})\n")
        print(county_results)

        # Saving county results to text file. 
        txt_file.write(county_results)

        # Determining county with largest turnout. 
        # Determine winning vote count, winning percentage, and candidate.
        if (turnout_votes > county_count) and (turnout_vote_percentage > county_percentage):
            county_count = turnout_votes
            largest_turnout_county = county
            county_percentage = turnout_vote_percentage

    # Printing the largest county turnout results to the terminal.
    largest_turnout_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_turnout_county}\n"
        f"-------------------------\n")

    print(largest_turnout_summary)

    # Saving largest county turnout to the text file.
    txt_file.write(largest_turnout_summary)

# --- End of Challenge Code Section --- 

    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the
        # terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)