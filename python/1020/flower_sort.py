dist_list=[0.4242640687119289, 0.5385164807134505, 0.6324555320336757, 0.8944271909999159, 0.905538513813742, 0.9055385138137411, 0.6403124237432846, 1.3152946437965904]

indexed_num=list(enumerate(dist_list))
print("Before sorting:", indexed_num)

sorted_indexed_num=sorted(indexed_num, key=lambda x: x[1])
print("After sorting:", sorted_indexed_num)