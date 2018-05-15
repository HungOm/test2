def isPrime(n):
    if n<2:
        return False
    if n ==2:
        return True
    for u in range(2,n):
        if n%u ==0:
            return False
    return True


def prime_num(num):
    prime =[]
    for i in num:
        if isPrime(i):
            prime.append(i)
    return prime
def main():
    num = [1,12,11,9,100,5,30,12,1,0]
    print("Prime numbers in the list include : ",prime_num(num))

if __name__ == "__main__":
    main()
