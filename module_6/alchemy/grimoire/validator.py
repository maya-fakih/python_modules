def validate_ingredients(ingredients: str) -> str:
    okay = ["fire", "water", "earth", "air"]
    ing_list = ingredients.split(" ")

    is_valid = all(item in okay for item in ing_list)

    if is_valid:
        return f"[{ingredients}] - VALID"
    else:
        return f"[{ingredients}] - INVALID"
