# Math - Problem #1

def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a%b)
responses = []
test_cases = int(input())
while(test_cases > 0):
    a, b = map(int, input().split())
    responses.append(str(mcd(a, b)))
    test_cases -= 1
    
print(*responses, sep="\n")

