#draw a diamond with a specified height as the parameter 
def draw_diamond(height):
    mid=height//2 
    #top half of the diamond including the middle line 
    for i in range (mid + 1):
        spaces= mid-i
        hashes=2*i+1
        print(' '*spaces+'#'*hashes)
    #bottom half of the diamond including the middle line 
    for i in range(mid-1,-1,-1):
        spaces=mid-i
        hashes=2*i+1
        print(' '*spaces+'#'*hashes)
draw_diamond(7)

def draw_right_triangle(height):
    #build each row of the right triangle 
    for i in range(1,1+ height):
        print('#'*i)
draw_right_triangle(7)

def compound_interest(p,r,y):
    amount=p
    #apply interest rate to each year 
    for _ in range(y):
        amount+=amount*r
    #round amount 2 decimal places 
    return round(amount,2)
print(compound_interest(10000,0.05,5))

def draw_hollow_square(size,thickness):
    for i in range(size):
        #draw entire rows for top and bottom edges 
        if i<thickness or i>=size-thickness:
            print('#'*size)
        #draw hollow rows with side edges 
        else:
            print('#'*thickness+' '*(size-2*thickness)+'#'*thickness)
draw_hollow_square(5,1)