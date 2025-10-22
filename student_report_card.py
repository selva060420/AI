def get_grade(average):
    if average >= 90: return 'A'
    elif average >= 80: return 'B'
    elif average >= 70: return 'C'
    elif average >= 60: return 'D'
    else: return 'F'

def generate_report_card():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    
    subjects = ['Math', 'Science', 'English', 'History', 'Art']
    marks = {}
    
    for subject in subjects:
        marks[subject] = float(input(f"Enter marks for {subject}: "))
    
    average = sum(marks.values()) / len(marks)
    grade = get_grade(average)
    
    print("\n" + "="*40)
    print("         STUDENT REPORT CARD")
    print("="*40)
    print(f"Student ID: {student_id}")
    print(f"Name: {name}")
    print("-"*40)
    print("SUBJECT MARKS:")
    for subject, mark in marks.items():
        print(f"{subject:<10}: {mark:>6.1f}")
    print("-"*40)
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print("="*40)

if __name__ == "__main__":
    generate_report_card()