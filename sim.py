import random
"""
This is a simple program to test/implement the economic principle 
that given two groups starting with equal amounts of money, if they 
flip a coin and gamble one unit of money, given enough time/trades,
all of the money will end up with one person, while everyone else 
loses everything. Please feel free to play with the numbers.

"""
def tradesVisualizer():
    p1, p2 = 100, 100
    num = 0
    #Mess around with the number of 'trades'
    #Currentyly set to show where the money ends up between two people given 10000 random trades
    while num < 10000 and p1 > 0 and p2 > 0:
        cur = random.randint(0, 1)
        if cur == 0:
            p1 += 1
            p2 -= 1
        else:
            p1 -= 1
            p2 += 1
        num += 1
    print(f'P1: {p1}')
    print(f'P2: {p2}')

    return

def tradeSimulation():
    count = 0
    res = 0
    #Currently set to simulate the trade between two people with 100$ given 100000 random trades, and see how many times out of 100 that the money goes to one person
    while count < 1000:
        p1, p2 = 100, 100
        num = 0
        while num < 10000 and p1 > 0 and p2 > 0:
            cur = random.randint(0, 1)
            if cur == 0:
                p1 += 1
                p2 -= 1
            else:
                p1 -= 1
                p2 += 1
            num += 1
        if p1 != 0 and p2 != 0:
            res += 1
        count += 1

    print(f'# of times both groups both have a non zero amount of money: {res}')
    
    return

def main():
    tradeSimulation()
    tradesVisualizer()

if __name__ == '__main__':
    main()