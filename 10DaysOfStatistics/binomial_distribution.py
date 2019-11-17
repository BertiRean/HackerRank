# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://es.wikipedia.org/wiki/Raz%C3%B3n_de_momios

import math

def combinatory(n, r):
    return (math.factorial(n) / (math.factorial(r) * (math.factorial(n - r))))

def binomial_dist(x, p, n):
    b = (combinatory(n, x) * (p ** x) * ((1-p)**(n-x)))
    return round(b, 3)

def main():
    
    data = input().split(' ')

    odd_ratio_boys = float(data[0])

    prob = odd_ratio_boys/(odd_ratio_boys + 1)

    total_prob = 0.0

    for i in range(3, 7):
        total_prob += binomial_dist(i, prob, 6)

    print(round(total_prob, 3))

if __name__== "__main__":
  main()


