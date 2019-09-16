class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        nums=sorted(nums,reverse = True)[:k]
        self.nums = nums[::-1]
        heapq.heapify(self.nums)
        if k<=len(self.nums):
            self.last = heapq.heappop(self.nums)
        else:
            self.last = float('-inf')
        self.k = k

    def add(self, val: int) -> int:
        if self.last> val:
            return self.last
        self.last = heapq.heappushpop(self.nums, val)
        return self.last


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)