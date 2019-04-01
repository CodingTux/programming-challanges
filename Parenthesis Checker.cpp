// Given an expression string exp. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
// For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”

// Input:
// The first line of input contains an integer T denoting the number of test cases.  Each test case consists of a string of expression, in a separate line.

// Output:
// Print 'balanced' without quotes if the pair of parenthesis is balanced else print 'not balanced' in a separate line.

// Constraints:
// 1 ≤ T ≤ 100
// 1 ≤ |s| ≤ 105

// Example:
// Input:
// 3
// {([])}
// ()
// ([]

// Output:
// balanced
// balanced
// not balanced

// ** For More Input/Output Examples Use 'Expected Output' option **
// https://practice.geeksforgeeks.org/problems/parenthesis-checker/0


#include <bits/stdc++.h>
using namespace std;

int checkParen(string paren){
        int pointerA=0;
        int pointerB=0;
        int pointerC=0;
      //  cout << paren.size() << endl;
        for(int i=0; i<paren.size(); ++i){
            if(paren[i] == '{'){
                pointerA++;
            }else if(paren[i] == '('){
                pointerB++;
            }else if(paren[i] == '['){
                pointerC++;
            }
            
            if(paren[i] == '}'){
                pointerA--;
            }else if(paren[i] == ')'){
                pointerB--;
            }else if(paren[i] == ']'){
                pointerC--;
            }
        }
        if(pointerC ==0 && pointerA ==0  && pointerB ==0  ){
            return 0;
        }else{
            return 1;
        }
     //   cout << pointer << endl;
}

int main(){
    int testcase;
    string paren;
    
    cin >> testcase;
    
     while(testcase > 0){
         
         cin >> paren;
    
            int ans;
            ans = checkParen(paren);
            
            if(ans==0){
                cout << "balanced" << endl;
            }else{
                cout << "not balanced" << endl;
            }
            
            testcase--;
    
     }
}