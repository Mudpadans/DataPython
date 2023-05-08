import csv

with open("CupcakeInvoices.csv", "r") as csvfile:
    reader = csv.reader(csvfile)

    chocolate_total = 0
    vanilla_total = 0
    strawberry_total = 0
    all_total = 0

    for line in reader:
        n = float(line[3])
        p = float(line[4])
        each_total = n * p
        if line[2] == "Chocolate":
            chocolate_total += each_total
        elif line[2] == "Vanilla":
            vanilla_total += each_total
        elif line[2] == "Strawberry":
            strawberry_total += each_total
    
    print("%.2f" % chocolate_total)
    print("%.2f" % vanilla_total)
    print("%.2f" % strawberry_total)

    

csvfile.close()