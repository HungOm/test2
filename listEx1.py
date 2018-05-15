
def filter_even(numList):
    even = []
    for i in numList:
        if i %2 == 0:
            even.append(i)
    return even


def main():
    numList = [1,12,11,9,100,5,30,12,1,0]
    print("Even numbers in the list include : ",filter_even(numList))

if __name__ == "__main__":
    main()
