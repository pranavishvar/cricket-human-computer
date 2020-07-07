import random
print("odd or even game")
Toss=input("(b)Bat or (s)Bowl: ")
if Toss== "b":
    print("computer will bowl")
else:
    print("computer will bat")
playerscore = 0
computerscore=0
turn=0
while Toss=="b" or Toss =="s":
        while Toss== "b" :
           computer = random.randint(1, 6)
           player = input(" your turn: ")
           player=int(player)
           if player>0 and player < 7:
               print("player:    " , player)
               print("computer:  " , computer)
           else:
               print("Invalid input")
           if player==computer  :
              print('"player out "')
              break
           else:
               playerscore+=player
        if Toss == "b":
            print(f'"player score {playerscore}"')
            turn+=1
            Toss = "s"
        if turn==2:
            break
        while Toss == "s":
            if Toss=="s":
                computer = random.randint(1, 6)
                player = input(" your turn: ")
                player = int(player)
                if player>0 and player < 7:
                    print("player:   " ,player)
                    print("computer: " ,computer)
                else:
                    print("Invalid input")
                if computer == player:
                  print('"computer out "')
                  break
                else:
                   computerscore += computer
        if Toss == "s":
            print(f'" computer score {computerscore}"')
            turn+=1
            Toss = "b"
        if turn==2:
            break
if computerscore < playerscore:
    print('"Player won the match"')
elif computerscore > playerscore:
    print('"computer won the match"')
else :
    print('"Match Tie"')

































