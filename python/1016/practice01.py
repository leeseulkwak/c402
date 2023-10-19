'''
*****  *   *          **    *   *        *****  *****
*   *  *   *    *      *    *   *    *   *          *
*   *  *****           *    *****        *****  *****
*   *      *    *      *        *    *       *  *
*****      *         *****      *        *****  *****
'''
# print(f"*****\n*   *\n*   *\n*   *\n*****")
# print(f" **  \n  *  \n  *  \n  *  \n*****")
# print(f"*****\n    *\n*****\n*    \n*****")
# print(f"*****\n    *\n*****\n    *\n*****")
# print(f"*   *\n*   *\n*****\n    *\n    *")
# print(f"*****\n*    \n*****\n    *\n*****")
# print(f"*****\n*    \n*****\n*   *\n*****")
# print(f"*****\n*   *\n    *\n    *\n    *")
# print(f"*****\n*   *\n*****\n*   *\n*****")
# print(f"*****\n*   *\n*****\n    *\n*****")
# print(f"     \n  *  \n     \n  *  \n     ")

import datetime

bignum = {'0':["*****","*   *","*   *","*   *","*****"],
    '1':[" **  ","  *  ","  *  ","  *  ","*****"],
    '2':["*****","    *","*****","*    ","*****"],
    '3':["*****","    *","*****","    *","*****"],
    '4':["*   *","*   *","*****","    *","    *"],
    '5':["*****","*    ","*****","    *","*****"],
    '6':["*****","*    ","*****","*   *","*****"],
    '7':["*****","*   *","    *","*   *","    *"],
    '8':["*****","*   *","*****","    *","*****"],
    '9':["*****","*   *","*****","  *  ","*****"],
    's':["     ","  *  ","     ","  *  ","     "]}

now = datetime.datetime.now()

hh = now.hour
mm = now.minute
ss = now.second

# time = "042356"
time = "{}{}{}".format(hh,mm,ss)

# print(bignum[time[0]][0],bignum[time[1]][0],bignum['s'][0],bignum[time[2]][0],bignum[time[3]][0],bignum['s'][0],bignum[time[4]][0],bignum[time[5]][0])
# print(bignum[time[0]][1],bignum[time[1]][1],bignum['s'][1],bignum[time[2]][1],bignum[time[3]][1],bignum['s'][1],bignum[time[4]][1],bignum[time[5]][1])
# print(bignum[time[0]][2],bignum[time[1]][2],bignum['s'][2],bignum[time[2]][2],bignum[time[3]][2],bignum['s'][2],bignum[time[4]][2],bignum[time[5]][2])
# print(bignum[time[0]][3],bignum[time[1]][3],bignum['s'][3],bignum[time[2]][3],bignum[time[3]][3],bignum['s'][3],bignum[time[4]][3],bignum[time[5]][3])
# print(bignum[time[0]][4],bignum[time[1]][4],bignum['s'][4],bignum[time[2]][4],bignum[time[3]][4],bignum['s'][4],bignum[time[4]][4],bignum[time[5]][4])

print(time)
bigtext2=""

for i in[0,1,2,3,4,]:
    for j in [0,1,2,3,4,5,6,7]:
        if j in [2,5]:
            bigtext2+=bignum['s'][i]+" "
        else:
            bigtext2+=bignum[time[j]][i]+" "
    bigtext2+='\n'

print(bigtext2)