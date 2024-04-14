import csv
import sys


def main():
    # Ensure correct usage
    if len(sys.argv) != 3 or (".csv" not in sys.argv[1] or ".txt" not in sys.argv[2]):
        sys.exit("Usage: python dna.py <CSV> <DNA_SEQUENCE>")

    # Load CSV file
    fname = sys.argv[1]
    csv_file = open(fname)

    # Load DNA sequence
    fname = sys.argv[2]
    dna_file = open(fname)
    dna_reader = csv.reader(dna_file)

    # Find longest match of each STR in DNA sequence
    # Create reader object
    # reader = csv.DictReader(csv_file)
    reader = csv.reader(csv_file)
    seqs = []

    # Iterate csv reader
    for d in dna_reader:
        for i, n in enumerate(reader):
            if i == 0:
                seqs = n[1:]
                continue

            for i, c in enumerate(n[1:]):
                m = longest_match(d[0], seqs[i])

                if m != int(c):
                    break

                if i == len(n[1:]) - 1:
                    return n[0]

    return "No match"


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

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    print(main())
