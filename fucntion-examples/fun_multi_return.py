def hour():
    n_hr = int(raw_input('enter number of hours: '))
    return n_hr
def day():
    n_dy = int(raw_input('enter number of days: '))
    return n_dy
def cost(h,d):
    c_rs = h*d*8
    return c_rs
h = hour()
d = day()
print 'Total cost is',cost(h,d)
