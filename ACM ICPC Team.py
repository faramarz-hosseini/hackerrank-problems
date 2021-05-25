from itertools import combinations
topics = [
    '11101',
    '10101',
    '11001',
    '10111',
    '10000',
    '01110',
]


def acm_team(topic):
    length = len(topic)
    nums = [i for i in range(1, length + 1)]
    combos = list(combinations(nums, 2))
    max_topics = 0
    max_teams = 1
    for topple in combos:
        attendee_1_subjects = topic[topple[0]-1]
        attendee_2_subjects = topic[topple[1]-1]
        known_topics = attendee_1_subjects.count('1')
        for i, n in enumerate(attendee_1_subjects):
            if n == '0':
                if attendee_2_subjects[i] == '1':
                    known_topics += 1
        if known_topics > max_topics:
            max_topics = known_topics
            max_teams = 1
        elif known_topics == max_topics:
            max_teams += 1

    result = [max_topics, max_teams]
    return result


print(acm_team(topics))
