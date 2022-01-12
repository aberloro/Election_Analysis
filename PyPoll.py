# Add python dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote accumulator
total_votes = 0 

# declare candidates list and candidate votes dictionary
candidate_options = []
candidate_votes = {}

# declare counties list and counties votes dictionary
counties_list = []
counties_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county and county voter turnout.
largest_county = " "
largest_county_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote accumulator
        total_votes += 1

        #print candidate name and county name from each row
        candidate_name = row[2]
        county_name = row[1]

        # if candidate does not match existing candidate
        if candidate_name not in candidate_options:
            
            # add candidate name to candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

        # if county name does not match existing county in county list 
        if county_name not in counties_list:
            
            # add existing county to list of counties
            counties_list.append(county_name)

            #begin tracking the county's vote accumulator
            counties_votes[county_name]=0

        #add a vote to that county's vote accumulator
        counties_votes[county_name] += 1

# Save results to the text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------\n"
        f"\nCounty Votes: \n")
    
    #print to terminal
    print(election_results, end="")

    #save election vote results to text file
    txt_file.write(election_results)

    # get county from counties dictionary
    for county_name in counties_votes:

        #retrieve county vote count
        county_vote = counties_votes[county_name]

        #6c calc percent of votes for the county
        county_percent = float(county_vote) / float(total_votes) *100 

        #6d print county results to terminal
        county_results  =(f"{county_name}: {county_percent:.1f}% ({county_vote:,})\n")
        print (county_results)

        #6e save county votes to text file
        txt_file.write(county_results)

        #6f use IF to determine the winning county and its vote county
        if county_vote > largest_county_votes:
            #if true then set largest_county_votes = county_vote
            largest_county_votes = county_vote
            # and set largest county = county name
            largest_county = county_name

    print(f"\n------------------------------ \n"
            f"Largest County Turnout: {largest_county} \n "
            f"------------------------------ \n " )
    txt_file.write(f"\n------------------------------ \n"
            f"Largest County Turnout: {largest_county}\n"
            f"------------------------------ " )

    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        candidate_results =(f"\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})")
        
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
        f"\n------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n")
    print(winning_candidate_summary)
    
    # Save winning candidate's name to text file
    txt_file.write(winning_candidate_summary)