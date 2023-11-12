from pymongo import MongoClient

def orderMealPlans(username, mealPlans):
    
    mongodb_server_url = 'mongodb+srv://anish:anish@cluster0.evuvsxb.mongodb.net/'
    database_name = 'MealPlanner'
    collection_name = 'uservectors'

    # Establish a connection to the MongoDB server
    client = MongoClient(mongodb_server_url)

    # Select the database
    db = client[database_name]

    # Select the collection
    collection = db[collection_name]

    mealPlansWHeiristics = []

    doc = collection.find_one({"username": username})

    vector = doc["dense"]

    for mealPlan in mealPlans:
        val = 0

        for recipeId in mealPlan:
            val += vector[recipeId-1]

        mealPlansWHeiristics.append((val, mealPlan))

    sorted_meal_plans = sorted(mealPlansWHeiristics, key=lambda x: x[0])

    sorted_meal_plans_only = [array for (value, array) in sorted_meal_plans]

    collection_name = 'users'

    collection = db[collection_name]

    collection.update_one(
            {"username": username},  # Assuming the _id field is the user ID
            {"$set": {"generatedMeals": sorted_meal_plans_only}}
        )

    return sorted_meal_plans_only