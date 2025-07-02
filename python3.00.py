justice_league=["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
 #tasks on list
#number of members in jutice_league
print("No. of members:",len((justice_league)))

 #add Batgirl and Nightwing
justice_league.extend(["Batgirl", "Nightwing"])
print("\nAfter adding:", justice_league)

 #moving Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman") 
print("\nAfter moving Wonder Woman to the beginning:", justice_league)

 #separating Aquaman and Flash
justice_league.remove("Superman")
index_flash = justice_league.index("Flash")
index_aquaman = justice_league.index("Aquaman")

print("\nAfter separating Aquaman and Flash:", justice_league)

 #due to crisis replacing members of justics_league
justice_league=["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\nNew team:", justice_league)
 #sorting the list alphabetically
justice_league.sort()
print("\nSorted list:", justice_league)
 #finding the new leader
print("\nThe new leader is:", justice_league[0])