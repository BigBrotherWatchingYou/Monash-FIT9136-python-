import random

def traps(position):
    move = 0
    if position == 5:
        print(" He lost his wallet and go back to find it -2")
        move = -2
        
    if position == 8:
        print(" He was fucked by a tiger -1")
        move = -1
        
    if position in [10,11,15,17]:
        print(" Nuclear missile attack, all players die ")
        move = 888   
        
    if position == 12:
        print(" Lightning Storm created, all go back -3")
        move = -3
    
    if position == 16:
        print(" Your daddy ask you to pay the debt,  go back -2")
        move = -2
    
    if position == 9:
        print(" Mother fucker,  go back -5")
        move = -5
        
    return move

def throw_dice(P1_position, P2_position, round):
    if round >= 20:
        if P2_position > P1_position:
            print("winner: Player 2")
        if P1_position > P2_position:
            print("winner: Player 1")
        if P1_position == P2_position:
            print(" all losers")
        
        return False
    print("Round: ", round)
    
    # player_1 move
    P1_throw_dice = random.randint(1,6)
    P1_dice_number = P1_throw_dice
    print('player_1 throw dice and get:  ', P1_dice_number, " ") 
       
    P1_position += P1_dice_number
    
    P1_position += traps(P1_position)
    
    if P1_position  >= 888 or P2_position >= 888:
        print("All nuked die")
        return False
    
    print('now he is at: ', P1_position)
    
    
    
    # player_2 move
    P2_throw_dice = random.randint(1,6)
    P2_dice_number = P2_throw_dice
    print('player_2 throw dice and get:  ', P2_dice_number, " ")
    
    P2_position += P2_dice_number
     
    P2_position += traps(P2_position)
    if P1_position  >= 888 or P2_position >= 888:
        print("All nuked die")
        return False
    
    print('now he is at: ', P2_position)
    
    round += 1
    
    
    
    return throw_dice(P1_position, P2_position,round)

throw_dice(0, 0, 0)

