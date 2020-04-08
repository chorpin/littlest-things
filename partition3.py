# Uses python3
import sys
import itertools

def partition3(A):
    Sum = sum(A)
    if Sum%3 != 0:
        return 0
    else:
        Sum = int(Sum/3)
        A_reserve = A
        Pos = [[], [], []]
        Cluster = [[], [], []]
        for times in range(0, 2):
            dp = [[1]*(len(A)+1) for i in range(0, Sum+1)]
            for i in range(0, Sum+1):
                dp[i][0] = False
            for j in range(0, len(A)+1):
                dp[0][j] = True
            for i in range(1, Sum+1):
                for j in range(1, len(A)+1):
                    dp[i][j] = dp[i][j-1]
                    if i>= A[j-1]:
                        dp[i][j] = dp[i][j] or dp[i-A[j-1]][j-1]
                # Any elements in dp[Sum][Any] == True

            if dp[Sum][len(A)] == True :
                k = Sum
                while k > 0:
                    pos = dp[k].index(True)
                    Pos[times].append(pos-1)
                    k = k - A[pos-1]
                for p in Pos[times]:
                    Cluster[times].append(A[p])
                    del A[p]
        Cluster[2] = A
        return Cluster















if __name__ == '__main__':
    input = sys.stdin.readline()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

