from classes import *
import os

map = Map()
p1 = Player('X')
p2 = Player('O')
count = 0

while True:
   
    os.system('cls')
    map.print_hash()

    print()
    player1 = int(input("PLAYER 1 - Choose the hash position: "))
    count += 1
    map.apply_play_on_hash(p1.play(player1), p1.x_or_o) 
        
    os.system('cls')
    map.print_hash()
    
    if count > 4:
        print()
        if map.verify_winner():
            break
    if count == 9 and map.has_winner == False:
        print("DRAW GAME!")
        break
    print(count)    
    
    print()
    player2 = int(input("PLAYER 2 - Choose the hash position: "))
    count += 1
    map.apply_play_on_hash(p2.play(player2), p2.x_or_o)


