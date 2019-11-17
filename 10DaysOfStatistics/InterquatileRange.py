# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def get_median(p_Values, p_N):

    median = 0.0

    if p_N == 0:
        return 0

    sorted_values = p_Values[:]
    sorted_values.sort()

    idx = int(p_N/2)

    if p_N % 2 == 0:
        median += sorted_values[idx - 1]
        median += sorted_values[idx]
        median /= 2.0
        return round(median, 1)
    else:
        return round(sorted_values[idx], 1)

def get_interquatile_range(p_Values, p_N):

    median = get_median(p_Values, p_N)

    sorted_values = p_Values[:]
    sorted_values.sort()

    first_half = []
    second_half = []

    idx = int(p_N/2)

    if p_N % 2 == 0:
        first_half = sorted_values[:idx]
        second_half = sorted_values[-idx:]
    else:
        first_half = sorted_values[:-idx]
        second_half = sorted_values[idx + 1:]

    q1 = get_median(first_half, len(first_half))
    q2 = median
    q3 = get_median(second_half, len(second_half))

    return round(float(q3 - q1), 1)

def main():

    n = int(sys.stdin.readline())
    lineVals = sys.stdin.readline().split(' ')
    freqs = sys.stdin.readline().split(' ')

    values = []
    
    for idx, val in enumerate(lineVals):
        j = 0
    
        while j < int(freqs[idx]):
            j += 1
            values.append(int(val))
    
    values.sort()

    print(get_interquatile_range(values, len(values)))

if __name__== "__main__":
  main()