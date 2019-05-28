def score_grades(grade):
    """
    Funcao para descobrir a nota
    """

    if grade >= 90:
        if grade == 100:
            return "+A"
        else:
            return "Not +A"
    else:
        return "F"

grades = [10, 5, 100, 90]

scores = [score_grades(grade) for grade in grades]

print(scores)
