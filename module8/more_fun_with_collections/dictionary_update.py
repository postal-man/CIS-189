"""
Program: dictionary_update.py
Author: Liam P Reardon
Last date modified: 10/18/2023
Class: CIS-189
This program prompts the user for test scores, stores them in a dictionary, and averages the scores and returns the average to the user
"""

def get_test_scores():
    """
    :return: Dictionary of test scores
    """
    scores_dict = dict()
    num_scores = int(input("Please enter the desired number of test scores: "))

    # Loop to get inputted test scores
    for x in range(num_scores):
        while True:
            try:
                score = float(input("\nPlease enter a test score: "))
                # Check if score is between 0 and 100, if not print error message and try again
                if score < 0 or score > 100:
                    print("ERROR: You must enter a value between 0 and 100")
                    continue
                else:
                    print("[SCORE ENTERED SUCCESSFULLY]")
                # Add score to dictionary
                scores_dict.update({x: score})
                break
            except ValueError:
                # If score is not a number, print error message and try again
                print("ERROR: You must enter a numeric value")
                continue

    return scores_dict

def average_scores(scores_dict):
    """
    :param scores_dict: Dictionary of test scores
    :return: Average of test scores
    """
    if len(scores_dict) < 1:
        raise ValueError("You must enter at least one test score")

    num_scores = len(scores_dict) # Get number of scores
    total_score = sum(scores_dict.values()) # Get sum of scores
    average_score = total_score / num_scores # Calculate average score
    
    return average_score
        

def main():
    # Call functions get_test_scores and average_scores
    test_scores = get_test_scores()
    average_score = average_scores(test_scores)

    print("Test scores: ")
    # Enumerate through dictionary and print test scores
    for x in test_scores:
        print(test_scores[x])
    # Print average score, with some formatting to 2 decimal places
    print(f"Average score: {average_score:.2f}%")

if __name__ == "__main__":
    main()

