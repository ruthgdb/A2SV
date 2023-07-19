class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # dp[index][combination of skills] = [list of people]
        # dp[i] = [min(dp[i-1][j || people[i]] + 1, dp[i-1][j]) for all possible j]
        skill_to_ind_dict = defaultdict(int)
        for index, skill in enumerate(req_skills):
            skill_to_ind_dict[skill] = index + 1
        max_possible = (1 << len(req_skills)) - 1
        
        dp = [[] for i in range(2 ** len(req_skills))] 
        for i, skills in enumerate(people):
            skill_set = 0
            for skill in skills:
                if skill in skill_to_ind_dict:
                    skill_set |= (1 << (skill_to_ind_dict[skill] - 1))
            for j in range(max_possible):
                new_count = dp[j] + [i]
                new_pos = j | skill_set
                if j != 0 and len(dp[j]) == 0 or new_pos == 0:
                    continue
                if len(dp[new_pos]) == 0 or len(dp[new_pos]) > len(new_count):
                    dp[new_pos] = new_count
        return dp[-1]