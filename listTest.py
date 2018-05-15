
# a =[]
# for i in range(100,3):
#     if i >=1 and i <= 10:
#         b=a[i]
#         print(b)
#     else:
#         print("There is no number within the range of 10")
# print("Thank you")
#-----------------------------------------------
a = [1,12,11,9,100,5,30,12,1,0]
new_list =[]

for i in a:
    if i < 10:
        new_list.append(i)
#return new_list # Return is for function
print(new_list)
#
#
# def filter_list(a):
#     new_list =[]
#     for number in a:
#         if number <10:
#             new_list.append(number)
#     return new_list
# def main():
#     a = [1,12,11,9,100,5,30,12,1,0]
#     print("New List:",filter_list(a))
#
# if __name__ == "__main__":
#     main()
# #This code works!
