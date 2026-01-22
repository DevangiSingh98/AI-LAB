import queue

def puzzle(start,goal):
    start = tuple(start)
    goal = tuple(goal)

    q = queue.Queue()
    q.put(start)

    visited = set()
    visited.add(start)

    explored = 0

    while not q.empty():
        state= q.get()
        explored +=1

        if state == goal:
            return explored

        blank= state.index(0)
        row= blank // 3
        col= blank % 3

        
        for dr, dc in [(-1,0),(1,0),(0,-1), (0,1)]:
            r = row + dr
            c = col + dc

            if 0<=r<3 and 0<=c<3:
                newblank = r * 3 + c
                newstate = list(state)

                temp = newstate[blank]
                newstate[blank] = newstate[newblank]
                newstate[newblank] = temp

                newstate = tuple(newstate)

                if newstate not in visited:
                    visited.add(newstate)
                    q.put(newstate)

    return -1



start = [7, 2, 4,
         5, 0, 6,
         8, 3, 1]

goal = [0, 1, 2,
        3, 4, 5,
        6, 7, 8]

print(puzzle(start, goal))

