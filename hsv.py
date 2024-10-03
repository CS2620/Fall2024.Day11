def rgb_to_hsv(r,g,b):
    _max = max(r,g,b)
    _min = min(r,g,b)
    _diff = _max-_min
    
    # Black exception
    if _max == 0:
        return (0,0,0)
    
    v_255 = _max
    s_1 = _diff/_max
    
    if _diff == 0:
        hue_360 = 0
    else:
        if r == _max:
            hue_360 = 0 + 60*(g-b)/_diff
        elif g == _max:
            hue_360 = 120 + 60*(b-r)/_diff
        else:# b == _max:
            hue_360 = 240 + 60*(r-g)/_diff
        
    return (hue_360/360, s_1, v_255/255)

def hsv_to_rgb(h,s,v):
    _max = v
    _min = v - s * v
    _diff = (_max - _min)
    
    base_angle = 0
    if 1/6<h<=3/6:
        base_angle = 120
    if 3/6<h<5/6:
        base_angle = 240
        
    rotate_positive = True
    if 0<=h<1/6 or 2/6<=h<3/6 or 4/6<=h<5/6:
        rotate_positive = False
    if rotate_positive:
        _mid = (h*360-base_angle)*_diff/60+_min
    else:
        _mid = (base_angle-360*h)*_diff/60+_min
    
    
    
    if base_angle == 0:
        if rotate_positive:
            rgb_1 =  (_max, _mid, _min)
        else:
            rgb_1 =  (_max, _min, _mid)
    if base_angle == 120:
        if rotate_positive:
            rgb_1 =  (_min, _max, _mid)
        else:
            rgb_1 =  (_mid, _max, _min)
    if base_angle == 240:
        if rotate_positive:
            rgb_1 =  (_mid, _min, _max)
        else:
            rgb_1 =  (_min, _mid, _max)
            
    return (rgb_1[0]*255, rgb_1[1]*255, rgb_1[2]*255)

print(rgb_to_hsv(72, 96, 110))
print(hsv_to_rgb(0, 0, 0))
    
