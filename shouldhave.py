numbers=[1,2,56,32,51,2,8,92,15]
print(numbers)
i = 0
N = int(len(numbers))

while i < N-1:
    j=0
    while j < N-i-1:
        #if numbers[j] > numbers[j+1]:
            temp = numbers[j+1]
            numbers[j+1]=numbers[j]
            numbers[j]=temp
            j = j+1
    else:
        j = j+1
else:
    print(numbers)