
student_name = "Steven Thorpe"
current_gpa = 3.9
study_hours = 10
social_points = 40
stress_level = 0

print(student_name)
print(current_gpa)
print(study_hours)
print(social_points)
print(stress_level)

#Course load options
print("Choose your course load:")
print("1) Light (12 credits)")  
print("2) Standard (15 credits)")
print("3) Heavy (18 credits)")

decision1 = input()

if decision1 == "1":
    if current_gpa >= 3.5:
        study_hours = 18
        stress_level = stress_level + 20
        print(f"Study Hours Required: {study_hours}")
        print(f"Potential Stress Level: {stress_level}")
    elif current_gpa >= 3.0 and current_gpa <= 3.4:
        study_hours = 24
        stress_level = stress_level + 25
        print(f"Study Hours Required: {study_hours}")
        print(f"Potential Stress Level: {stress_level}")
    elif current_gpa >= 2.5 and current_gpa <= 2.9:
        study_hours = 30
        stress_level = stress_level + 30
        print(f"Study Hours Required: {study_hours}")
        print(f"Potential Stress Level: {stress_level}")
    elif current_gpa >= 2.0 and current_gpa <= 2.4:
        study_hours = 36
        stress_level = stress_level + 35
        print(f"Study Hours Required: {study_hours}")
        print(f"Potential Stress Level: {stress_level}")
    else:
        study_hours = 40
        stress_level = 100
        print(f"Study Hours Required: {study_hours}")
        print(f"Potential Stress Level: {stress_level}")
elif decision1 == "2":
    if current_gpa >= 3.5:
        study_hours = 22
        stress_level = stress_level + 25
        print(f"Study Hours Required: {study_hours}")
        print(f"Potential Stress Level: {stress_level}")
    elif current_gpa >= 3.0 and current_gpa <= 3.4:
        study_hours = 30
        stress_level = stress_level + 30
        print(f"Study Hours Required: {study_hours}")
        print(f"Potential Stress Level: {stress_level}")
    elif current_gpa >= 2.5 and current_gpa <= 2.9:
        study_hours = 37
        stress_level = stress_level + 35
        print(f"Study Hours Required: {study_hours}")
        print(f"Potential Stress Level: {stress_level}")
    elif current_gpa >= 2.0 and current_gpa <= 2.4:
        study_hours = 45
        stress_level = stress_level + 40
        print(f"Study Hours Required: {study_hours}")
        print(f"Potential Stress Level: {stress_level}")
    else:
        study_hours = 50
        stress_level = 100
        print(f"Study Hours Required: {study_hours}")
        print(f"Potential Stress Level: {stress_level}")
elif decision1 == "3":
    if current_gpa >= 3.5:
        study_hours = 27
        stress_level = stress_level + 30
        print(f"Study Hours Required: {study_hours}")
        print(f"Potential Stress Level: {stress_level}")
    elif current_gpa >= 3.0 and current_gpa <= 3.4:
        study_hours = 36
        stress_level = stress_level + 35
        print(f"Study Hours Required: {study_hours}")
        print(f"Potential Stress Level: {stress_level}")
    elif current_gpa >= 2.5 and current_gpa <= 2.9:
        study_hours = 45
        stress_level = stress_level + 40
        print(f"Study Hours Required: {study_hours}")
        print(f"Potential Stress Level: {stress_level}")
    elif current_gpa >= 2.0 and current_gpa <= 2.4:
        study_hours = 54
        stress_level = stress_level + 45
        print(f"Study Hours Required: {study_hours}")
        print(f"Potential Stress Level: {stress_level}")
    else:
        study_hours = 60
        stress_level = 100
        print(f"Study Hours Required: {study_hours}")
        print(f"Potential Stress Level: {stress_level}")
else:
    print("Invalid")