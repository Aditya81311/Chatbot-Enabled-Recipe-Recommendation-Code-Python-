import pyttsx3

class RecipeRecommendation:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, name, ingredients, cuisine, dietary_restrictions, procedure):
        self.recipes.append({
            "name": name,
            "ingredients": ingredients,
            "cuisine": cuisine,
            "dietary_restrictions": dietary_restrictions,
            "procedure": procedure
        })

    def find_recipes_by_ingredients(self, available_ingredients):
        suggestions = []
        for recipe in self.recipes:
            if all(ingredient in available_ingredients for ingredient in recipe["ingredients"]):
                suggestions.append(recipe)
        return suggestions

    def filter_recipes(self, field, value):
        return [recipe for recipe in self.recipes if recipe[field].lower() == value.lower()]

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chatbot_interface():
    recipe_system = RecipeRecommendation()
    
    # Adding recipes
    recipe_system.add_recipe("Chicken Curry", ["chicken", "curry powder", "onions", "tomatoes"], "Indian", "Non-Vegetarian", "1. Heat oil and sauté onions...\n2. Add tomatoes and spices...")
    recipe_system.add_recipe("Biryani", ["rice", "chicken", "yogurt", "spices"], "Indian", "Non-Vegetarian", "1. Marinate chicken...\n2. Layer with rice...")
    recipe_system.add_recipe("Sushi", ["rice", "nori", "fish", "soy sauce"], "Japanese", "Non-Vegetarian", "1. Cook sushi rice...\n2. Roll with fish...")
    recipe_system.add_recipe("Tacos", ["tortilla", "beef", "lettuce", "cheese"], "Mexican", "Non-Vegetarian", "1. Cook beef...\n2. Assemble tacos...")
    recipe_system.add_recipe("Pad Thai", ["noodles", "peanuts", "tofu", "lime"], "Thai", "Vegetarian", "1. Cook noodles...\n2. Add sauce and tofu...")
    
    greeting = "Hello! Welcome to the Recipe Recommendation Chatbot."
    print(greeting)
    speak(greeting)
    print("You can ask me to suggest recipes based on ingredients, cuisine, or dietary restrictions!")
    
    while True:
        user_input = input("\nYour query (or type 'exit' to quit): ").lower()
        if user_input == "exit":
            farewell = "Goodbye! Happy cooking!"
            print(farewell)
            speak(farewell)
            break
        elif "ingredients" in user_input:
            ingredients = input("Enter your available ingredients (comma-separated): ").lower().split(", ")
            suggestions = recipe_system.find_recipes_by_ingredients(ingredients)
            if suggestions:
                print("\nRecipes you can make:")
                for recipe in suggestions:
                    print(f" - {recipe['name']} ({recipe['cuisine']}, {recipe['dietary_restrictions']})")
                    print(f"   Procedure: {recipe['procedure']}\n")
            else:
                print("Sorry, no recipes match your ingredients.")
        elif "cuisine" in user_input:
            cuisine = input("Enter the cuisine type: ").lower()
            filtered_recipes = recipe_system.filter_recipes("cuisine", cuisine)
            if filtered_recipes:
                print(f"\nRecipes from {cuisine} cuisine:")
                for recipe in filtered_recipes:
                    print(f" - {recipe['name']} (Ingredients: {', '.join(recipe['ingredients'])})")
                    print(f"   Procedure: {recipe['procedure']}\n")
            else:
                print(f"No recipes found for {cuisine} cuisine.")
        elif "diet" in user_input or "dietary restrictions" in user_input:
            diet = input("Enter your dietary restriction (e.g., Vegetarian, Vegan, Gluten-Free, Halal, Kosher, Keto): ").lower()
            filtered_recipes = recipe_system.filter_recipes("dietary_restrictions", diet)
            if filtered_recipes:
                print(f"\nRecipes suitable for a {diet} diet:")
                for recipe in filtered_recipes:
                    print(f" - {recipe['name']} (Ingredients: {', '.join(recipe['ingredients'])})")
                    print(f"   Procedure: {recipe['procedure']}\n")
            else:
                print(f"No recipes found for a {diet} diet.")
        else:
            print("Sorry, I didn't understand that. Please ask about ingredients, cuisine, or dietary restrictions.")

# Run the chatbot
if __name__ == "__main__":
    chatbot_interface()