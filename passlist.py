def count(lst):
    even=0
    odd=0
    for i in lst:
      if i%2==0:
        even+=1
      else:
        odd+=1
    return even,odd
lst=[20,30,14,26,45,78,56,12]
even,odd=(count(lst))
print(even)
print(odd)


print("even :{}and odd:{}". format(even,odd))
