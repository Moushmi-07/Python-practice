def recperfect(n,f,t):
    if f < n and n % f == 0:
        t += f
    elif f == n and t == n:
        return True
    elif f > n:
        return False
    return recperfect(n,f+1,t)

def perfect(n):
    print(recperfect(n,1,0))
