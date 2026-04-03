'''
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
'''

# 은지님풀이
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        dp = [0] * n
        # i 번째 집까지만 있을 때 최대 금액 

        # 집 건너뛰는 건 2개 까지가 최대이므로 0 ~ 3까지만 base case 설정 
        # ex) 2 7 9 3 1

        if n >= 1:
            dp[0] = nums[0]
        if n >= 2:
            dp[1] = max(dp[0], nums[1])
        if n >= 3:
            dp[2] = max(dp[0] + nums[2], nums[1])
        if n >= 4:
            dp[3] = max(dp[0] + nums[2], nums[1] + nums[3], nums[0] + nums[3])
            # 0 2 번째 vs 1 3 번째 vs 0 3 번째 
        
        if n >= 5:
            for i in range(4, len(nums)): 
                dp[i] = max(dp[i - 3] + nums[i], dp[i - 2] + nums[i], dp[i - 1])
                # 2개까지 최대 + 5번째 
                # 3개까지 최대 + 5번째
                # 4개까지 최대 

        return dp[n - 1]
    
# 서진이 풀이
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        점화식 1, 2 간격으로 털 수 있음
        N = n-1, n-2 를 비교해서 max를 구해야함
        대신 구할 때 현재 위치 비교
        현재값과 n-2값 더함 vs n-1 값중에 max갱신

              0 1 2  3  4
        dp = [2 7 11 11 12 ]
        2,3,4
        """

        dp = [0] * (len(nums))
        dp[0] = nums[0]
        # 제약조건: 1 <= nums.length <= 100
        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]

# 내풀이
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        num_1 = 0
        num_2 = 0

        for i in range(0, n):
            # n까지 홀수 인덱스만 더하기
            if i % 2 == 0:
                num_1 += nums[i]
            if i % 2 == 1:
                num_2 += nums[i]
        return max(num_1, num_2)


# I: list 각 집의 돈
# O: 털 수 있는 돈의 최대합
# 조건: 인접한 집은 털 수 없음, 정렬 안됨
# 숫자 배열의 인접하지 않은 요소들의 최대 합
# 돈의 합을 구한다
# base case:

'''
집 1개: 0 홀
집 2개: 0 vs 1 짝
집 3개: 152 0 2 vs 1  홀 
집 4개: 1528 0 2 vs 1 3 짝
집 5개: 15280 0 2 4 vs 1 3 홀
집 6개: 152804 0 2 4 vs 1 3 5 짝
홀일때 왼쪽이 하나 더 많음
짝일 때는 같음



'''        

