n = int(input())
S = set()

def handle_exception():
    order = input()
    if order == 'all':
        all()
    elif order == 'empty':
        empty()
        print(3)
        global S
        S = set()
        print(S)
    
def add(x):
    S.add(x)

def check(x):
    print(S)
    if x in S:
        print(1)
    else:
        print(0)

def remove(x):
    if x in S:
        S.remove(x)

def toggle(x):
    if x in S:
        S.remove(x)
    else:
        S.add(x)

def all():
    for i in range(20):
        S.add(i+1)

def empty():
    S.clear()

for _ in range(n):
    try:
        order, x = input().split()
        x = int(x)
    except ValueError:
        handle_exception()
    

    if order == "add" and x is not None:
        add(x)
    
    elif order == 'check' and x is not None:
        check(x)
    
    elif order == 'remove' and x is not None:
        remove(x)
    
    elif order == 'toggle' and x is not None:
        toggle(x)

    elif order == 'all':
        all()

    elif order == 'empty':
        empty()