def trap(height) -> int:
    lmax = height[0]
    rmax = height[-1]
    l = 0
    r = len(height) - 1
    water = 0
    while (l < r):
        if (height[l] < height[r]):
            lmax = max(lmax, height[l])
            water += lmax - height[l]
            l += 1
        else:
            rmax = max(rmax, height[r])
            water += rmax - height[r]
            r -= 1
    return water

# height = [4,2,0,3,2,5]
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [1,8,6,2,5,4,8,3,7]
print(trap(height))