def check_answers(quiz_answers,answer_key,passing_grade):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    quiz_answers: answers to check for correctness
    answer_key: key of correct answers to check against quiz_answers
    passing_grade: float. The percent of correct answers needed to pass in decimal form
    """
    #create variable to count correct answers
    count_correct = 0
    #check to make sure answer_key and quiz_answers are same length
    if len(quiz_answers) == len(answer_key):
        #compare each quiz_answer to its corresponding answer_key value and add
        #to count_correct for each matching answer
        for index in range(len(quiz_answers)):
            if quiz_answers[index] == answer_key[index]:
                count_correct += 1

    #returns a pass or fail message, depending on whether you got enough correct
    #answers to meet the passing_grade
    if count_correct/len(quiz_answers) > passing_grade:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of " + str(len(quiz_answers)) + "."
    else:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of " + str(len(quiz_answers)) + "."
