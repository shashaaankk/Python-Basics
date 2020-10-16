def fibb(end_num):
    prev_num=0
    next_num=1
    fibb_list=[prev_num,next_num]
    for count in range(1,end_num):
        fibb_num=prev_num+next_num
        fibb_list.append(fibb_num)
        prev_num=next_num
        next_num=fibb_num
    return fibb_list

print(fibb(5))
