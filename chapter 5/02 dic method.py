marks = {
    "Kanhaiya": 10,
    "K" : 100,
    "Aman" :25
}
print(marks.items())
print(marks.keys())
marks.update({"K": 99, "R":10})
print(marks)
print(marks.get("K"))
print(marks.pop("K"))
print(marks["K2"])
