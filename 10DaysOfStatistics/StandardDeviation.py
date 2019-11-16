# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math


def get_mean(p_Values, p_N):

    mean = 0.0

    if p_N == 0:
        return 0.0

    for value in p_Values:
        mean += value

    return round(mean/p_N, 1)

def get_standard_deviation(p_Values, p_N):

    mean = 0.0

    if p_N == 0:
        return 0.0

    mean = get_mean(p_Values, p_N)

    variance = 0.0

    for val in p_Values:
        variance += ((val - mean) * (val - mean))

    return round(math.sqrt(variance/p_N), 1)

def main():

    n = int(sys.stdin.readline())

    values = []
    
    for num in sys.stdin.readline().split(' '):
        values.append(int(num))

    print(get_standard_deviation(values, n))

if __name__== "__main__":
  main()