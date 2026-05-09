"""

Joel Siguaw
IS 303 - A02

#Description
Meal Recommender: 
- Suggests a meal based on time of day, dietary preference, and budget

#INPUT
- Meal time (breakfast, lunch, dinner) (String)
- Dietary preference (vegetarian, vegan, none) (String)
- Budget (low, medium, high) (String)

#PROCESS
- Validate meal time (must be one of the specified options)
- Validate dietary preference (must be one of the specified options)
- Validate budget (must be one of the specified options)
- Based on the combination of meal time, dietary preference, and budget, determine a recommended meal

#OUTPUT
- Prints reccommended meal based on user's meal time, dietary preference, and budget
- Prints Invalid input messages for any input that is invalid

"""
#COMBINATIONS
breakfast_veg_low = "Oatmeal with fresh fruit and a drizzle of honey."
breakfast_veg_medium = "Avocado toast with a side of mixed berries."
breakfast_veg_high = "Vegetable omelette with a side of whole grain toast and a smoothie."
breakfast_vegan_low = "Chia seed pudding made with almond milk and topped with sliced bananas."
breakfast_vegan_medium = "Tofu scramble with sautéed vegetables and a slice of whole grain toast."
breakfast_vegan_high = "Vegan breakfast burrito with black beans, avocado, and salsa wrapped in a whole wheat tortilla."
breakfast_none_low = "Scrambled eggs with toast and a side of fruit."
breakfast_none_medium = "Pancakes with maple syrup and a side of bacon."
breakfast_none_high = "Steak and eggs with a side of roasted potatoes."
lunch_veg_low = "Grilled cheese sandwich with tomato soup."
lunch_veg_medium = "Quinoa salad with mixed vegetables and a lemon vinaigrette."
lunch_veg_high = "Vegetable stir-fry with tofu and brown rice."
lunch_vegan_low = "Hummus and veggie wrap with a side of fruit."
lunch_vegan_medium = "Lentil soup with a side of whole grain bread."
lunch_vegan_high = "Vegan burger with sweet potato fries."
lunch_none_low = "Turkey sandwich with a side of chips."
lunch_none_medium = "Chicken Caesar salad with a side of garlic bread."
lunch_none_high = "Grilled salmon with quinoa and steamed vegetables."
dinner_veg_low = "Pasta with marinara sauce and a side salad."
dinner_veg_medium = "Vegetable curry with basmati rice."
dinner_veg_high = "Eggplant Parmesan with a side of garlic bread."
dinner_vegan_low = "Black bean tacos with a side of rice."
dinner_vegan_medium = "Vegan chili with cornbread."
dinner_vegan_high = "Stuffed bell peppers with quinoa and vegetables."
dinner_none_low = "Spaghetti with meat sauce and a side salad."
dinner_none_medium = "Grilled chicken with roasted vegetables and mashed potatoes."
dinner_none_high = "Steak with a baked potato and steamed asparagus."   


#INPUT
meal_time = input("Enter meal time (breakfast, lunch, dinner): ").lower()
if not meal_time in ["breakfast", "lunch", "dinner"]:
    print("Invalid input: Meal time must be 'breakfast', 'lunch', or 'dinner'.")
    exit()

dietary_preference = input("Enter dietary preference (vegetarian, vegan, none): ").lower()
if not dietary_preference in ["vegetarian", "vegan", "none"]:
    print("Invalid input: Dietary preference must be 'vegetarian', 'vegan', or 'none'.")
    exit()

budget = input("Enter budget (low, medium, high): ").lower()
if not budget in ["low", "medium", "high"]:
    print("Invalid input: Budget must be 'low', 'medium', or 'high'.")
    exit()  

#PROCESS
if meal_time == "breakfast":
    if dietary_preference == "vegetarian":
        if budget == "low":
            meal = breakfast_veg_low
        elif budget == "medium":
            meal = breakfast_veg_medium
        else:
            meal = breakfast_veg_high
    elif dietary_preference == "vegan":
        if budget == "low":
            meal = breakfast_vegan_low
        elif budget == "medium":
            meal = breakfast_vegan_medium
        else:
            meal = breakfast_vegan_high
    else:
        if budget == "low":
            meal = breakfast_none_low
        elif budget == "medium":
            meal = breakfast_none_medium
        else:
            meal = breakfast_none_high
elif meal_time == "lunch":
    if dietary_preference == "vegetarian":
        if budget == "low":
            meal = lunch_veg_low
        elif budget == "medium":
            meal = lunch_veg_medium
        else:
            meal = lunch_veg_high
    elif dietary_preference == "vegan":
        if budget == "low":
            meal = lunch_vegan_low
        elif budget == "medium":
            meal = lunch_vegan_medium
        else:
            meal = lunch_vegan_high
    else:
        if budget == "low":
            meal = lunch_none_low
        elif budget == "medium":
            meal = lunch_none_medium
        else:
            meal = lunch_none_high
else:
    if dietary_preference == "vegetarian":
        if budget == "low":
            meal = dinner_veg_low
        elif budget == "medium":
            meal = dinner_veg_medium
        else:
            meal = dinner_veg_high
    elif dietary_preference == "vegan":
        if budget == "low":
            meal = dinner_vegan_low
        elif budget == "medium":
            meal = dinner_vegan_medium
        else:
            meal = dinner_vegan_high
    else:
        if budget == "low":
            meal = dinner_none_low
        elif budget == "medium":
            meal = dinner_none_medium
        else:
            meal = dinner_none_high


#OUTPUT
print(f"\nMeal Recommendation Summary\n"
      f"Meal Time: {meal_time} | Diet: {dietary_preference} | Budget: {budget}\n"
      f"Recommended Meal: {meal}")
