for i in range(1,100):
    print("\n\n******* WELCOME TO tictacto (multiplayer) ******** \n\n")
    board={
         '1': ' ' ,'2': ' ' , '3': ' ',
         '4': ' ' ,'5': ' ' , '6': ' ',
         '7': ' ' ,'8': ' ' , '9': ' '
    }
    p1=input("player 1 please enter you name :")
    p2=input("player 2 please enter you name :")
    while p1==p2:
        print("error  PLAYER 2 YOUR NAME MUST BE UNIQUE")
        p2=input("player 2 please enter you name :")
    p2_symbol=input(p2+" please select your symbol 'x' or 'o'  :")
    while p2_symbol !='x' and p2_symbol !='o':
        print(" invalid you are bound to select x or o \n")
        p2_symbol=input(p2+" please select your symbol 'x' or 'o'  :")
    
    if p2_symbol=='x':
        print(p1," your symbol is 'o' ")
        p1_symbol='o'
    else:
        print(p1," your symbol is 'x' \n")
        p1_symbol='x'
    choice=input(p1+" select heads(enter 0)  or tail(enter 1) : ")
    while choice !='0' and choice !='1':
        print(" invalid you are bound to enter 0 or 1  \n")
        choice=input(p1+" select heads(enter 0)  or tail(enter 1) : ")
    heads='0'
    tail='0'   
    print("          we are doing a toss please wait            ")    
   
    import random
    toss=random.randint(0,1)
    if toss==1:
        print(p1," won the toss")
        print(p1," you have awarded 1st move : ") 
    else:
        print(p2,"   won the toss")
        print(p2,"   you have awarded 1st move : ") 
    
       
    player=1   
    total_moves=0
    end_check=0

    def check():
     if p1_symbol=='x':
        if board['1']==board['2']==board['3']=='x' :
            print(p1,"won the match ")
            return 1
        if board['4']==board['5']==board['6']=='x':
             print(p1," won the match ")
             return 1
        if board['7']==board['8']==board['9']=='x':
            print(p1," won the match ")
            return 1   
        if board['1']==board['4']==board['7']=='x':
            print(p1," won the match ")
            return 1
        if board['2']==board['5']==board['8']=='x':
            print(p1," won the match ")
            return 1
        if board['3']==board['6']==board['9']=='x':
            print(p1," won the match ")
            return 1
        if board['1']==board['5']==board['9']=='x':
            print(p1," won the match ")
            return 1
        if board['3']==board['5']==board['7']=='x':
            print(p1," won the match ")
            return 1
        if board['1']==board['2']==board['3']=='o' :
            print(p1 ," won the match ")
            return 1
        if board['4']==board['5']==board['6']=='o':
            print(p2," won the match ")
            return 1
        if board['7']==board['8']==board['9']=='o':
            print(p2," won the match ")
            return 1   
        if board['1']==board['4']==board['7']=='o':
            print(p2," won the match ")
            return 1
        if board['2']==board['5']==board['8']=='o':
            print(p2," won the match ")
            return 1
        if board['3']==board['6']==board['9']=='o':
            print(p2," won the match ")
            return 1
        if board['1']==board['5']==board['9']=='o':
            print(p2," won the match ")
            return 1
        if board['3']==board['5']==board['7']=='o':
            print(p2," won the match ")
            return 1
        else:
             if total_moves==9:
               print("########## ITS TIE ###########")
             return 0
               
     else:     
        if board['1']==board['2']==board['3']=='o' :
            print(p1,"won the match ")
            return 1
        if board['4']==board['5']==board['6']=='o':
             print(p1," won the match ")
             return 1
        if board['7']==board['8']==board['9']=='x':
            print(p1," won the match ")
            return 1   
        if board['1']==board['4']==board['7']=='o':
            print(p1," won the match ")
            return 1
        if board['2']==board['5']==board['8']=='o':
            print(p1," won the match ")
            return 1
        if board['3']==board['6']==board['9']=='o':
            print(p1," won the match ")
            return 1
        if board['1']==board['5']==board['9']=='o':
            print(p1," won the match ")
            return 1
        if board['3']==board['5']==board['7']=='o':
            print(p1," won the match ")
            return 1
        if board['1']==board['2']==board['3']=='x' :
            print(p1 ," won the match ")
            return 1
        if board['4']==board['5']==board['6']=='x':
            print(p2," won the match ")
            return 1
        if board['7']==board['8']==board['9']=='x':
            print(p2," won the match ")
            return 1   
        if board['1']==board['4']==board['7']=='x':
            print(p2," won the match ")
            return 1
        if board['2']==board['5']==board['8']=='x':
            print(p2," won the match ")
            return 1
        if board['3']==board['6']==board['9']=='x':
            print(p2," won the match ")
            return 1
        if board['1']==board['5']==board['9']=='x':
            print(p2," won the match ")
            return 1
        if board['3']==board['5']==board['7']=='x':
            print(p2," won the match ")
            return 1
        if (board['1']==board['2']and board['2'] !=board['3'])and(board['4']==board['5']and board['5']!=board['6'])and(board['7']==board['8']and board['8']!=board['9'])and (board['1']==board['4']and board['4']!=board['7'])and (board['2']==board['5']and board['5']!=board['8'])and (board['3']==board['6']and board['6']!=board['9'])and(board['1']==board['5']and board['6']!=board['9'])and (board['3']==board['5']and board['5']!=board['7']):
            print("ITS TIE ")
            return 1
        if (board['1']!=board['2']and (board['2'] ==board['3']or board['1']==board['3']))and(board['4']!=board['5']and(board['5']==board['6']or board['4']==board['6'])and(board['7']!=board['8']and (board['8']==board['9']or (board['7']==board['9'])and board['1']!=board['4']))and (board['4']==board['7']or board['1']==board['7']))and (board['2']!=board['5']and (board['5']==board['8']or board['2']==board['8']))and (board['3']!=board['6']and (board['6']==board['9']or board['3']==board['9']))and(board['1']!=board['5']and (board['5']==board['9']or board['1']==board['9']))and (board['3']!=board['5']and (board['5']==board['7']or board['3']==board['7'])):
            print("ITS TIE ")
            return 1
      
        else:
            if total_moves==9:
                print("######## ITS TIE #########")
            return 0


    print('1|2|3')
    print('_+_+_')
    print('4|5|6')
    print('_+_+_')
    print('7|8|9')
    print('_+_+_')
    print("########")

    while True:
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
        print('_ _ _ ')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('_ _ _ ')
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print('_ _ _')
        end_check=check()
        if total_moves==9 or end_check==1:
            break
        while True:
            if toss==1:    
                    if player==1:     
                       p1_input=input( p1+" please select position : ")
                       if p1_input in board and board[p1_input]== ' ':
                          if p1_symbol=='o':
                             board[p1_input]='o'
                             player=2
                             break
                          if p1_symbol=='x':
                             board[p1_input]='x'
                             player=2
                             break
                            
                       else :
                           print("invalid input,try again")
                           continue
                    else:
                         p2_input=input(p2+" please select position : ")
                         if p2_input in board and board[p2_input]== ' ':
                            if p2_symbol=='o':
                             board[p2_input]='o'
                             player=1
                             break
                            if p2_symbol=='x':
                               board[p2_input]='x'
                               player=1
                               break 
                         else:
                            print("invalid input,try again")
                            continue
            else:
                    if player==1:     
                       p2_input=input( p2+" please select position : ")
                       if p2_input in board and board[p2_input]== ' ':
                           if p2_symbol=='o':
                              board[p2_input]='o'
                              player=2
                              break
                           if p2_symbol=='x':
                              board[p2_input]='x'
                              player=2
                              break
                       else :
                           print("invalid input,try again")
                           continue
                    else:
                         p1_input=input(p1+" please select position : ")
                         if p1_input in board and board[p1_input]== ' ':
                            if p1_symbol=='o':
                               board[p1_input]='o'
                               player=1
                               break
                            if p1_symbol=='x':
                               board[p1_input]='x'
                               player=1
                               break
                         else:
                            print("invalid input,try again")
                            continue
                    
        total_moves+=1
    print()
    print("********************")
    n=input("do you want to play again(enter y or any key) otherwise enter x( to exit)  :")
    if (n=='x' or n=='X') and n!=' ':
       break
    if (n=='y' or n=='Y'):
       i+=1 
