def tri_distance(focal_l, base, disparity):
    f = focal_l/1000
    b = base/100
    d = disparity/1000
    if d == 0:
        return float('int')
    Z = (f*b) / d
    return Z

focal_l = 6
base = 15
disparity = 3

distance = tri_distance(focal_l,base, disparity)
print(f"Object is {distance:.2f} meter away.")