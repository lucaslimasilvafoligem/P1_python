subtra = int(15)

for i in range(list(subtra)-1):
    if int(subtra[i]) == int(subtra[i+1]):
        subtra -= 1
    #if subtra == subtra -=1:
        if subtra == -5:
            print(f"{subtra:.1f}")

