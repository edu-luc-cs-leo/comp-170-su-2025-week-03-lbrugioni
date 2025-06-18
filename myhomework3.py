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

