import sys

def solution(numbers, target):
    visited = set()
    for number in numbers:
        number = int(number)
        pair = int(target) - number
        if not(number in visited) and str(pair) in numbers:
            visited.add(number)
            visited.add(pair)
            print(number, pair)

if __name__ == "__main__":
    numbers = sys.argv[1].split(',')
    target = sys.argv[2]
    solution(set(numbers), target)