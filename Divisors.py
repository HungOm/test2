def give_divisors(num):
    dividsors = []
    for i in range(1,num+1):
        if num %i ==0:
            dividsors.append(i)
    return dividsors


def main():
    num = int((input("Enter a number: ")))
    print("Dividsors", give_divisors(num))

if __name__ == "__main__":
    main()
