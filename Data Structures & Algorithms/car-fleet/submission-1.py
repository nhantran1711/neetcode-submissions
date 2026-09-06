class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(position)

        cars = [[0, 0]] * n
        
        for i in range(n):
            cars[i] = [position[i], speed[i]]
        
        sorted_cars = sorted(cars, key = lambda x:x[0], reverse = True)

        stack = []
        for i in range(n):
            pos, spe = sorted_cars[i]

            new_speed = (target - pos) / spe

            if not stack or new_speed > stack[-1]:
                stack.append(new_speed)

        return len(stack)

        
            