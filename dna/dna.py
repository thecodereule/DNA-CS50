import csv
import sys
import pandas as pd


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py database.csv sequence.txt")
        sys.exit(1)
    # TODO: Read database file into a variable
    dbfile = sys.argv[1]
    database_df = pd.read_csv(dbfile)

    #with open(dbfile, 'r') as file:
     #   reader = csv.DictReader(file)
      #  for row in reader:
       #     database.append(row)



    # TODO: Read DNA sequence file into a variable
    sequences = sys.argv[2]
    sequencefile = ''
    sequenced_list = list()
    with open(sequences, 'r') as file:
        sequencefile = file.read().strip()
    # TODO: Find longest match of each STR in DNA sequence
    strs = {key: longest_match(sequencefile, key) for key in database_df.columns[1:]}
    print(strs)

    print("------------------------------")

    # TODO: Check database for matching profiles
    for index, row in database_df.iterrows():
        if all(row[str_key] == str_value for str_key, str_value in strs.items()):
            print(row['name'])
            return
    print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


main()
