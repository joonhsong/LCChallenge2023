class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        player = []
        dp = []
        for i in range(len(scores)):
            player.append([scores[i], ages[i]])
        player.sort()
        for i in range(len(scores)):
            dp.append(player[i][0])
        for i in range(1,len(scores)):
            for j in range(i-1,-1,-1):
                if player[j][1]<=player[i][1]:
                    dp[i] = max(dp[i],player[i][0]+dp[j])

        return max(dp)