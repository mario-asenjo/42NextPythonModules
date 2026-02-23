"""

"""


def validate_ingredients(ingredients: str) -> str:
    return f"{ingredients} - VALID" \
        if all(x in ["fire", "water", "earth", "air"] for x in ingredients.split()) \
        else f"{ingredients} - INVALID"
