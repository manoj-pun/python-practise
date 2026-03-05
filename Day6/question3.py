#Write a function that takes a dictionary of student names and grades and returns a new dictionary grouping
#students into 'Pass' and 'Fail' categories.

def categorize_students(grades, passing_mark=50):
    """
    Categorize students into 'Pass' and 'Fail' based on their grades.
    
    Args:
    grades (dict): Dictionary with student names as keys and grades as values
    passing_mark (int, optional): Minimum grade to pass. Default is 50.
    
    Returns:
    dict: Dictionary with two keys 'Pass' and 'Fail', each containing a list of student names
    """
    result = {'Pass': [], 'Fail': []}
    
    for student, grade in grades.items():
        if grade >= passing_mark:
            result['Pass'].append(student)
        else:
            result['Fail'].append(student)
    
    return result

# Example usage
students = {
    'Alice': 75,
    'Bob': 45,
    'Charlie': 60,
    'David': 30
}

print(categorize_students(students))