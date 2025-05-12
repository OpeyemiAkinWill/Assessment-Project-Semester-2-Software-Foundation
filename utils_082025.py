def calculate_average(scores):
    return sum(scores) / len(scores)

def assign_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 85:
        return 'B'
    elif average >= 75:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
