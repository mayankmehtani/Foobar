def answer(l,t):
    # your code here
    for i in range(0,len(l)):
        sum = l[i]
        if sum == t:
            return [i,i]

        if sum > t:
            continue

        for j in range(i+1, len(l)):
            sum += l[j]
            if sum == t:
                return [i,j]
            
            if sum > t:
                break

    return [-1,1]
