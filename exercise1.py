N = input("Enter the N value: ")
oddSum=0
evenSum=0
for i in range(1, int(N)+1):
      if(i%2==0):
            evenSum+=i
      else:
            oddSum+=i
print("Sum of the odd numbers:", oddSum)
print("Average of the even numbers:", (evenSum)/int(N))