import decimal


def napr(x,y):
    result = (y+3*(x-1)-2)/x
    return result

def euler(n_x,x,y):
    global x0,y0
    k = napr(x,y)
    y2 = k*(n_x-x)+y
    return y2

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

dots = [[1],[1]]
x0 = dots[0][0]
y0 = dots[1][0]

STEP = 0.1

for dot in float_range(1,4,STEP):
    y = euler(dot,dots[0][-1],dots[1][-1])
    dots[0].append(dot)
    dots[1].append(y)

dots[0].remove(1)
dots[1].remove(1)
print(dots[1][dots[0].index(3.0)])
