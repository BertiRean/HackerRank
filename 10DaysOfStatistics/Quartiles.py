# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

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
        return round(sorted_values[(p_N/2)], 1)

def get_quartiles(p_Values, p_N):

    median = get_median(p_Values, p_N)

    sorted_values = p_Values[:]
    sorted_values.sort()

    first_half = []
    second_half = []

    if p_N % 2 == 0:
        first_half = sorted_values[:p_N/2]
        second_half = sorted_values[-p_N/2:]
    else:
        first_half = sorted_values[:-p_N/2]
        second_half = sorted_values[p_N/2 + 1:]

    print(int(get_median(first_half, len(first_half))))
    print(int(median))
    print(int(get_median(second_half, len(second_half))))

def main():

    n = int(sys.stdin.readline())

    values = []
    
    for num in sys.stdin.readline().split(' '):
        values.append(int(num))

    get_quartiles(values, n)

if __name__== "__main__":
  main()