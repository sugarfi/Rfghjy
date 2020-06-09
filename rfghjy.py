import sys

next = { 'p':'n', 'n':'i', 'i':'e', 'e':'d', 'd':'x', 'x':'p' }
n = [ 'p', 'n', 'i', 'e', 'd', 'x' ]

def run_one(i, at, ex, stack):
    if not stack:
        print(''.join(stack))
        sys.exit(0)
    if i == 'p':
        return stack.pop(0), ex, stack
    elif i == 'n':
        stack.append('p')
        return at, ex, stack
    elif i == 'i':
        stack.append(next[stack.pop()])
        return at, ex, stack
    elif i == 'e':
        sys.exit(0)
    elif i == 'd':
        at, ex = stack.pop(0), stack.pop()
        for i in range(n.index(ex)):
            stack.append(at)
        return at, ex, stack
    elif i == 'x':
        return at, stack.pop(0), stack
    print(f'Invalid character "{i}"')

def run(code):
    at, ex = 'p', 'p'
    stack = list(code.strip())
    print(''.join(stack))
    while stack:
        at, ex, stack = run_one(ex, at, ex, stack)
        at, ex, stack = run_one(at, at, ex, stack)
        print(''.join(stack))

if sys.argv[1:]:
    code = open(sys.argv[1]).read()
    run(code)
else:
    while True:
        run(input('> '))
