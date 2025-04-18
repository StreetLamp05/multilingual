def main():
    gradebook = {}

    num_students = int(input("Enter the number of students: "))

    for i in range(num_students):
        name = input("Enter student name: ")
        grades = input("Enter grades for {name}: (comma-separated): ")
        grade_list = [float(g.strip()) for g in grades.split(",")]
        gradebook[name] = grade_list

    print("\nGradebook")
    for name, grades in gradebook.items():
        print(name)
        average = sum(grades) / len(grades)
        print(f"{name}: Average = {average:.2f}; Grades = {grades}")

if __name__ == "__main__":
    main()

