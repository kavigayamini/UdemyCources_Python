colors = ['red','green','blue','yellow','orange','purple','brown']

print(f'This is before  reversing {colors}')
colors.reverse()
print(f'This is after reversing {colors}')

numbers = [1,10,2,300,13,55,56]
print(f'This is afer reversing {numbers}')
numbers.reverse()
print(f'This is afer reversing {numbers}')

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)
