class PlateStack(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return self.stacks

    def push(self, item):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    def pop_at(self, stack_num):
        if len(self.stacks[stack_num]) > 0:
            return self.stacks[stack_num].pop()
        else:
            return None


ps = PlateStack(5)
ps.push(1)
ps.push(2)
ps.push(2)
ps.push(2)
ps.push(2)
ps.push(2)
ps.push(2)
ps.push(2)
ps.push(2)
ps.push(2)
ps.pop_at(0)
print(ps.stacks)

