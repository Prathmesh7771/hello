def fact(n):
  if(n==0 | n==1):
   return 1
  else:
   r=n*fact(n-1)
   return r
print(fact(6))
print("See the above factorial as:")
print("is there anychnages")
print("see")