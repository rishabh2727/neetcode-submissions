import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use a dict to store the task and their frequency


        mydict = {}
        heap = []

        for t in tasks:
            if t not in mydict:
                mydict[t] = 1
            else:
                mydict[t] += 1

        for k,v in mydict.items():
            # now this is a max heap
            heapq.heappush(heap,(-v,k))
        
        # dry run:
        # A -> 3 idle spaces -> B -> C
        cycles = 0

# Heap = [(-2, 'X'), (-2, 'Y')]
# reduce the count, 

        while len(heap) > 0:
            # schedule the highest occuring task, subtract one and 
            # add the task back again once the whole iteration is done
            # so it is not scheduled again in its own idle space
            # then schedule for all idle spaces == n
            scheduled = []
            count = 0
            ran = 0
            while count < n+1:
                # if element left in heap, pop that element, schedule
                # that task, update its count and put it in the heap again
                # but now if B is scheduled, we cannot choose that again.
                if len(heap) > 0:
                    t_count, task = heapq.heappop(heap)
                    t_count += 1
                    ran += 1
                    if t_count < 0:
                        scheduled.append((t_count,task))

                # else condition means heap is empty, so it will have to
                # be idle for the remaining n cycles.
                count += 1
            
            if scheduled:
                cycles += n + 1
            else:
                cycles += ran

            for tasks in scheduled:
                # tasks is like (-2,'X')
                heapq.heappush(heap,tasks)
           
        return cycles
        
        # need to know how many idle spaces are created if we have
        # X = 2, and n = 2, two spaces, if Y = 3, and n = 2, 
        # then 3 spaces, and so on.

        # so try to start with the highest occring task 

        

        



        # while we are done with all the tasks, we keep going through
        # the tasks array, 
        # how to schedule a task:
        # means process it, reduce the count, and put it cooling down queue







        

        







        