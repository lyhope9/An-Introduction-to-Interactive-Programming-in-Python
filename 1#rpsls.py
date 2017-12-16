#rock-paper-scissors-lizard-spock
#0-rock
#1-spock
#2-paper
#3-lizard
#4-scissors
#用求余算法简化比较过程，画一个圈，
#打败逆时针的两个选择，输给顺时针的两个是选择
#random.range()函数随机取数作为计算机的选择

import random

def name_to_number(name):
    if name=='rock':
        num=0
    elif name=='spock':
        num=1
    elif name=='paper':
        num=2
    elif name=='lizard':
        num=3
    elif name=='scissors':
        num=4
    else:
        print 'you input an invalid name'
    return num

def number_to_name(num):
    if num==0:
        name='rock'
    elif num==1:
        name='spock'
    elif num==2:
        name='paper'
    elif num==3:
        name='lizard'
    elif num==4:
        name='scissors'
    else:
        print 'you input an invalid number'
    return name

def rpsls(guess):
    player_number=name_to_number(guess)
    comp_number=random.randrange(0,4,1)
    player_choose=number_to_name(player_number)
    comp_choose=number_to_name(comp_number)
    print ''
    print 'Player chooses',player_choose
    print 'Compter chooses',comp_choose
    mod=(player_number-comp_number)%5
    if mod==1 or mod==2:
        print 'Player wins!'
    elif mod==3 or mod==4:
        print 'Compter wins!'
    elif mod==0:
        print 'Make ties'
    else:
        print 'The input has an error'


rpsls('rock')
rpsls('spock')
rpsls('paper')
rpsls('lizard')
rpsls('scissors')
