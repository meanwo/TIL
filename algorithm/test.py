import random

def Me(opp, turn, opp_prev, opp_last_pattern):
    candi = [0, 1, 2, 'RABBIT', 'SNAKE', 'DEER']
    if turn == 0:
        if opp_last_pattern[0] == 'DEER':
            return 1
        elif opp_last_pattern[0] == 2:
            return 0
        else:
            return 2
    elif turn == 1:
        if opp_last_pattern[1] == 'DEER':
            return 1
        elif not opp_last_pattern[1]:
            return 2
        else:
            return 2
    elif turn == 2:
        if opp_last_pattern[2] == 'DEER':
            return 1
        elif not opp_last_pattern[2]:
            return 2
        else:
            return 2
    elif turn == 3:
        if opp_last_pattern[3] == 'DEER':
            return 1
        elif not opp_last_pattern[3]:
            return 2
        else:
            return 2
    elif turn == 4:
        if opp_last_pattern[4] == 'DEER':
            return 1
        elif not opp_last_pattern[4]:
            return 2
        else:
            return 2
    elif turn == 5:
        if opp_last_pattern[5] == 'DEER':
            return 1
        elif not opp_last_pattern[5]:
            return 2
        else:
            return 2
    elif turn == 6:
        if opp_last_pattern[6] == 'DEER':
            return 1
        elif opp_last_pattern[6] == 'RABBIT':
            return 0
        else:
            return 0

    elif turn == 7:
        if opp_last_pattern[7] == 'DEER':
            return 1
        elif not opp_last_pattern[7]:
            return 2
        else:
            return 2
    elif turn == 8:
        if opp_last_pattern[8] == 'DEER':
            return 1
        elif not opp_last_pattern[8]:
            return 2
        else:
            return 2
    elif turn == 9:
        if opp_last_pattern[9] == 'DEER':
            return 1
        elif not opp_last_pattern[9]:
            return 2
        else:
            return 2


    opp_choices = []
    opp_choices.append(opp_last_pattern)
    deer_count = opp_choices.count(0)
    rabbit_count = opp_choices.count(1)
    snake_count = opp_choices.count(2)

    if turn == 0:
        return random.randrange(1, 4)
    elif opp_prev == 0:
        return 2
    elif opp_prev == 1:
        if snake_count >= deer_count and snake_count >= deer_count:
            return 2
        else:
            return 0
    elif opp_prev == 2:
        if deer_count > rabbit_count and deer_count > snake_count:
            return 0
        else:
            return 1
