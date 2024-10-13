"""Practice with for in loops"""

# pets: list[str] = ["Louie", "Bo", "Bear"]

# for name in pets:
# print(f"Good boy, {name}!")

# for x in [1, 2, 3]:
# print(x)

names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
