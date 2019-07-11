print("Enter percentage")
percentage = int(input())

def final_grade(percentage):
    if percentage <= 100 and percentage >= 97:
        return 'A+'
    elif percentage <= 96 and percentage >= 93:
        return 'A'
    elif percentage <= 92 and percentage >= 90:
        return 'A-'
    else:
        return 'well done.'

print(final_grade(percentage)) 