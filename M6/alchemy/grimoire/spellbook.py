"""

"""


def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    res: str = validate_ingredients(ingredients)
    return f"Spell {"recorded" if res.endswith(" VALID") else "rejected"}: {spell_name} ({res})"