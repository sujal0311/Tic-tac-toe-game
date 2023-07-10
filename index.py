def ConstBoard(board):
  print("Current State of the Board : \n\n");
  for i in range(0,9):
    if(i>0) and ((i%3)==0):
      print("\n");
    if(board[i]==0):
      print("_ ", end=" ");
    if(board[i]==-1):
      print("X ", end=" ");
    if(board[i]==1):
      print("O ", end=" ");
  print("\n\n");

def User1Turn(board):
  pos=input("Enter a X's position from [1,2,3,......7,8,9] ");
  pos=int(pos);
  if(board[pos-1]!=0):
    print("Wrong move");
    exit(0);
  board[pos-1]=-1;

def User2Turn(board):
  pos=input("Enter a O's position from[1,2,3,4,5,6,7,8,9] ");
  pos=int(pos);
  if(board[pos-1]!=0):
    print("Wrong move");
    exit(0);
  board[pos-1]=1;

def minmax(board, player):
  x= analyzeboard(board);
  if(x!=0):
    return(x*player);
  pos=-1;
  value=-2;
  for i in range(0,9):
    if(board[i]==0): 
      board[i]=player;
      score=-minmax(board, player*-1);
      board[i] = 0;
      if(score>value):
        value=score;
        pos=i; 
      
  if(pos==-1):
     return 0;
  return value;
    
def CompTurn(board):
  pos=-1;
  value=-2;
  for i in range(0,9):
    if(board[i]==0): 
      board[i]=1;
      score=-minmax(board, -1);
      board[i] = 0;
      if(score>value):
        value=score;
        pos=i;
  board[pos]=1;         
 
def analyzeboard(board):
  cb=[[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]            
  for i in range(0,8):
     if(board[cb[i][0]]!=0 and board[cb[i][0]]==board[cb[i][1]] and board[cb[i][0]]==board[cb[i][2]]):
       return board[cb[i][0]];
  return 0;  
       
def main():
  choice=input("ENTER 1 for Single Player , 2 for Multiplayer:")
  choice=int(choice);
  board=[0, 0, 0, 0, 0, 0, 0, 0, 0]
  if(choice==1):
    print("Computer : O Vs. You : X");
    player=input("Enter to play 1st or 2nd : ");
    player=int(player);
    for i in range(0,9):
      if(analyzeboard(board)!=0):
          break;
      if((i+player)%2==0):
         CompTurn(board);
      else:
        ConstBoard(board);
        User1Turn(board);

  else:
    for i in range(0,9):
       if(analyzeboard(board)!=0):
        break;
       if(i%2==0):
          ConstBoard(board);
          User1Turn(board);
       else:
          ConstBoard(board);
          User2Turn(board);

  x=analyzeboard(board);
  if(x==0):
    ConstBoard(board);
    print("Draw! ");
  if(x==-1):
    ConstBoard(board);
    print("Player X Wins!! O Looses!  ");
  if(x==1):
    ConstBoard(board);
    print("Player O Wins!! X Looses!  ");
    
main()    