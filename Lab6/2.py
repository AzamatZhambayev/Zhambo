def generate_squares(x,y):
    for num in range(x, y+1):
        yield num**2
        
x=int(input())
y=int(input())
for num in range generate_squares(x,y):
    print(num)


    
    