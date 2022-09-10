Letters in some of the SOS messages are altered by cosmic radiation
during transmission. Given the signal received by Earth as a string, s,
determine how many letters of the SOS message have been changed by
radiation.

Example
§ = 'SOSTOT'
The original message was sossos. Two of the message's characters
were changed in transit.

Function Description
Complete the marsExploration function in the editor below.
marsExploration has the following parameter(s);
string S. the string as received on Earth

Returns
int: the number of letters changed during transmission

Input Format
There is one line of input: a single string, s.

Constraints
≤ length of s ≤ 99
length of s modulo 3 = 0
§ will contain only uppercase English letters, asci[A-Z].

Sample Input 0
SOSSPSSQSSOR

Sample Output 0
3

Explanation 0
S = SOSSPSSQSSOR, and signal length |$| = 12. They sent 4 SOS
messages (i.e.: 12/3 = 4).

Expected signal: SOSSOSSOSSOS
Recieved signal: SOSSPSSQSSOR

Sample Input 1
SOSSOT

Sample Output 1
1

Explanation 1
S = SOSSOT, and signal length |s] = 6. They sent 2 SoS messages (i.e.: 6/3 = 2).
