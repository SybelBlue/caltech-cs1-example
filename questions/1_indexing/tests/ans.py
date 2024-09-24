treasure = "gold!"
treasure_map1 = ["", "", "", treasure, ""]
print(treasure_map1[3])
treasure_map2 = [[[],[]],[[],treasure],[]]
print(treasure_map2[1][1])
treasure_map3 = [[[],[]],[[],(treasure)],[]]
print(treasure_map3[1][1])
treasure_map4 = ((0,1),(0,1,0),(1,0,(1,0),(1,0,1,0,treasure)))
# note the use of -1 to get the last items!
print(treasure_map4[-1][-1])