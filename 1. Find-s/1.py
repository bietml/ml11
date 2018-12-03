import csv
n = 6	# number of attributes
a = [ ]
print("\n The Given Training Data Set \n")
with open('tennis.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        a.append(row)
        print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * n
print(hypothesis)

# Comparing with First Training Example
for j in range(0,n): hypothesis[j] = a[0][j];
# Comparing with Remaining Training Examples of Given Data Set
for i in range(0, len(a)):
    if a[i][n] == 'TRUE':
        for j in range(0, n):
            if a[i][j] != hypothesis[j]:
                hypothesis[j] = '?'
            else:
                hypothesis[j] = a[i][j]

print("\n The Maximally Specific Hypothesis for a given Training Examples :\n")
print(hypothesis)
