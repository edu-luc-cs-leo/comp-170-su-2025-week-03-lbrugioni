def draw_diamond(height):
    mid=height//2
    for i in range (mid + 1):
        spaces= mid-i
        hashes=2*i+1
        print(' '*spaces+'#'*hashes)
    for i in range(mid-1,-1,-1):
        spaces=mid-i
        hashes=2*i+1
        print(' '*spaces+'#'*hashes)
draw_diamond(7)

def draw_right_triangle(height):
    for i in range(1,1+ height):
        print('#'*i)
draw_right_triangle(7)

def compound_interest(p,r,y):
    amount=p
    for _ in range(y):
        amount+=amount*r
    return round(amount,2)
print(compound_interest(10000,0.05,5))

def draw_hollow_square(size,thickness):
    for i in range(size):
        if i<thickness or i>=size-thickness:
            print('#'*size)
        else:
            print('#'*thickness+' '*(size-2*thickness)+'#'*thickness)
draw_hollow_square(5,1)

