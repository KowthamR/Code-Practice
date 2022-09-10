# Gries Chapter 9
# 9.16
rat_1_weight=[2,3,5,9,4]
rat_2_weight=[4,7,4,2,8]
week = 1
while rat_1_weight[week] / rat_1_weight[0] - 1 < .25:
 week += 1
print(week) 