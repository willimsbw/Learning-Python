def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """

    def convert_to_numeric(score):
        """
        Convert the score to a float.
        """
        return float(score)

    def sum_of_middle_three(score1, score2, score3, score4, score5):
        """
        Takes 5 numbers and returns the sum of all 5 minus the minimum and the
        max. Put another way, returns the sum of the middle 3 numbers.
        """
        max_score = max(score1, score2, score3, score4, score5)
        min_score = min(score1, score2, score3, score4, score5)
        return score1 + score2 + score3 + score4 + score5 - max_score - min_score

    def score_to_rating_string(score):
        """
        returns a rating string based on input score
        """
        if score < 1:
            return "Terrible"
        elif score < 2:
            return "Bad"
        elif score < 3:
            return "OK"
        elif score < 4:
            return "Good"
        elif score >= 4:
            return "Excellent"

    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating

print(scores_to_rating("1", 2.5, 3, 4, 5))
print(scores_to_rating("5", 5.0, 5, 5, 5))
print(scores_to_rating("1", 1.0, 1, 1, 5))
print(scores_to_rating("1", 2, 3.0, "2", 5))
