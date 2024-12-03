def sticks_game():
    sticks = 16
    print("Welcome to the Sticks Game!")
    print("There are 16 sticks in total.")
    print("Each player can take 1, 2, or 3 sticks during their turn.")
    print("The player who takes the last stick loses the game.")

    while sticks > 0:
     print(f"\nSticks remaining: {sticks}")
     player1_move=int(input("how man sticks will you  take(1,2,3)"))
     sticks -= player1_move
     if sticks==0:
        print("player one takes the stick player1 loss")

     print(f"sticks remaining : {sticks}")
     play2_move=int(input("how many sticks will you take(1,2,3,)"))
     sticks -= play2_move
     if sticks==0:
        print("player two takes the stick player2 loss")

sticks_game()

