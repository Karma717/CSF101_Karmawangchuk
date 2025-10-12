#define function as fibonacci and n value of our choice
def fibonacci(n):
    if n <= 1:  # setting basr case 
        return n
    else:    # if n > 1 than return an instance of prevoius two value of fibonacci number  
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7)) # than call the function