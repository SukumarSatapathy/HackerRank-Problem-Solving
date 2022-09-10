A pangram is a string that contains every letter of the alphabet. Given a
sentence determine whether it is a pangram in the English alphabet. Ignore
case. Return either pangram or not pangram as appropriate.

Example
S = 'The quick brown fox jumps over the lazy dog'
The string contains all letters in the English alphabet, so return pangram.

Function Description
Complete the function pangrams in the editor below. It should return the string
pangram if the input string is pangram. Otherwise, it should return not
pangram.
pangrams has the following parameter(s):
string S: a string to test

Returns
string: either pangram or not pangram

Input Format
A single line with string s.

Constraints
0 < length of s < 103
Each character of s, sli] E {a z, A Z, space}

Sample Input 0
We promptly judged antique ivory buckles for the next prize

Sample Output 0
pangram

Sample Explanation 0
All of the letters of the alphabet are present in the string.

Sample Input 1
We promptly judged antique ivory buckles for the prize

Sample Output 1
not pangram

Sample Explanation 0
The string lacks an X.
