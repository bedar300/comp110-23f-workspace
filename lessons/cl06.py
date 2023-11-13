"""Practice with for loops"""

pets: list[str] = ["Louie", "Bo", "Bear"]
for pet_names in pets:
    print(f"Good boy, {pet_names}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for idx in range (0,3):
    elem: str = names[idx]
    print(f"{idx}: {elem}")

