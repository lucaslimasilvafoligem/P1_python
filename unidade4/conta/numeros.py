nuns = int(input())
antes = 0
entre = 0
depois = 0


for ini in range(nuns):
    ns = input()

print('---')

a = int(input())
b = int(input())

#if ns < a:
#    antes += 1

if ns > a and ns < b:
    entre += 1

if ns > b:
    depois += 1

print('{antes} antes\n{entre} entre\n{depois} depois')

