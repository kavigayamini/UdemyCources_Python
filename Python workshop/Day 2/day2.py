#import random

#roll=random.randint(1, 10)
#print(roll)
#print(f'You rolled {roll}')



tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)

n = 0
c= 0
while n > 0 :
    print('Lather')
    print('Rinse')
    c=c+1

print('Dry off!')
print(c)