nums = [1, 2, 3, -7, 8, 78, 45]
def sum_pos( nums ):
    for k in range ( 0 , len(nums) ):
        if nums[k] < 0:
            nums[k] = 0
    return sum ( nums )
    print (nums)
sum_pos
print ( nums )

#----------------------------

def dashed_line ( len, head = ' ' ):
    empty_str = ''
    space = ' '
    if head != empty_str:
        head = space + head + space
    print (head.center( len, '-' ))

dashed_line (50)
