# Advanced Programming Methodology #
# Sidequest 2.1 Template #
#
# Note that written answers are commented out to allow us to run your #
# code easily while grading your problem set.

from random import *
from puzzle import GameGrid


###########
# Helpers #
###########

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0], 
                  accumulate(fn, initial, seq[1:]))

def flatten(mat):
    return [num for row in mat for num in row]



###########
# Task 1  #
###########

def new_game_matrix(n):
    "Your answer here"
    N=[]
    F=[]
    for i in range(0,n):
        for j in range(0,n):
            F.append(0)
        N.append(F)
        F=[]
    return N
def has_zero(mat):
    "Your answer here"
    matrix=flatten(mat)
    for i in range(0,len(matrix)):
        if matrix[i]==0:
            return True
    return False


def add_two(mat):
    "Your answer here"
    if has_zero(mat)==False:
        return mat
    matrix=flatten(mat)
    #random_number=randint(0,15)
    #zero_dict={}
    zero_index=[]
    for i in range(0,len(matrix)):
        if matrix[i]==0:
            zero_index.append(i)
            random_number=randint(0,len(zero_index)-1)

    matrix[zero_index[random_number]]=2
    N=[]
    F=[]
    count=0
    for i in range(0,len(mat)):
        for j in range(0,len(mat[0])):
            F.append(matrix[count])
            count+=1
        N.append(F)
        F=[]
    return N

            
                



###########
# Task 2  #
###########
def is_adj(mat):
    matrix=flatten(mat)
    if len(mat)==1:
        for i in range(0,len(matrix)-1):
            if matrix[i]==matrix[i+1]:
                return True
            else:
                return False
    for i in range(0,len(matrix)-len(mat[0])):
        if (i+1)%len(mat[0])==0:
            if matrix[i]==matrix[i+len(mat[0])]:
                return True
        else:
            if matrix[i]==matrix[i+1] or matrix[i]==matrix[i+len(mat[0])]:
                return True
    for i in range(len(matrix)-len(mat[0]),len(matrix)-1):
        if matrix[i]==matrix[i+1]:
            return True
    return False
        
def game_status(mat):
    "Your answer here"
    matrix=flatten(mat)
    mark=0
    for i in range(0,len(matrix)):
        if matrix[i]==2048:
            return 'win'
        elif matrix[i]!=0:
            mark+=1
    if mark==len(matrix):
        if is_adj(mat)==False:
            return 'lose' 
    return 'not over'



###########
# Task 3a #
###########

def transpose(mat):
    "Your answer here"
    #row=len(mat)
    #col=len(mat[0])
    return [[row[col] for row in mat] for col in range(len(mat[0]))]



###########
# Task 3b #
###########

def reverse(mat):
    "Your answer here"
    return [[row[col] for col in range(len(mat[0]))[::-1]] for row in mat]


############
# Task 3ci #
############

def merge_line(list1):
    no_zero_list=[]
    value=0
    is_move=False
    for i in range(len(list1)):
        if list1[i]!=0:
            no_zero_list.append(list1[i])
    for j in range(0,len(no_zero_list)-1):
        if no_zero_list[j]==no_zero_list[j+1]:
            no_zero_list[j]*=2
            value+=no_zero_list[j]
            no_zero_list[j+1]=0
    for j in range(0,len(no_zero_list)-1):        
        if no_zero_list[j]==0:
            temp=no_zero_list[j]
            no_zero_list[j]=no_zero_list[j+1]
            no_zero_list[j+1]=temp
    for k in range(len(list1)-len(no_zero_list)):
        no_zero_list.append(0)
    for p in range(len(list1)):
        if list1[p]!=no_zero_list[p]:
            is_move=True
        
    return no_zero_list,value,is_move

def merge_left(mat):
    "Your answer here"
    matrix=[]
    value=0
    is_move=False
    for i in range(len(mat)):
        matrix.append(merge_line(mat[i])[0])
        value+=merge_line(mat[i])[1]
        if merge_line(mat[i])[2]==True:
            is_move=True
    return matrix,is_move,value

    
    



#############
# Task 3cii #
#############

def merge_right(mat):
    "Your answer here"
    matrix,is_move,value = merge_left(reverse(mat))
    return reverse(matrix),is_move,value
def merge_up(mat):
    "Your answer here"
    matrix,is_move,value = merge_left(transpose(mat))
    return transpose(matrix),is_move,value
def merge_down(mat):
    "Your answer here"
    matrix,is_move,value = merge_right(transpose(mat))
    return transpose(matrix),is_move,value

###########
# Task 3d #
###########

def text_play():
    def print_game(mat, score):
        for row in mat:
            print(''.join(map(lambda x: str(x).rjust(5), row)))
        print('score: ' + str(score))
    GRID_SIZE = 4
    score = 0
    mat = add_two(add_two(new_game_matrix(GRID_SIZE)))
    print_game(mat, score)
    while True:
        move = input('Enter W, A, S, D or Q: ')
        move = move.lower()
        if move not in ('w', 'a', 's', 'd', 'q'):
            print('Invalid input!')
            continue
        if move == 'q':
            print('Quitting game.')
            return
        move_funct = {'w': merge_up,
                      'a': merge_left,
                      's': merge_down,
                      'd': merge_right}[move]
        mat, valid, score_increment = move_funct(mat)
        if not valid:
            print('Move invalid!')
            continue
        score += score_increment
        mat = add_two(mat)
        print_game(mat, score)
        status = game_status(mat)
        if status == "win":
            print("Congratulations! You've won!")
            return
        elif status == "lose":
            print("Game over. Try again!")
            return
        
# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR GAME
#text_play()


# How would you test that the winning condition works?
# Your answer:create a new game with 2048
#


##########
# Task 4 #
##########

##def make_state(matrix, total_score):
##    "Your answer here"
##    return lambda t:matrix if t==0 else total_score
##
##def get_matrix(state):
##    "Your answer here"
##    return state(0)
##def get_score(state):
##    "Your answer here"
##    return state(1)
##def make_new_game(n):
##    "Your answer here"
##    return make_state(add_two(add_two(new_game_matrix(n))),0)
##    
##
##def left(state):
##    "Your answer here"
##    new_matrix,is_move,value=merge_left(get_matrix(state))
##    if is_move==True:
##        new_matrix=add_two(new_matrix)
##    return make_state(new_matrix,get_score(state)+value),is_move
##    
##    
##def right(state):
##    "Your answer here"
##    new_matrix,is_move,value=merge_right(get_matrix(state))
##    if is_move==True:
##        new_matrix=add_two(new_matrix)
##    return make_state(new_matrix,get_score(state)+value),is_move
##def up(state):
##    "Your answer here"
##    new_matrix,is_move,value=merge_up(get_matrix(state))
##    if is_move==True:
##        new_matrix=add_two(new_matrix)
##    return make_state(new_matrix,get_score(state)+value),is_move
##def down(state):
##    "Your answer here"
##    new_matrix,is_move,value=merge_down(get_matrix(state))
##    if is_move==True:
##        new_matrix=add_two(new_matrix)
##    return make_state(new_matrix,get_score(state)+value),is_move

# Do not edit this #
##game_logic = {
##    'make_new_game': make_new_game,
##    'game_status': game_status,
##    'get_score': get_score,
##    'get_matrix': get_matrix,
##    'up': up,
##    'down': down,
##    'left': left,
##    'right': right,
##    'undo': lambda state: (state, False)
##}

# UNCOMMENT THE FOLLOWING LINE TO START THE GAME (WITHOUT UNDO)
#gamegrid = GameGrid(game_logic)




#################
# Optional Task #
#################

###########
# Task 5i #
###########
                     
def make_new_record(mat, increment):
    "Your answer here"
    return mat,increment
def get_record_matrix(record):
    "Your answer here"
    return record[0]
def get_record_increment(record):
    "Your answer here"
    return record[1]
############

# Task 5ii #
############

def make_new_records():
    "Your answer here"
    return list()

def push_record(new_record, stack_of_records):
    "Your answer here"
    if len(stack_of_records)>=3:
        del stack_of_records[0]
    stack_of_records.append(new_record)
    return stack_of_records

def is_empty(stack_of_records):
    "Your answer here"
    return len(stack_of_records)==0

def pop_record(stack_of_records):
    "Your answer here"
    if is_empty(stack_of_records)!=True:
            stack_of_records.pop()
    return stack_of_records
#############
# Task 5iii #
#############

# COPY AND UPDATE YOUR FUNCTIONS HERE
def make_state(matrix, total_score, records):
    "Your answer here"
    
    return matrix,total_score,records
def get_matrix(state):
    "Your answer here"
    return state[0]
def get_score(state):
    "Your answer here"
    return state[1]
def make_new_game(n):
    "Your answer here"
    return make_state(add_two(add_two(new_game_matrix(n))),0,make_new_records())
def left(state):
    "Your answer here"
    old_mat,old_score=get_matrix(state),get_score(state)
    new_matrix,is_move,value=merge_left(get_matrix(state))
    if is_move==True:
        new_matrix=add_two(new_matrix)
    return make_state(new_matrix,get_score(state)+value,push_record(make_new_record(old_mat,old_score), get_records(state))),is_move

def right(state):
    "Your answer here"
    old_mat,old_score=get_matrix(state),get_score(state)
    new_matrix,is_move,value=merge_right(get_matrix(state))
    if is_move==True:
        new_matrix=add_two(new_matrix)
    return make_state(new_matrix,get_score(state)+value,push_record(make_new_record(old_mat,old_score), get_records(state))),is_move

def up(state):
    "Your answer here"
    old_mat,old_score=get_matrix(state),get_score(state)
    new_matrix,is_move,value=merge_up(get_matrix(state))
    if is_move==True:
        new_matrix=add_two(new_matrix)
    return make_state(new_matrix,get_score(state)+value,push_record(make_new_record(old_mat,old_score), get_records(state))),is_move


def down(state):
    "Your answer here"
    old_mat,old_score=get_matrix(state),get_score(state)
    new_matrix,is_move,value=merge_down(get_matrix(state))
    if is_move==True:
        new_matrix=add_two(new_matrix)
    return make_state(new_matrix,get_score(state)+value,push_record(make_new_record(old_mat,old_score), get_records(state))),is_move

# NEW FUNCTIONS TO DEFINE
def get_records(state):
    "Your answer here"
    return state[2]
def undo(state):
    "Your answer here"
    records = get_records(state)
    if not is_empty(records):
        record = records[-1]
        return (make_state(get_record_matrix(record),get_record_increment(record),pop_record(records)),True)
    else:
        return (state,True)


# UNCOMMENT THE FOLLOWING LINES TO START THE GAME (WITH UNDO)
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': lambda state: (state, False)
}

def auto_move(state):
    c=AI(state[0])
    #print(c)
    if c=='w':
        return (up(state)[0],True)
    elif c=='a':
        return (left(state)[0],True)
    elif c=='s':
        return (down(state)[0],True)
    elif c=='d':
        return (right(state)[0],True)

from math import *
def AI(mat):
    # replace the following line with your code
    dt=tree()
    dt.linktohead(node([mat,0]))
    depth=0
    if num_blank(mat)<5 :
        depth=4
    else:
        depth=2
    make_decision_tree(dt._head,depth)
    child_value_list=[]
    index=5
    if merge_up(mat)[1]==True:
        child_value_list.append(maxer2(dt._head.children[0]))
    else:
        child_value_list.append(0)

    if merge_left(mat)[1]==True:
        child_value_list.append(maxer2(dt._head.children[1]))
    else:
        child_value_list.append(0)
    if merge_down(mat)[1]==True:
        child_value_list.append(maxer2(dt._head.children[2]))
    else:
        child_value_list.append(0)
    if merge_right(mat)[1]==True:
        child_value_list.append(maxer2(dt._head.children[3]))
    else:
        child_value_list.append(0)
    print(child_value_list)
    index=max_index(child_value_list)

    dict={0:'w',1:'a',2:'s',3:'d'}
    print (dict[index])
    
    return ('w', 'a', 's', 'd')[index]

def max_index(lst):
    max_value=max(lst)
    for i in range(len(lst)):
        if max_value==lst[i]:
            return i
    return False

def make_decision_tree(node1,depth):
    matrix=node1.getdata()[0]
    if depth==0:
        return
    left_move=miner(merge_left(matrix)[0]) if merge_left(matrix)[1]==True else matrix
    right_move=miner(merge_right(matrix)[0]) if merge_right(matrix)[1]==True else matrix
    up_move=miner(merge_up(matrix)[0]) if merge_up(matrix)[1]==True else matrix
    down_move=miner(merge_down(matrix)[0]) if merge_down(matrix)[1]==True else matrix
    left=node([left_move,cal_value(left_move)])
    right=node([right_move,cal_value(right_move)])
    up=node([up_move,cal_value(up_move)])
    down=node([down_move,cal_value(down_move)])

    node1.add(up)
    node1.add(left)
    node1.add(down)
    node1.add(right)
    make_decision_tree(up,depth-1)
    make_decision_tree(left,depth-1)
    make_decision_tree(down,depth-1)
    make_decision_tree(right,depth-1)
    return
    #给定树的起始结点和遍历深度，生成完全4叉树（不剪枝）
    


def maxer(node1):
    matrix,value=node1.getdata()
    list=[]
    for i in range(len(node1.children)):
        list.append(node1.children[i].data[1])
    new_value=max(list)
    return new_value

def maxer2(node1):
    matrix,value=node1.getdata()
    list=[]
    if node1.children==[]:
        return cal_value(matrix)
    for i in range(len(node1.children)):
        list.append(maxer2(node1.children[i]))
    return max(list)
    


def num_blank(mat):
    matrix=flatten(mat)
    count=0
    for i in range(len(matrix)):
        if matrix[i]==0:
            count+=1
    return count

def miner(mat):
    min_num=10000
    min_i=-1
    min_j=-1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==0:
                mat[i][j]=2
                temp=cal_value(mat)
                if temp<min_num:
                    min_i,min_j,min_num=i,j,temp
                mat[i][j]=0
    mat[min_i][min_j]=2
    return mat
    
                
                

def cal_value(mat):
    matrix=flatten(mat)
    sqrt_value=0#平方和价值（log底数大于0）
    for i in range(len(matrix)):
        sqrt_value+=matrix[i]**2 #特征1：当前棋局的所有数字的平方和
    sqrt_value=2*log(sqrt(sqrt_value),2)
    blank=num_blank(mat)#特征2：空格数
    value=sqrt_value+blank
    return value
    #输入当前决策的矩阵
    #返回当前决策的价值
class node(object):
    def __init__(self,data):
        self.data=data
        self.children=[]
    def getdata(self):
        return self.data
    def getchildren(self):
        return self.children
    def add(self,node):
        if len(self.children)==4:
            return False
        else:
            self.children.append(node)

 
class tree:
 
    def __init__(self):
        self._head = node('header')
 
    def linktohead(self, node):
        self._head = node


game_logic['make_new_game'] = make_new_game
game_logic['undo'] = undo

game_logic['auto'] = auto_move

gamegrid = GameGrid(game_logic)


