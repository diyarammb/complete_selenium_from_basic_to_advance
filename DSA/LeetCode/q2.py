def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        set_nums = set(nums)
        missing = []

        for i in range(1,len(nums)+1):
            if i not in set_nums:
                missing.append(i)

        return missing

findDisappearedNumbers(4,)

# Do upvote if you like it