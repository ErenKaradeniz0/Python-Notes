def q1():
    name = open("Python-Notes/Slides/weather.txt")

    lines = name.read().split()
    prev = float(lines[0])

    for i in range(1, len(lines)):
        next = float(lines[i])
        print(prev, "to", next, ", change=", round(next-prev, 1))
        prev = next


def q2():
    file = open("Python-Notes/Slides/gasprice.txt")
    belgium = 0
    usa = 0
    count = 0
    lines = file.read().split()

    for i in range(0, len(lines), 3):
        belgium += float(lines[i])
        usa += float(lines[i+1])
        count += 1
    print("Belgium average:", (belgium/count), "Ş/gal")
    print("USA average:", (usa/count), "Ş/gal")

q2()
