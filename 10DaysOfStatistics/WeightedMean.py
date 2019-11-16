# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def get_weighted_mean(p_Values, p_Weights, p_N):

    mean = 0.0

    if p_N == 0:
        return 0.0

    total_weight = 0.0

    for idx, value in enumerate(p_Values):
        mean += (value * p_Weights[idx])
        total_weight += p_Weights[idx]
    
    return round(mean/total_weight, 1)

def main():

    n = int(sys.stdin.readline())

    values = []
    weights = []
    
    for num in sys.stdin.readline().split(' '):
        values.append(int(num))

    for weight in sys.stdin.readline().split(' '):
        weights.append(int(weight))

    print(get_weighted_mean(values, weights, n))

if __name__== "__main__":
  main()