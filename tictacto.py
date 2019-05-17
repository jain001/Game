 def choice():
    player_1 = input("enter the choice you want to enter player 1 'X' OR '0' : ").upper()
    player_2 = input("enter the choice you want to enter player 2 'X' OR '0' : ").upper()
    return (player_1,player_2)


def board_2():
    for i in range(3):
        for j in range(3):
            print('|__'+lis[i][j]+'__|',end=" ")
        print('\n') 

        
        
def check_index1(a):
    if a in list_1:
        b =list_1.index(a) 
        row,col =(0,b)
        lis[row][col]=player_1
        board_2()
    elif a in list_2:
        b=list_2.index(a)
        row,col =(1,b)
        lis[row][col]=player_1
        board_2()
    elif a in list_3:
        b=list_3.index(a)
        row,col =(2,b)
        lis[row][col]=player_1
        board_2() 
    else:
        print("You Entered Wrong Input Sorry...... ")
        print("Game Start From Begning..")
        play(player_1,player_2)
        
        
        

def check_index2(a):
    if a in list_1:
        b =list_1.index(a) 
        row,col =(0,b)
        lis[row][col]=player_2
        board_2()
    elif a in list_2:
        b=list_2.index(a)
        row,col =(1,b)
        lis[row][col]=player_2
        board_2()
    elif a in list_3:
        b=list_3.index(a)
        row,col =(2,b)
        lis[row][col]=player_2
        board_2()
    else:
        print("You Entered Wrong Input Sorry...... ")
        print("Game Start From Begning..")
        play(player_1,player_2)
        


def draw_no(lis):
    up1 =lis[0]
    up2 =lis[1]
    up3 =lis[2]
    t=['1','2','3','4','5','6','7','8','9']
    re= any(i in up1 for i in t) or any(i in up2 for i in t) or any(i in up3 for i in t)
    return re


def play(player_1,player_2):
    while True:
        if player_1==player_2:
            print('\n')
            print("Your choices are same please select diffrentely....")
            player_1,player_2 = choice()
        elif player_1.upper()=='X' and player_2=='0':
            result =draw_no(lis)
            print(result)
            if result==False:
                print("Match Is Draw Opps.........")
                inp=input(" Do You Want To Play Again . If Yes Press 1 Otherwise Press 0 For Exit:  ")
                if inp=='1':
                    pass
                elif inp=='0':
                    print("You Are Out Of The Game.......")
                    break
            pos_p1 = input(f"On Which Position You Want To Enter {player_1} Player 1 :  ")
            check_index1(pos_p1)
            if lis[0]==['X','X','X'] or lis[1]==['X','X','X'] or lis[2]==['X','X','X']or(lis[0][0]=='X'and lis[1][0]=='X'and lis[2][0]=='X')or(lis[0][1]=='X'and lis[1][1]=='X'and lis[2][1]=='X')or(lis[0][2]=='X'and lis[1][2]=='X'and lis[2][2]=='X')or(lis[0][0]=='X' and lis[1][1]=='X'and lis[2][2]=='X')or (lis[0][2]=='X' and lis[1][1]=='X'and lis[2][0]=='X'):
                print("Player 1 Win The Match..........")
                break
            result =draw_no(lis)
            print(result)
            if result==False:
                print("Match Is Draw Opps.........")
                inp=input(" Do You Want To Play Again . If Yes Press 1 Otherwise Press 0 For Exit:  ")
                if inp=='1':
                    pass
                elif inp=='0':
                    print("You Are Out Of The Game.......")
                    break    
                
            pos_p2 = input(f"On Which Position You Want To Enter {player_2} Player 2 :  ")
            check_index2(pos_p2)
            if lis[0]==['0','0','0'] or lis[1]==['0','0','0'] or lis[2]==['0','0','0']or(lis[0][0]=='0'and lis[1][0]=='0'and lis[2][0]=='0')or(lis[0][1]=='0'and lis[1][1]=='0'and lis[2][1]=='0')or(lis[0][2]=='0'and lis[1][2]=='0'and lis[2][2]=='0')or(lis[0][0]=='0' and lis[1][1]=='0'and lis[2][2]=='0')or (lis[0][2]=='0' and lis[1][1]=='0'and lis[2][0]=='0'):
                print("Player 2 Win The Match..........")
                break     
        elif player_1=='0' and player_2.upper()=='X':
            result =draw_no(lis)
            print(result)
            if result==False:
                print("Match Is Draw Opps.........")
                inp=input(" Do You Want To Play Again . If Yes Press 1 Otherwise Press 0 For Exit:  ")
                if inp=='1':
                    pass
                elif inp=='0':
                    print("You Are Out Of The Game.......")
                    break
            pos_p1 = input(f"On Which Position You Want To Enter {player_1} Player 1 :  ")
            check_index1(pos_p1)
            if lis[0]==['0','0','0'] or lis[1]==['0','0','0'] or lis[2]==['0','0','0']or(lis[0][0]=='0'and lis[1][0]=='0'and lis[2][0]=='0')or(lis[0][1]=='0'and lis[1][1]=='0'and lis[2][1]=='0')or(lis[0][2]=='0'and lis[1][2]=='0'and lis[2][2]=='0')or(lis[0][0]=='0' and lis[1][1]=='0'and lis[2][2]=='0')or (lis[0][2]=='0' and lis[1][1]=='0'and lis[2][0]=='0'):
                print("Player 1 Win The Match..........")
                break 
            result =draw_no(lis)
            print(result)
            if result==False:
                print("Match Is Draw Opps.........")
                inp=input(" Do You Want To Play Again . If Yes Press 1 Otherwise Press 0 For Exit:  ")
                if inp=='1':
                    pass
                elif inp=='0':
                    print("You Are Out Of The Game.......")
                    break    
            pos_p2 = input(f"On Which Position You Want To Enter {player_2} Player 2 :  ")
            check_index2(pos_p2)
            if lis[0]==['X','X','X'] or lis[1]==['X','X','X'] or lis[2]==['X','X','X']or(lis[0][0]=='X'and lis[1][0]=='X'and lis[2][0]=='X')or(lis[0][1]=='X'and lis[1][1]=='X'and lis[2][1]=='X')or(lis[0][2]=='X'and lis[1][2]=='X'and lis[2][2]=='X')or(lis[0][0]=='X' and lis[1][1]=='X'and lis[2][2]=='X')or (lis[0][2]=='X' and lis[1][1]=='X'and lis[2][0]=='X'):
                print("Player 2 Win The Match..........")
                break
        else:
            print("You Had Choose Incorrect Choice. Please Choose It Again....")
            player_1,player_2 = choice()


        
lis =[['1','2','3'],1
       ['4','5','6'],
       ['7','8','9']]
list_1 =lis[0]
list_2= lis[1]
list_3 = lis[2]



player_1,player_2 = choice()
play(player_1,player_2)