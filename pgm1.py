# PROBLEM STATEMENT
# Stage: https://www.hackerearth.com

# Harry was contesting to be the most stylist person in his college. He had to collect maximum points from the judges to be able to win. However there was a problem. The judges were sitting in a line and each pair of adjacent judges had ego issues with each other. So if one judge gave X points to Harry then the next judge won’t give him any points. Harry had a friend in the organizing team and through him he had found out the exact points he would get from each judge if he chose their score to be considered. Help him find out the maximum points he can score.

# INPUT
# The first line of input contains the number of test cases, T.
# 0 < T < = 10
# Each test case starts with a number N, the number of judges.
# 0 <= N < = 10^4.
# The next line will have N numbers, number of points each judge gave Harry
# 0 < = X(i) < = 10^9.
# The order of the judges does not change.

# OUTPUT
# For each test case print “Case T: A” without quotes in a single line.
# T is the case number, starting with 1.
# A is the maximum number of points Harry can collect.

# SAMPLE INPUT:
# 2
# 5
# 1 2 3 4 5
# 1
# 10

# SAMPLE OUTPUT:
# Case 1: 9
# Case 2: 10

# CUSTOM TestCase I/P:
# 



Max_Scores = []
rounds = int(input())

for i in range(rounds):
    no_of_judges = int(input())
    score_of_all_judges =  a = [int(x) for x in input().split()]
    sum1 = sum(score_of_all_judges[::2]) # Calculate the score of even seated judges
    sum2 = sum(score_of_all_judges[1::2]) # Calculate the score of even seated judges
    if sum1 > sum2:
        Max_Scores.append(sum1)
    else:
        Max_Scores.append(sum2)

for i in range(len(Max_Scores)):
    print("Case {}: {}".format(i+1, Max_Scores[i]))

3
7
7 4 3 2 1 5 6
6
9 1 8 5 1 12
7
7 6 5 4 3 2 1
