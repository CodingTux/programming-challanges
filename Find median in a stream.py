# QUESTION: Given an input stream of N integers. The task is to insert these numbers into a new stream and find the median of the stream formed by each insertion of X to the new stream.

# Input:
# The first line of input contains an integer N denoting the number of elements in the stream. Then the next N lines contains integer x denoting the number to be inserted into the stream.
# Output:
# For each element added to the stream print the floor of the new median in a new line.
 
# Constraints:
# 1 <= N <= 106
# 1 <= x <= 106
 
# Example:
# Input:
# 4
# 5
# 15
# 1 
# 3
# Output:
# 5
# 10
# 5
# 4
 
# Explanation:
# Testcase 1:
# Flow in stream : 5, 15, 1, 3 
# 5 goes to stream --> median 5 (5) 
# 15 goes to stream --> median 10 (5, 15) 
# 1 goes to stream --> median 5 (5, 15, 1) 
# 3 goes to stream --> median 4 (5, 15, 1, 3) 
 

number_of_inputs=int(input())
median=1
median_list=[]
digit_store=[]
temp=[]
b=1
def calcMedian(a):
    a.sort()
    return st.median(a)
# INPUT
while(number_of_inputs > 0):
    num = int(input())
    digit_store.append(num)
    number_of_inputs=number_of_inputs-1
for i in digit_store:
    temp.append(i)
    median = calcMedian(temp)
    median_list.append(median)
median_list = list(map(int, median_list)) # CONVERT TO INT
# print(median_list,"\n")
for i in median_list:
    print(i)