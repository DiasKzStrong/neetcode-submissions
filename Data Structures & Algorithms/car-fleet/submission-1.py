class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]

        cars.sort(reverse=True, key=lambda x: x[0])

        stack = []
        res = 0

        for car in cars:
            pos, sp = car

            time = (target - pos)  / sp

            if stack and time <= stack[-1]:
                continue

            stack.append(time)
            res += 1 
        return res

