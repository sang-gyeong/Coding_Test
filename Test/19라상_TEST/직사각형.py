def get_divisor(n):
    n = int(n)
    divisors = []
    divisors_back = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisors.append(i)
            if (i != (n // i)):
                divisors_back.append(n//i)

    return divisors + divisors_back[::-1]


def solution(N):
    a = get_divisor(N)
    b = N // a
    print(a, b)
    print(a * b)
    answer = abs(b-a)
    return answer


def main():
    result = solution(100000000000)
    print(result)


main()
