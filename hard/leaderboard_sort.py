from unittest import TestCase

"""
Leaderboard Sort

Given an array of users, each defined by an object with the following 
properties: name, score, reputation create a function that 
sorts the array to form the correct leaderboard.

The leaderboard takes into consideration the score of each user of course, 
but an emphasis is put on their reputation in the community, 
so to get the trueScore, you should add the reputation multiplied by 2 to the score.

Once you know the trueScore of each user, sort the array according to it in descending order.

Examples

leaderboards([
  { "name": "a", "score": 100, "reputation": 20 },
  { "name": "b", "score": 90, "reputation": 40 },
  { "name": "c", "score": 115, "reputation": 30 },
]) ➞ [
  { "name": "c", "score": 115, "reputation": 30 },  # trueScore = 175
  { "name": "b", "score": 90, "reputation": 40 },   # trueScore = 170
  { "name": "a", "score": 100, "reputation": 20 }   # trueScore = 140
]

"""


def leaderboards(users):
    f = lambda user: user['score'] + 2 * user['reputation']
    return sorted(users, key=f, reverse=True)


TestCase().assertEqual(
    leaderboards([
        {'name': 'a', 'score': 100, 'reputation': 20},
        {'name': 'b', 'score': 90, 'reputation': 40},
        {'name': 'c', 'score': 115, 'reputation': 30},
    ]),
    [
        {'name': 'c', 'score': 115, 'reputation': 30},
        {'name': 'b', 'score': 90, 'reputation': 40},
        {'name': 'a', 'score': 100, 'reputation': 20},
    ]
)

TestCase().assertEqual(
    leaderboards([
        {'name': 'tkincaid0', 'score': 4128, 'reputation': 3002},
        {'name': 'sblackater1', 'score': 6208, 'reputation': 3050},
        {'name': 'ocallis2', 'score': 6883, 'reputation': 3812},
        {'name': 'shoofe3', 'score': 4900, 'reputation': 174},
        {'name': 'cbrazear4', 'score': 7862, 'reputation': 2940},
        {'name': 'oszachnie5', 'score': 6217, 'reputation': 1772},
        {'name': 'lingcourt6', 'score': 5746, 'reputation': 1263},
        {'name': 'tquincey7', 'score': 4209, 'reputation': 1419},
        {'name': 'mcapsey8', 'score': 6961, 'reputation': 2699},
        {'name': 'cbester9', 'score': 4090, 'reputation': 3934},
    ]),
    [
        {'name': 'ocallis2', 'score': 6883, 'reputation': 3812},
        {'name': 'cbrazear4', 'score': 7862, 'reputation': 2940},
        {'name': 'mcapsey8', 'score': 6961, 'reputation': 2699},
        {'name': 'sblackater1', 'score': 6208, 'reputation': 3050},
        {'name': 'cbester9', 'score': 4090, 'reputation': 3934},
        {'name': 'tkincaid0', 'score': 4128, 'reputation': 3002},
        {'name': 'oszachnie5', 'score': 6217, 'reputation': 1772},
        {'name': 'lingcourt6', 'score': 5746, 'reputation': 1263},
        {'name': 'tquincey7', 'score': 4209, 'reputation': 1419},
        {'name': 'shoofe3', 'score': 4900, 'reputation': 174},
    ]
)

TestCase().assertEqual(
    leaderboards([
        {'name': 'kdavet0', 'score': 8680, 'reputation': 3149},
        {'name': 'rollerearn1', 'score': 7127, 'reputation': 968},
        {'name': 'hcastel2', 'score': 8375, 'reputation': 1650},
        {'name': 'mslorach3', 'score': 8097, 'reputation': 1925},
        {'name': 'hseefus4', 'score': 5526, 'reputation': 1747},
        {'name': 'ddiggles5', 'score': 7519, 'reputation': 3433},
        {'name': 'estalman6', 'score': 8516, 'reputation': 755},
        {'name': 'eklemt7', 'score': 8487, 'reputation': 3289},
        {'name': 'eskitch8', 'score': 7762, 'reputation': 329},
        {'name': 'jroos9', 'score': 6288, 'reputation': 3043},
    ]),
    [
        {'name': 'eklemt7', 'score': 8487, 'reputation': 3289},
        {'name': 'kdavet0', 'score': 8680, 'reputation': 3149},
        {'name': 'ddiggles5', 'score': 7519, 'reputation': 3433},
        {'name': 'jroos9', 'score': 6288, 'reputation': 3043},
        {'name': 'mslorach3', 'score': 8097, 'reputation': 1925},
        {'name': 'hcastel2', 'score': 8375, 'reputation': 1650},
        {'name': 'estalman6', 'score': 8516, 'reputation': 755},
        {'name': 'rollerearn1', 'score': 7127, 'reputation': 968},
        {'name': 'hseefus4', 'score': 5526, 'reputation': 1747},
        {'name': 'eskitch8', 'score': 7762, 'reputation': 329},
    ]
)

TestCase().assertEqual(
    leaderboards([
        {'name': 'jlordon0', 'score': 7775, 'reputation': 789},
        {'name': 'srosenshine1', 'score': 5055, 'reputation': 3928},
        {'name': 'wendrighi2', 'score': 8039, 'reputation': 3519},
        {'name': 'rburt3', 'score': 5944, 'reputation': 3451},
        {'name': 'mgreest4', 'score': 7333, 'reputation': 2452},
        {'name': 'khugues5', 'score': 5304, 'reputation': 2465},
        {'name': 'bhazeman6', 'score': 4164, 'reputation': 3203},
        {'name': 'vcauson7', 'score': 4918, 'reputation': 3781},
        {'name': 'ffarrears8', 'score': 6438, 'reputation': 1929},
        {'name': 'jtwamley9', 'score': 4690, 'reputation': 3731},
    ]),
    [
        {'name': 'wendrighi2', 'score': 8039, 'reputation': 3519},
        {'name': 'srosenshine1', 'score': 5055, 'reputation': 3928},
        {'name': 'rburt3', 'score': 5944, 'reputation': 3451},
        {'name': 'vcauson7', 'score': 4918, 'reputation': 3781},
        {'name': 'mgreest4', 'score': 7333, 'reputation': 2452},
        {'name': 'jtwamley9', 'score': 4690, 'reputation': 3731},
        {'name': 'bhazeman6', 'score': 4164, 'reputation': 3203},
        {'name': 'ffarrears8', 'score': 6438, 'reputation': 1929},
        {'name': 'khugues5', 'score': 5304, 'reputation': 2465},
        {'name': 'jlordon0', 'score': 7775, 'reputation': 789},
    ]
)
