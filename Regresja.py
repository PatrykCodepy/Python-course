import math
import matplotlib.pyplot as plt
import scipy.stats as st

data_y = [14.1, 13.8, 12.7, 12.3, 11.5, 11.0]
data_x = [5, 10, 15, 20, 25, 30]
n = len(data_y)

def average(data):
    return sum(data) / len(data)

def variance(data):
    sum = 0
    for i in range(n):
        sum += pow(data[i], 2)
    return ( 1 / (n-1)) * (sum-n*pow(average(data), 2))

def cov(x,y):
    sum = 0
    for i in range(n):
        sum += (x[i] * y[i])
    return (1 / (n-1)) * (sum - n * average(x) * average(y))

def r(x,y):
    return (cov(x, y))/(math.sqrt(variance(x)*variance(y)))

class regression:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n
    def b0(self):
        b0 = average(self.y) - self.b1() * average(self.x)
        return b0
    def b1(self):
        b1 = cov(self.x, self.y)/variance(self.x)
        return b1
    def print(self):
        print('y=', self.b0(), self.b1(), 'x')
    def vary(self):
        vary = []
        for i in range(10-self.x[self.n-1], self.x[n-1]+1):
            vary.append(self.b0()+self.b1()*i)
        return vary
    def chart(self):
        plt.scatter(self.x, self.y)
        plt.plot(range(10-self.x[n-1], self.x[n-1]+1), self.vary(), 'r')
        plt.title('REGRESSION')
        plt.show()

class hypothesis:
    print('b1 == 0 \nb1 =/= 0')
    def __init__(self, alfa, n, x ,y):
        self.alfa = alfa
        self.n = n
        self.x = x
        self.y = y
    def t(self):
        t = st.t.ppf((self.alfa/2), n-2)
        return t
    def R(self):
        print(f'(-inf;{self.t()})U({-self.t()};inf)')
    def t0(self):
        t0 = (r(self.x, self.y) * math.sqrt(n-2)) / (math.sqrt(1-pow(r(self.x, self.y), 2)))
        return t0
    def t0inR(self):
        if self.t0() <= -self.t() or self.t0() >= self.t():
            print('t0€R')
            return True
    def matched(self):
        if pow(r(self.x, self.y), 2) >= .9 or pow(r(self.x, self.y), 2) >= 1:
            print('The best!')
        elif pow(r(self.x, self.y), 2) >= .8 or pow(r(self.x, self.y), 2) > .9:
            print('Better!')
        elif pow(r(self.x, self.y), 2) >= 0.6 or pow(r(self.x, self.y), 2) > .8:
            print('Satisfactorily')
        else:
            print('Shit')

variable = hypothesis(float(input('Podaj alfa: ')), n, data_x, data_y)
print(variable.matched())
print(variable.t0inR())
print(variable.t0())
del variable
variable = regression(data_x, data_y, n)
variable.chart()
