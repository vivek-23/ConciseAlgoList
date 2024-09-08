# Dutch National Flag Algorithm - Sort the array with 0s, 1s and 2s.

def sort012(self, arr):
    zeroes = i = 0
    twos = len(arr) - 1
    
    while i <= twos:
        if arr[i] == 0:
            arr[zeroes], arr[i] = arr[i], arr[zeroes]
            zeroes += 1
            i += 1
        elif arr[i] == 2:
            arr[twos], arr[i] = arr[i], arr[twos]
            twos -= 1
        else:
            i += 1
