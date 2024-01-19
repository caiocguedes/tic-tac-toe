class Map:
    def __init__(self):
        #hash game constructor
        self.hash = [
                        [1,2,3],
                        [4,5,6],
                        [7,8,9]
                    ]
    #print actual hash game on screen    
    def print_hash(self):
        for x in self.hash:
            for j in x:
                print(j, end = ' ')
            print()
    
    #insert play into the hash (X or O)        
    def apply_play_on_hash(self, hash_position, x_or_o):
        #setting the index depending on the hash position chosen by the player
        if hash_position < 4:
            self.index = 0
        elif hash_position < 7:
            self.index = 1
        else:
            self.index = 2
        
        #for every position into the hash index, compares the number in the position to the position chosen by the player. Apply X or 0 to the chosen position    
        for i in range(len(self.hash[self.index])):
            if self.hash[self.index][i] == hash_position:
                self.hash[self.index][i] = x_or_o     
    
    def verify_winner(self):
        self.has_winner = False 
        for index in range(3):
            #winner in row?
            if self.hash[index][0] == self.hash[index][1] == self.hash[index][2]:
                print(f'{self.hash[index][0]} is the winner!')
                self.has_winner = True
                return True
            #winner in column?
            if self.hash[0][index] == self.hash[1][index] == self.hash[2][index]:
                print((f'{self.hash[0][index]} is the winner!'))
                self.has_winner = True
                return True
            #winner in main diagonal?
            if self.hash[0][0] == self.hash[1][1] == self.hash[2][2]:
                 print(f'{self.hash[0][0]} is the winner!')
                 self.has_winner = True
                 return True
            #winner in secondary diagonal?
            if self.hash[0][2] == self.hash[1][1] == self.hash[2][0]:
                print (f'{self.hash[0][2]} is the winner!')  
                self.has_winner = True
                return True             
                            
                
class Player:
    def __init__(self, x_or_o):
        self.x_or_o = x_or_o
        
    def play(self, hash_position):
        self.hash_position = hash_position
        return hash_position
    

