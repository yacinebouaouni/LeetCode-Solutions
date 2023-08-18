class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        Rqueue = deque()
        Dqueue = deque()
        for i, c in enumerate(senate):
            if c == 'R':
                Rqueue.append(i)
            else:
                Dqueue.append(i)
        
        while Rqueue and Dqueue:
            rTurn = Rqueue.popleft()
            dTurn = Dqueue.popleft()

            if rTurn < dTurn:
                Rqueue.append(rTurn + len(senate))
            else:
                Dqueue.append(dTurn + len(senate))

        return "Radiant" if Rqueue else "Dire"

