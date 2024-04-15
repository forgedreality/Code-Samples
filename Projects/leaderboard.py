# climbing the leaderboard (binary search)

def climbingLeaderboard(ranked, player):
    result = []
    scores = [ranked[0]]
    tmp = ranked[0]

    for i in range(1,len(ranked)) :
        if ranked[i] != tmp:
            scores.append(ranked[i])
            tmp = ranked[i]

    for p in player:
        left, right, center = 0, len(scores) - 1, None
        while left <= right:
            center = left + ((right - left) // 2)
            if scores[center] == p:
                result.append(center + 1)
                break
            else:
                if p > scores[center]:
                    right = center - 1
                else:
                    left = center + 1
        if scores[center] != p:
            result.append(left + 1)

    return result

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))