class TimeMap:

    def __init__(self):
        self.t_KV = {}
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        print(key, value, timestamp)
        if key in self.t_KV and key in self.times:
            val =  self.t_KV[key]
            val[timestamp] = value
            
            self.t_KV[key] = val
            key_times = self.times[key]
            key_times.append(timestamp)
            self.times[key] = key_times

        else:
            self.t_KV[key] = {timestamp: value}
            self.times[key] = [timestamp]
            
    def get(self, key: str, timestamp: int) -> str:
        if key in self.t_KV and timestamp in self.t_KV[key]:
            return self.t_KV[key][timestamp]

        if key not in self.times or not self.times[key]:
            return ""
        
        target = timestamp
        nums = self.times[key]
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        if left == 0:
            return ""

        t = nums[left - 1]
        return self.t_KV[key][t]

