# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0 
# declare new list for candidates
candidate_options = []
# Declare an empty dictionary
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        #print candidate name from each row
        candidate_name = row[2]

        # if candidate does not match existing candidate
        if candidate_name not in candidate_options:
            
            # add candidate name to candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

# Save results to our text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------\n")
    #print to terminal
    print(election_results, end="")

    #save final vote to text file
    txt_file.write(election_results)

    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        candidate_results =(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # print each candidate name, votes, percent votes to terminal
        print(candidate_results)

        # Save candidate results to our text file
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        if(votes>winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning_count = votes and winning_percent =vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # and set winning candidate = candidate's name
            winning_candidate = candidate_name

    # print winning candidate's results to terminal
    winning_candidate_summary = (
        f"------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n")
    print(winning_candidate_summary)
    
    # Save winning candidate's name to text file
    txt_file.write(winning_candidate_summary)