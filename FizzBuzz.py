class Solution:
    def fizzBuzz(self, n):
        list=[]
        for i in range(1,n+1):
            if i%3==0 and not(i%5==0):
                list.append('Fizz')
            elif i%5==0 and not(i%3==0):
                list.append('Buzz')
            elif i%3==0 and i%5==0:
                    list.append('FizzBuzz')
            else:
                list.append(str(i))
        return list
                
