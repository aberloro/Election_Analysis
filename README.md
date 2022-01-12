# Election_Analysis

## Overview of Election Audit
Client from Colorado Board of Elections has asked for an election audit of a local congressional election with the intent to scale the code to use in other elections as well.  The deliverables are listed below:

1. Total number of votes cast
2. Total number and percent of votes for each county
3. County with the highest voter turnout
4. Total number of votes and percentage of votes per candidate
5. Winner of election based on popular vote

## Resources
 - Data Source: election_results.csv
 - Software: Python 3.7, Visual Studio Code

## Election Audit Results
### Colorado Election Analysis 
The analysis of the election results show that:
1. Total Votes: 369,711
2. The county results were
   - Jefferson: 10.5% (38,855)
   - Denver: 82.8% (306,055)
   - Arapahoe: 6.7% (24,801)
3. The county with the most votes was Denver. 
4. The candidate results were
   - Charles Casper Stockham: 23.0% (85,213)
   - Diana DeGette: 73.8% (272,892)
   - Raymon Anthony Doane: 3.1% (11,606)
5. The Winner of the election was
   - Diana DeGette with a total of 272,892 votes at 73.8% of the total vote.

### Overview of Code

The first step is to import two dependencies, or pre-written software code, from Python.  The CVS module will help us read the CSV file containing the raw election data, and the OS module will help python interact with our computer's operating system, specifically to help locate files.

     #Add python dependencies
     import csv
     import os

Next, assign variables to load the raw CVS file and to save the text file we create.  You'll tell python where to find these files via their path in this step as well.

     #Assign a variable to load a file from a path.
     file_to_load = os.path.join("Resources", "election_results.csv")
     #Assign a variable to save the file to a path.
     file_to_save = os.path.join("Analysis", "election_analysis.txt")

Now that python knows how to get the data and where to send our analysis results, we need to set up variables to hold the data we are looking for.

     #Initialize a total vote accumulator
     total_votes = 0 

     #Declare candidates list and candidate votes dictionary
     candidate_options = []
     candidate_votes = {}

     #Declare counties list and counties votes dictionary
     counties_list = []
     counties_votes = {}

     #Track the winning candidate, vote count, and percentage.
     winning_candidate = ""
     winning_count = 0
     winning_percentage = 0

     #Track the largest county and county voter turnout.
     largest_county = " "
     largest_county_votes = 0

With our variables, lists, and dictionaries ready to store data, we can open the election results CVS file and ask pyhton to read it row by row.  As python is reading each row, it will plug useful data into the variables we established.

     #Open the election results and read the file.
     with open(file_to_load) as election_data:
         file_reader = csv.reader(election_data)

         #Read the header row.
         headers = next(file_reader)

         #Print each row in the CSV file.
         for row in file_reader:
             # Add to the total vote accumulator
             total_votes += 1

             #Store candidate name and county name from each row
             candidate_name = row[2]
             county_name = row[1]

             #If candidate does not match existing candidate
             if candidate_name not in candidate_options:

                 #Add candidate name to candidate list
                 candidate_options.append(candidate_name)

                 #Begin tracking that candidate's vote count.
                 candidate_votes[candidate_name] = 0

             #Add a vote to that candidate's count
             candidate_votes[candidate_name] +=1

             #If county name does not match existing county in county list 
             if county_name not in counties_list:

                 #Add existing county to list of counties
                 counties_list.append(county_name)

                 #Begin tracking the county's vote accumulator
                 counties_votes[county_name]=0

             #Add a vote to that county's vote accumulator
             counties_votes[county_name] += 1

Now that there is election data stored (temporirily) in our variables, we need to write that data to the txt file so we may save it, and to the terminal so we may view it. 

     #Save results to the text file
     with open(file_to_save, "w") as txt_file:
         election_results = (
             f"\nElection Results\n"
             f"------------------------------\n"
             f"Total Votes: {total_votes:,}\n"
             f"------------------------------\n"
             f"\nCounty Votes: \n")

         #Print to terminal
         print(election_results, end="")

         #Save election vote results to text file
         txt_file.write(election_results)

The next step is to look at our counties dictionary, which has been storing the voter turnout for each county, to determine which county had the best turnout. The keys are the county names, and the value associated with each key is the number of votes cast in that county. 

         #Get county from counties dictionary
         for county_name in counties_votes:

             #Retrieve county vote count
             county_vote = counties_votes[county_name]

             #Calculate percent of votes for the county
             county_percent = float(county_vote) / float(total_votes) *100 

             #Print county results to terminal
             county_results  =(f"{county_name}: {county_percent:.1f}% ({county_vote:,})\n")
             print (county_results)

             #Save county votes to text file
             txt_file.write(county_results)

             #Use IF to determine the winning county and its vote county
             if county_vote > largest_county_votes:
                 #if true then set largest_county_votes = county_vote
                 largest_county_votes = county_vote
                 # and set largest county = county name
                 largest_county = county_name

Then print the county turn out information to the terminal and to the text file. 

         print(f"\n------------------------------ \n"
                 f"Largest County Turnout: {largest_county} \n "
                 f"------------------------------ \n " )
         txt_file.write(f"\n------------------------------ \n"
                 f"Largest County Turnout: {largest_county}\n"
                 f"------------------------------ " )

Pull candidate names and votes from the candidate votes dictionary. The keys are candidate names, and the values are the number of votes. Print this info to the terminal and txt file. 

         #Iterate through the candidate list.
         for candidate_name in candidate_votes:

             #Retrieve vote count of a candidate.
             votes = candidate_votes[candidate_name]

             #Calculate the percentage of votes.
             vote_percentage = float(votes) / float(total_votes) * 100

             candidate_results =(f"\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})")

             #Print each candidate name, votes, percent votes to terminal
             print(candidate_results)

             #Save candidate results to our text file
             txt_file.write(candidate_results)

Use an IF conditional statement to evlauate which candidate had the most votes and highest percentage of total votes. Print that info to the terminal and save it to the text file. 

             #Determine winning vote count and candidate
             if(votes>winning_count) and (vote_percentage > winning_percentage):
                 #if true then set winning_count = votes and winning_percent =vote_percentage
                 winning_count = votes
                 winning_percentage = vote_percentage
                 # and set winning candidate = candidate's name
                 winning_candidate = candidate_name

         #Print winning candidate's results to terminal
         winning_candidate_summary = (
             f"\n------------------------------\n"
             f"Winner: {winning_candidate}\n"
             f"Winning Vote Count: {winning_count:,}\n"
             f"Winning Percentage: {winning_percentage:.1f}%\n"
             f"------------------------------\n")
         print(winning_candidate_summary)

         #Save winning candidate's name to text file
         txt_file.write(winning_candidate_summary)

## Summary
 In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
