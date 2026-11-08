class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def timeTo(pos):
            return (target - pos)/SpeedMap[pos]
        
        SpeedMap = {position[x]:speed[x] for x in range(len(position))}  
        position.sort()
        fleets = []

        while position:
            pos = position.pop()
            time = timeTo(pos)
            if not fleets:
                fleets.append(time)
                lasttime = time
            else:
                if time <= lasttime:
                    continue
                else:
                    fleets.append(time)
                    lasttime = time

        return len(fleets)

