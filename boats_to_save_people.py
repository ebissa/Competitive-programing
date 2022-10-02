class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people=sorted(people)
        i=0
        boats=0
        j=len(people)-1
        while i<j:
            if people[j]==limit or (people[i]+people[j])>limit:
                boats+=1
                j-=1
            elif people[i]+people[j]<=limit:
                boats+=1
                j-=1
                i+=1
        if i==j:
            boats+=1
            
        return boats
