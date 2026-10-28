class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ans = defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     ans[tuple(count)].append(s)
        # return list(ans.values())
        # for s in strs:
        #     for j in s:
        #         d[j] += d.get("")+j
        d ={}
        for s in strs:    
            k = "".join(sorted(s))
            d[k] = d.get(k,[])+[s]
        return list(d.values())