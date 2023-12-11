import random

import itertools as it


def groupStage(teams_name):
    random.shuffle(teams_name)
    result = it.combinations(teams_name, 2)
    group_result = []
    for x in result:
        group_result.append(x)
    random.shuffle(group_result)
    return group_result
