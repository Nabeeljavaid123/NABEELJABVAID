from itertools import count

tuple1=(1,2,3,4,5,6,7,8,8,9)
tuple2=(10,11,12,13,14,15,16,17,18,)
combine=tuple1+tuple2
print(combine)
tuple1=('hello',)
repeated=tuple1*3
print(repeated)
numbers=(1,2,3,4,5,6,7,8,8,9)
print(numbers[1:6])
print(numbers[:5])
print(numbers[7:])
tuple=('apple','banana','orange','apple')
print(tuple.count('apple'))
print(tuple.index('orange'))
for num in range(5):
    if num==3:
     break
     print(num)

      for i in range(6):
          if i==3:
              continue
              print(i)

