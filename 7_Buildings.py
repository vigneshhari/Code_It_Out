'''
Question
Motu is a skydiver. Every time he jumps off an airplane, he tries to land on one of the highest available buildings in his premises. Given the heighti of all available buildings in the locality, calculate the number of buildings on which he can land.

Input 
First line contains an integer n denoting the total number of buildings in the area.
The second line contains n space-separated integers, where each integer i denotes the height of the ith building.

Output
Print the available number of buildings on a new line.


Sample Cases

Sample input  	|	Sample Output
6				|	
3 8 4 1 7 8		|	2

Explanation:
Here the buildings with height 8 has the maximum heights. As there are 2 such buildings, hence it is the answer.

Constraints

1 <= n <= 20000
1 <= height <= 1000000

'''

#Answer in Python 3

input()
a=list(map(int,input().split()))
print (a.count(max(a)))
