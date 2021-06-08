t_room, t_cond = map(int, input().split())
mode = input()

if mode == 'auto':
    t_result = t_cond
elif mode == 'fan':
    t_result = t_room
elif mode == 'freeze':
    if t_room <= t_cond:
        t_result = t_room
    else:
        t_result = t_cond
else:
    if t_room >= t_cond:
        t_result = t_room
    else:
        t_result = t_cond

print(t_result)
    
