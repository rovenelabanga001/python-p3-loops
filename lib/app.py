player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 
0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008,
0.009, 0.008, 0.009, 0.01, 0.01]

inch_heights = list()
inch_heights = [height * 7920 for height in player_heights]
print(player_heights)