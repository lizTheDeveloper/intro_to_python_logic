guests = "Ash,Max,Joe,Roan,Caitlin"

names = guests.split(",")

names.append("Liz")
names.append("Liz")

print(len(names))
names[6] = "Kellyn"
print(names[-1])
first_person = names.pop(-1)
print(first_person)

for name in names[0:3]:
    print(name + "@themultiverse.school")

