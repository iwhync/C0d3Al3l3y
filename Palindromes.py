with open("codeab.txt", "r") as a_file:
    for line in a_file:
        x = line.strip()
        x = x.replace(" ","").replace(",","").replace("-","").lower()
        if x == x[::-1]:
            print("Y")
        else:
            print("N")
