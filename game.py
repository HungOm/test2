def print_numbers():
    for i in range(1,101):
        if i%3 ==0:
            print(i,"Fizz")
        elif i%15 == 0:
            print(i,"Buzz")
        elif i%5 ==0:
            print(i,"Buzz")
        else:
            print(i)


def main():
    print_numbers()

if __name__ =="__main__":
    main()
