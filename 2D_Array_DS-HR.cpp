//QUESTION: Given a 6x6 2D Array, arr:

// 1 1 1 0 0 0
// 0 1 0 0 0 0
// 1 1 1 0 0 0
// 0 0 0 0 0 0
// 0 0 0 0 0 0
// 0 0 0 0 0 0
// We define an hourglass in 'A' to be a subset of values with indices falling in this pattern in arr's graphical representation:

// a b c
//   d
// e f g
// There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.

// For example, given the 2D array:

// -9 -9 -9  1 1 1 
//  0 -9  0  4 3 2
// -9 -9 -9  1 2 3
//  0  0  8  6 6 0
//  0  0  0 -2 0 0
//  0  0  1  2 4 0
// We calculate the following 16 hourglass values:

// -63, -34, -9, 12, 
// -10, 0, 28, 23, 
// -27, -11, -2, 10, 
// 9, 17, 25, 18
// Our highest hourglass value is 28 from the hourglass:

// 0 4 3
//   1
// 8 6 6
// Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

// Function Description

// Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.

// hourglassSum has the following parameter(s):

// arr: an array of integers
// Input Format

// Each of the  lines of inputs  contains  space-separated integers .
// Output Format
// Print the largest (maximum) hourglass sum found in .

// Sample Input
// 1 1 1 0 0 0
// 0 1 0 0 0 0
// 1 1 1 0 0 0
// 0 0 2 4 4 0
// 0 0 0 2 0 0
// 0 0 1 2 4 0
// Sample Output

// 19
// Explanation

// arr contains the following hourglasses:

// image (https://s3.amazonaws.com/hr-assets/0/1534256743-35b846ad4a-hourglasssum.png)

// The hourglass with the maximum sum () is:

// 2 4 4
//   2
// 1 2 4


#include <bits/stdc++.h>
using namespace std;

int hourglassSum(int arr[][6]){
    int answer;
    std::list<int> HourGlassSum;
    int GlassSum=0;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
                GlassSum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2];
                HourGlassSum.push_front(GlassSum);
        }
    }
    HourGlassSum.sort(std::greater<int>());
    // for (int n : HourGlassSum) {
    //     std::cout << n << '\n';
    // }
    answer = HourGlassSum.front();
    return answer;
                
}

int main(){
    int HourGlass[6][6];
    for(int i=0;i<6;i++)
        for(int j=0;j<6;j++)
            cin>>HourGlass[i][j];
    
    int MAX_GLASSHOUR = hourglassSum(HourGlass);
    
    cout<<MAX_GLASSHOUR;
    
}