
ice_cream: dict[str, int] = {"Chocolate": 12, "vanilla": 8, "Strawberry": 5}

ice_cream["mint"] = 3
print(ice_cream)

ice_cream.pop("mint")
print(ice_cream)

ice_cream["vanilla"] = 10

print(len(ice_cream))

print(f"There are {ice_cream['Chocolate']} orders of chocolate")

print("after updating vanilla")
print(ice_cream)

if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint")
else: print("There are no orders of mint")

if "Chocolate" in ice_cream:
    print(f"There are {ice_cream['Chocolate']} orders of chocolate")
else: print("There are no orders of chocolate")

for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders.")

    