# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def get_mean(p_Values, p_N):

    mean = 0.0

    if p_N == 0:
        return 0.0

    for value in p_Values:
        mean += value

    return round(mean/p_N, 1)


def get_median(p_Values, p_N):

    median = 0.0

    if p_N == 0:
        return 0

    sorted_values = p_Values[:]
    sorted_values.sort()

    if p_N % 2 == 0:
        median += sorted_values[(p_N/2) - 1]
        median += sorted_values[(p_N/2)]
        median /= 2.0
        return round(median, 1)
    else:
        return round(sorted_values[(p_N/2) - 1]/2, 1)


def get_mode(p_Values, p_N):

    sorted_values = p_Values[:]

    sorted_values.sort()

    mode = 0

    freq = {}

    for num in sorted_values:
        if num not in freq:
            freq[num] = 0
        else:
            freq[num] += 1

    greater = freq[sorted_values[0]]
    mode = sorted_values[0]

    for key, val in freq.items():

        if val > greater:
            mode = key
            greater = val
        elif val == greater and key < mode:
            mode = key

    return mode
        

def main():

    n = int(sys.stdin.readline())

    values = []

    for line in sys.stdin:
        for num in line.split(' '):
            values.append(int(num))

    print(get_mean(values, n))
    print(get_median(values, n))
    print(get_mode(values, n))

if __name__== "__main__":
  main()

