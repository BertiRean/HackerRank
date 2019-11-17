# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def combinatory(n, r):
    return (math.factorial(n) / (math.factorial(r) * (math.factorial(n - r))))

def binomial_dist(x, p, n):
    b = (combinatory(n, x) * (p ** x) * ((1-p)**(n-x)))
    return b

def main():
    
    data = input().split(' ')

    prob_fail = float(data[0]) / 100.0
    n = int(data[1])

    prob_almost_two_rejects = 0.0
    prob_no_rejects = 0.0

    for i in range(2, 11):
        prob_almost_two_rejects += binomial_dist(i, prob_fail, n)

    for i in range(0, 3):
        prob_no_rejects += binomial_dist(i, prob_fail, n)

    print(round(prob_no_rejects, 3))
    print(round(prob_almost_two_rejects, 3))

if __name__== "__main__":
  main()


