# Find the smallest number that can be framed using the series created by the digits obtained by raising the given number  (  "a"  ) to the power from 1 to  n  i.e.  a^1 , a^2 , a^3 .......a^n . We get  b1,b2 , b3 , ........... bn . 
# Using all the digits  ( including repeating ones )  that appear inb1 ,b2 , b3 .... bn . Frame a number that contains all the digits ( including repeating ones )  and find out the combination of digits that make the smallest number of all possible combinations. Excluding or neglecting zeroes  ( " 0 " )  . 
# Input: The first line contains a number T i.e numbers of  test cases . Followed by each test case that contains two integers "a" and "n" . 

# Output: Output of each test case contains an integer which is the smallest number out of all combinations .
# Constraints:   
# 1 < = T < = 350
# 0 < = n < =  5
# 0 < = a < = 90 

# Example:

# Input 
# 4
# 9 4
# 5 1
# 6 5
# 90 4

# Output:
# 1125667899
# 5
# 11223666667779
# 1125667899

# Explanation :
# Test case 1: 9 3 
# 9^1 = 9
# 9^2 = 81
# 9^3 = 729
# 9^4  = 6561 
# 9 81 729 6561
# We get  9817296561 .
# Using 9817296561 number we need to find the smallest possible number that can be framed using other combinations of the samenumber .
# 1298796561
# 8799265611
# 2186561997
# .
# .
# .
# 1125667899
# The smallest possible number that can be framed is1125667899 . 
# https://practice.geeksforgeeks.org/problems/the-tiny-miny/0

while(test_case > 0):
    int_number,int_power= [int(x) for x in input().split()]
    temp=0
    
    pow_store_list = []
    unsorted_list =[]
    final_unsorted_list =[]
    final_sorted_list = []
    
    for i in range(int_power):
        temp = pow(int_number, i+1)
        pow_store_list.append(temp)
    
    for i in pow_store_list:
        unsorted_list.append([int(j) for j in str(i)])
    
    for i in unsorted_list:
        for j in i:
            if j!=0:
                final_unsorted_list.append(j)
    
    final_sorted_list = sorted(final_unsorted_list, key=int)
    
    #print(pow_store_list)
    #print(unsorted_list)
    #print(final_unsorted_list)
    #print(final_sorted_list)
    
    for i in final_sorted_list:
        print(i, end="")
    print("")
    
    test_case -= 1