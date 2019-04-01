# Given three strings A, B and C your task is to complete the function isInterleave which returns true if C is an interleaving of A and B else returns false. C is said to be interleaving A and B, if it contains all characters of A and B and order of all characters in individual strings is preserved.

# Input:
# The first line of input contains an input T denoting the no of test cases. Then T test cases follow. Each test case contains three space separated strings A, B, C.

# Output:
# For each test case output will be 1 if C is interleaving of string A and B else 0.

# Constraints:
# 1<=T<=100
# 1<=length of A, B, C <=100

# Example(To be used only for expected output):
# Input:
# 2
# YX  X  XXY
# XY X XXY

# Output
# 0
# 1

# Explanation:
# 1. For first test case XXY is not interleaving of YX and X
# 2. For the sec test case XXY is interleaving of XY and X.

# Note:The Input/Ouput format and Example given are used for system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from stdin/console. The task is to complete the function specified, and not to write the full code.

# ** For More Input/Output Examples Use 'Expected Output' option **
# https://practice.geeksforgeeks.org/viewSol.php?subId=13122718&pid=700353&user=Anurag_IS


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#Your task is to complete this Function \
#function should return True/False
def isInterleave(A, B, C):
    # Code here
    if len(A) == len(B) == len(C) == 0:
        return True
    else:
        return ((len(A) > 0 and len(C) > 0) and A[0] == C[0] and isInterleave(A[1:], B, C[1:])
        or ((len(B) > 0 and len(C) > 0) and B[0] == C[0] and isInterleave(A, B[1:], C[1:])))
 