class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute force: Loop through entire array, add value to dict maintaining number of occurrences.
        # Sort in descending order by key at the end and return top k.
        occurrence_dict = {}
        for i in nums:
            if i not in occurrence_dict:
                occurrence_dict[i] = 1
            else:
                occurrence_dict[i] += 1
        print(occurrence_dict)
        sorted_dict = dict(sorted(occurrence_dict.items(), key=lambda x:x[1], reverse=True))
        print(sorted_dict)
        print(list(sorted_dict))
        return list(sorted_dict)[:k]
