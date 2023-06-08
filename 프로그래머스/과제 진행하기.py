#
# def solution(plans):
#     new_plans = []
#     for i in range(len(plans)):
#         start_time = (int(plans[i][1][0:2]) + float(plans[i][1][3:5]) / 60)
#         spend_time = int(plans[i][2]) / 60
#         end_time = start_time + spend_time
#         new_plans.append([plans[i][0], start_time, spend_time, end_time])
#     new_plans2 = sorted(new_plans, key=lambda x: x[1])
#     print(new_plans2)
#     answer = []
#     for i in range(len(new_plans2) - 1):
#         for j in range(i + 1):
#             if new_plans2[j][3] > new_plans2[i + 1][1]:
#                 new_plans2[j][3] += new_plans2[i + 1][2]
#
#     new_plans3 = sorted(new_plans2, key=lambda x: x[3])
#
#     for i in range(len(new_plans3)):
#         answer.append(new_plans3[i][0])
#
#     return answer

#########################################################################
def solution(plans):
    new_plans = []
    for i in range(len(plans)):
        start_time = (int(plans[i][1][0:2]) + float(plans[i][1][3:5]) / 60)
        spend_time = int(plans[i][2]) / 60
        new_plans.append([plans[i][0], start_time, spend_time])
    new_plans2 = sorted(new_plans, key=lambda x: x[1])
    print(new_plans2)
    remain_list = []
    answer = []
    # for _ in range(len(new_plans2) - 1):
    for i in range(len(new_plans2)-1):
        if i == len(new_plans2)-1:
            print('a')
            # answer.append(new_plans2[0][0])
        else:
            target = new_plans2.pop(0)
            # tmp 다음 과제까지 남은 시간
            tmp = new_plans2[0][1] - target[1]
            if tmp >= target[2]:
                answer.append(target[0])
                if tmp > target[2]:
                    while tmp > 0:
                        if len(remain_list) > 0:
                            target2 = remain_list.pop()
                            # print(target2)
                            if tmp >= target2[2]:
                                tmp -= target2[2]
                                answer.append(target2[0])
                            else:
                                target2 = [target2[0], target2[1], target2[2] - tmp]
                                tmp = 0
                                remain_list.append(target2)
            else:
                remain_list.append([target[0], target[1], target[2] - tmp])
    print(new_plans2, 'a')
    print(remain_list, 'b')
    print(answer, 'c')
    for i in range(len(new_plans2)):
        answer.append(new_plans2[i][0])
    for i in range(len(remain_list)-1, -1, -1):
        answer.append(remain_list[i][0])
    # for i in range(len(remain_list)):
    #     answer.append(remain_list[i])

    return answer




solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]])
# solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]])