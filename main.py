m = [0]*(4500000+1)
m[4500000] =  1
for i in range(4500000-1,2000000-1,-1):
    if i + 5 <= 4500000:
        m[i] += m[i + 5]
    if i * 2 <= 4500000:
        m[i] += m[i * 2]
    if i * 3 <= 4500000:
        m[i] += m[i * 3]
    if i * 3 + 1 <= 4500000:
        m[i] += m[i * 3 + 1]
    if i * 3 + 2 <= 4500000:
        m[i] += m[i * 3 + 2]
    if i * 5 <= 4500000:
        m[i] += m[i * 5]
    if i * 5 + 1 <= 4500000:
        m[i] += m[i * 5 + 1]
    if i * 5 + 2 <= 4500000:
        m[i] += m[i * 5 + 2]
    if i * 5 + 3 <= 4500000:
        m[i] += m[i * 5 + 3]
    if i * 5 + 4 <= 4500000:
        m[i] += m[i * 5 + 4]
m2 = [0]*(2000000+1)
m2[2000000] =  1
for i in range(2000000-1,0-1,-1):
    if i + 5 <= 2000000:
        m2[i] += m2[i + 5]
    if i * 2 <= 2000000:
        m2[i] += m2[i * 2]
    if i * 3 <= 2000000:
        m2[i] += m2[i * 3]
    if i * 3 + 1 <= 2000000:
        m2[i] += m2[i * 3 + 1]
    if i * 3 + 2 <= 2000000:
        m2[i] += m2[i * 3 + 2]
    if i * 5 <= 2000000:
        m2[i] += m2[i * 5]
    if i * 5 + 1 <= 2000000:
        m2[i] += m2[i * 5 + 1]
    if i * 5 + 2 <= 2000000:
        m2[i] += m2[i * 5 + 2]
    if i * 5 + 3 <= 2000000:
        m2[i] += m2[i * 5 + 3]
    if i * 5 + 4 <= 2000000:
        m2[i] += m2[i * 5 + 4]
print(m2[0]*m[2000000])