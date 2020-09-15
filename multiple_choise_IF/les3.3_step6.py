passw = input()
check = input()

if passw == check and len(passw) >= 7:
    print("OK")
elif len(passw) < 7:
    print('Short')
else:
    print('Difference')
