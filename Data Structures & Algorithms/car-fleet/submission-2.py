class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk  = []
        car = list(zip(position, speed))
        car.sort(reverse=True)
        print(car)
        for pos,spd in car:
            time = (target - pos) / spd
            print(pos)
            
            if not stk or stk[-1] < time:
                stk.append(time)


        return len(stk)
            



            



