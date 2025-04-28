name = ['Hong', 'Seong', 'Shim', 'Lee', 'Park']
kor = [74, 80, 62, 88, 56]
math = [68, 71, 54, 90, 61]
eng = [80, 59, 77, 76, 65]
sci = [70, 65, 50, 82, 73]

score = []
total = []
for i in range(len(name)): # Answer : len(name)
    total.append(kor[i] + math[i] + eng[i] + sci[i])
    score.append((total[i], total[i] / 4.0, name[i], kor[i], math[i], eng[i], sci[i]))

score.sort(key=lambda x: x[0], reverse=True) # Answer : score.sort(key=lambda x: x[0], reverse=True)
score = score[0:3] # Answer : score = score[0:3]
top_3 = score # Answer : top_3 = score
for t_score, avg, n, k, m, e, s in top_3:
    print(n, k, m, e, s, t_score, avg)