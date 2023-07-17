class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # the key to this problem is to realize that we can convert this
        # to a simple distance - time problem
        # If two cars reach the destination at the same time, they will form a group
        # If a car is supposed to reach the destination before another car
        # it will reach the destination with the slower car because of the condition
        # given in the question
        stack = []
        for car_position, car_speed in sorted(zip(position, speed), reverse=True):
            distance_from_target = target - car_position
            time_at_target = distance_from_target / car_speed
            if not stack:
                stack.append(time_at_target)
            else:
                if time_at_target > stack[-1]:
                    stack.append(time_at_target)
        return len(stack)