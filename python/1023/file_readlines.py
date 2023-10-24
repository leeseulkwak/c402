with open("info.txt", "r") as file:
    for line in file:
        (name, weight, height)=line.strip().split(",")

        print(line)