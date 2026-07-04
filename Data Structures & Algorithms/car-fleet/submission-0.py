class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count = 0 

        #zip function merges two lists into tuples
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)


        fleets=1
        prev_time = (target-pair[0][0]) / pair[0][1]

        for i in range(1, len(pair)):
            curr_car = pair[i]
            curr_time = (target-curr_car[0]) / curr_car[1]

            if curr_time > prev_time:
                fleets+=1
                prev_time = curr_time

        return fleets





            







        