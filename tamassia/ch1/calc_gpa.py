grade_map = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.67,
    "B+" :3.33, 
    "B" :3.0, 
    "B-" :2.67,
    "C+" :2.33, 
    "C" :2.0, 
    "C-" :1.67, 
    "D+" :1.33, 
    "D" :1.0, 
    "F" :0.0
}

def main():
    total_pts = 0
    num_courses = 0
    prompt()
    done = False
    while not done:
        grade = input()
        if grade == "":
            done = True
        elif grade not in grade_map.keys():
            print(f"Unknown grade {grade}, skipping...")
        else:
            total_pts += grade_map[grade]
            num_courses += 1

    print(f"Your gpa is: {calc_gpa(total_pts, num_courses):.2f}")

def calc_gpa(total: float, courses: int):
    return total / courses

def prompt():
    print("Welcome to the GPA calculator.")
    print("Please enter all your letter grades, one per line.")
    print("Enter a blank line to designate the end.")



main()