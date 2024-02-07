# user input to create a list
list = input("Enter a list of integers separated by space: ").split()
print(list)

# we convert the input strings into integers
int_list = [int(number) for number in list]
print(int_list)

# now we compute the sum of all integers in the list
total_sum = sum(int_list)
print("The sum of all integers in in the list is: ", total_sum)
