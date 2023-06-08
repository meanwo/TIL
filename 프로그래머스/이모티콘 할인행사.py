def solution(users, emoticons):
    from itertools import product

    disc = [10, 20, 30, 40]
    min_disc = 50
    # min_disc2 = 50
    max_disc = 0
    # max_disc2 = 0
    for i in range(len(users)):
        min_disc = min(min_disc, users[i][0])
        max_disc = max(max_disc, users[i][0])
    for i in range(len(disc)):
        if min_disc <= disc[i]:
            min_disc2 = disc[i]
            break

    for i in range(len(disc)):
        if max_disc <= disc[i]:
            max_disc2 = disc[i]
            break

    target_disc = []
    for i in range(len(disc)):
        if disc[i] >= min_disc2 and disc[i] <= max_disc2:
            target_disc.append(disc[i])
    target_set = list(product(target_disc, repeat=len(emoticons)))
    answer = [0, 0]
    for i in range(len(target_set)):
        tmp_answer = [0, 0]
        # print(target_set[i])
        for j in range(len(users)):
            emo_fee = 0
            for k in range(len(emoticons)):
                if users[j][0] <= target_set[i][k]:
                    # print(emoticons[k]*(100-target_set[i][k])/100)
                    emo_fee += emoticons[k] * (100 - target_set[i][k]) / 100
            if emo_fee >= users[j][1]:
                tmp_answer[0] += 1
            else:
                tmp_answer[1] += emo_fee
            # print(target_set[i] ,tmp_answer)
            if tmp_answer[0] > answer[0]:
                answer = tmp_answer
            elif tmp_answer[0] == answer[0]:
                if tmp_answer[1] > answer[1]:
                    answer = tmp_answer

    print(answer)

    return answer