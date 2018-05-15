def filter_odd(numList):
    odd = []
    for i in numList:
        if i %2 != 0:
            odd.append(i)
    return odd





def main():
    numList = [1,12,11,9,100,5,30,12,1,0]
    print("Odd numbers in the list include : ",filter_odd(numList))

if __name__ == "__main__":
    main()
