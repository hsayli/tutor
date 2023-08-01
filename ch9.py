import csv
l =[['star wars','terminator','top gun'],
    ['dumb','matilda','leviaphan'],
    ['men in black','i - robot','evolution'],
    ["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic", "The Revenant", "Inception"],
    ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv","w") as f:
    s = csv.writer(f,
                   delimiter=",")
    for mov in l:
        s.writerow(mov)