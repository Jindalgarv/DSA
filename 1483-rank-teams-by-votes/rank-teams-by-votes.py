class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        m=len(votes[0])
        rank={ch: [0]*m for ch in votes[0]}
        for vote in votes:
            for i,ch in enumerate(vote):
                rank[ch][i]+=1
        teams=list(rank)
        teams.sort(key=lambda ch: ([-x for x in rank[ch]],ch ))
        return ''.join(teams)
        