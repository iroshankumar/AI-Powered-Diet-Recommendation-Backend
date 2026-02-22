def calculate_daily_calories(user):
    bmr = 10 * user.weight + 6.25 * user.height - 5 * user.age + 5

    activity_multipliers = {
        "sedentary": 1.2,
        "moderate": 1.55,
        "active": 1.75
    }

    multiplier = activity_multipliers.get(user.activity_level.lower(), 1.2)
    maintenance_calories = bmr * multiplier

    if user.health_goal.lower() == "weight_loss":
        maintenance_calories -= 500
    elif user.health_goal.lower() == "muscle_gain":
        maintenance_calories += 300

    return maintenance_calories



def generate_meal_plan(user, meals):
    target = calculate_daily_calories(user)

    matching_meals = [
        meal for meal in meals
        if meal.diet_type.lower() == user.dietary_preference.lower()
    ]

    selected = []
    total = 0

    for meal in matching_meals:
        if total + meal.calories <= target:
            selected.append({
                "name": meal.name,
                "calories": meal.calories,
                "protein": meal.protein,
                "carbs": meal.carbs,
                "fat": meal.fat
            })
            total += meal.calories

    return {
        "target_calories": round(target, 2),
        "total_selected_calories": total,
        "meals": selected
    }