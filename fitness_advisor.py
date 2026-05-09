"""

Joel Siguaw
IS 303 - A02

#Description
Fitness Advisor:
- Recommends an exercise plan based on fitness level and goals

#INPUT
- Name (String)
- Age (Integer)
- Height (Inches) (Integer)
- Starting weight (lbs) (Integer)
- Fitness level (beginner, intermediate, advanced) (String)
- Fitness Goal (weight loss, Weight Gain) (String)

#PROCESS
- Validate name (must be a non-empty string)
- Validate age (must be a positive integer between 1 and 120)
- Validate height (must be a positive integer in inches between 12 and 96)
- Validate starting weight (must be a positive integer between 20 and 1000)
- Validate fitness level (must be one of the specified options)
- Validate fitness goal (must be one of the specified options)
- Based on the fitness level and goal, recommend an exercise plan:
    - For weight loss:
        - Beginner: 30 minutes of cardio 5 days a week, and 2 days of light strength training.
        - Intermediate: 45 minutes of cardio 5 days a week, and 3 days of moderate strength training.
        - Advanced: 60 minutes of cardio 6 days a week, and 4 days of intense strength training.
    - For Weight gain:
        - Beginner: 3 days of light strength training, and 2 days of moderate cardio.
        - Intermediate: 4 days of moderate strength training, and 2 days of light cardio.
        - Advanced: 5 days of intense strength training, and 1 day of light cardio

#OUTPUT
- name, age, height, starting weight, fitness level, fitness goal
- Personalized exercise plan based on the user's fitness level and goals
- Invalid input messages for any input that fails validation

"""

#PLAN OPTIONS
beg_weight_loss_plan = "Beginner Weight Loss Plan: 30 minutes of cardio 5 days a week, and 2 days of light strength training."
int_weight_loss_plan = "Intermediate Weight Loss Plan: 45 minutes of cardio 5 days a week, and 3 days of moderate strength training."
adv_weight_loss_plan = "Advanced Weight Loss Plan: 60 minutes of cardio 6 days a week, and 4 days of intense strength training."
beg_weight_gain_plan = "Beginner Weight Gain Plan: 3 days of light strength training, and 2 days of moderate cardio."
int_weight_gain_plan = "Intermediate Weight Gain Plan: 4 days of moderate strength training, and 2 days of light cardio."
adv_weight_gain_plan = "Advanced Weight Gain Plan: 5 days of intense strength training, and 1 day of light cardio."

#INPUT
name = input("What is your name? ").strip().capitalize()
if not name:
    print("Invalid input: Name must contain text.")
    exit()

age = input("What is your age? ")
if not age.isdigit() or not (1 <= int(age) <= 120):
    print("Invalid input: Age must be a positive integer between 1 and 120.")
    exit()
age = int(age)

height = input("What is your height in inches? ")
if not height.isdigit() or not (12 < int(height) < 96):
    print("Invalid input: Height must be a positive integer in inches between 12 and 96.")
    exit()
height = int(height)

starting_weight = input("What is your starting weight in pounds? ")
if not starting_weight.isdigit() or not (20 <= int(starting_weight) <= 1000):
    print("Invalid input: Starting weight must be a positive integer between 20 and 1000.")
    exit()
starting_weight = int(starting_weight)

fitness_level = input("What is your fitness level (beginner, intermediate, advanced)? ").lower()
if fitness_level not in ("beginner", "intermediate", "advanced"):
    print("Invalid input: Fitness level must be one of the specified options: beginner, intermediate, or advanced.")
    exit()

fitness_goal = input("What is your fitness goal (weight loss, weight gain)? ").lower()
if fitness_goal not in ("weight loss", "weight gain"):
    print("Invalid input: Fitness goal must be one of the specified options: weight loss or weight gain.")
    exit()

#PROCESS
if fitness_goal == "weight loss":
    if fitness_level == "beginner":
        exercise_plan = beg_weight_loss_plan
    elif fitness_level == "intermediate":
        exercise_plan = int_weight_loss_plan
    else:
        exercise_plan = adv_weight_loss_plan
else:
    if fitness_level == "beginner":
        exercise_plan = beg_weight_gain_plan
    elif fitness_level == "intermediate":
        exercise_plan = int_weight_gain_plan
    else:
        exercise_plan = adv_weight_gain_plan

#OUTPUT
print(f"{name}, your exercise plan and personal information are as follows:\n"
      f"{exercise_plan}\n"
      f"Age: {age}\n"
      f"Height: {height} inches\n"
      f"Starting Weight: {starting_weight} lbs\n"
      f"Fitness Level: {fitness_level}\n"
      f"Fitness Goal: {fitness_goal}")