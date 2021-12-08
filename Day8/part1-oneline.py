print(sum(1 for line in open('input.txt').readlines() for x in line.strip().split(' | ')[1].split() if len(x) in [2,3,4,7]))
