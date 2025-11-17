# KEY : VALUE

marks= {
    "Harrry": 100,
    "Shubham": 50,
    "Rohan": 0

}

print(marks, type(marks))
print(marks["Harrry"])

#    PROPERTIES
# 1. UNORDERED
# 2. MUTABLE
# 3. IT IS INDEXED
# 4. CANNOT CONTAIN DUPLICATE KEYS

# marks.item()  gives items inside in form of tuples
# marks.keys()

marks.update({"Rohan": 100, "Renuka":100})
print(marks)

marks.get("Harrry")