"""
Input

The first line contains an integer 𝑡
(1≤𝑡≤104

) — the number of test cases.

The first line of each test case contains two integers 𝑛
and 𝑞 (1≤𝑛≤105,1≤𝑞≤5⋅104

).

The following line contains 𝑛
integers 𝑎1,𝑎2,…,𝑎𝑛 (2≤𝑎𝑖≤105

).

The following 𝑞
lines each contain three integers 𝑘, 𝑙, and 𝑟 (1≤𝑘≤105,1≤𝑙≤𝑟≤𝑛

).

It is guaranteed that the sum of 𝑛
does not exceed 105 over all test cases, and the sum of 𝑞 does not exceed 5⋅104 over all test cases.
"""



def f(k, a, l, r):
    ans = 0
    for i in range(l, r + 1):
        while k % a[i] == 0:
            k //= a[i]
        ans += k
    return ans


testfile = "testcodeforce.txt"
def test():
    with open(testfile, "r") as f:
        lines = f.readlines()
    
    t = int(lines[0].strip())
    index = 1
    results = []
    
    for _ in range(t):
        n, q = map(int, lines[index].strip().split())
        index += 1
        a = list(map(int, lines[index].strip().split()))
        index += 1
        
        for __ in range(q):
            k, l, r = map(int, lines[index].strip().split())
            index += 1
            result = f(k, a, l - 1, r - 1)
            results.append(result)
    
    return results

