

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

print("")
print("")

class_options = ["Programming", "Math", "History", "English"]
print(class_options)
class_choice = input("Pick a class:")

if class_choice in class_options:
    print("Nice Choice!")
    if class_choice == "Programming":
        if current_gpa <= 3.7:
            current_gpa = current_gpa + 0.2
        elif 3.8 <= current_gpa <= 3.9:
            current_gpa = current_gpa + 0.1
        else:
            current_gpa = 4.0
    elif class_choice == "Math":
        if current_gpa > 1.0 :
            current_gpa = current_gpa - 0.1
        else:
            current_gpa = 1.0
    elif class_choice == "History":
        if current_gpa <= 3.5:
            current_gpa = current_gpa + 0.5
        else:
            current_gpa == 4.0
    elif class_choice == "English": 
        if not (current_gpa >= 3.0):
            current_gpa = current_gpa - 0.5
        else:
            current_gpa = current_gpa - 0.2
    else:
        print("GPA must be between 1.0 and 4.0, please enter GPA again.")
elif current_gpa not in class_options:
    print("Sorry, that is not an option.") or print("Error, please try again")
else:
    print("error")

# Social points logic
if class_choice in class_options and current_gpa >= 3.5:
    social_points += 25
elif class_choice in class_options and current_gpa >= 3.0:
    social_points += 15
elif class_choice in class_options and current_gpa >= 2.5:
    social_points -= 15
elif class_choice in class_options and current_gpa >= 2.0:
    social_points -= 25
elif class_choice in class_options and current_gpa < 2.0:
    social_points = 0

# Cap social points at a "good" maximum
good_social_score = 50
if social_points >= good_social_score:
    social_points = good_social_score
    if social_points is good_social_score:
        print("You're doing great")
    if social_points is not good_social_score:
        print("Please try harder")

print("\n--- Results ---")
print("Updated GPA:", round(current_gpa, 2))
print("Updated Social Points:", social_points)
print("Study Hours:", study_hours)
print("Stress Level:", stress_level)
print("")
print("")
print("")
if social_points >= 50 or current_gpa >= 3.0:
    print("Great Job! You completed the game with flying colors!")
elif social_points >= 30 or current_gpa >= 2.5:
    print("Congratulations! You Passed!")
else:
    print("You didn't pass :( Better luck next time!")




#chatgpt was used to help create lines (129-133) so that the not statement could fit.
# The following lines lower your gpa if your gpa is considered not a strong gpa 
#because of the rigor of enligsh class if you're not good at it already. The if
# not only activates if gpa is below 3.0. It was also used in lines under social points logic.
#Those lines of code use "if" and "and" statements to decipher how certain class choices affect your
#soclial points while allowing for multiple outcomes.