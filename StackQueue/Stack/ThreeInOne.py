class MultiStack:
    def __init__(self, stack_size):
        self.number_stacks = 3
        self.custom_list = [0] * (stack_size * self.number_stacks)
        self.sizes = [0] * self.number_stacks
        self.stack_size = stack_size

    def isFull(self, stack_num):
        if self.sizes[stack_num] == self.stack_size:
            return True
        else:
            return False

    def isEmpty(self, stack_num):
        if self.sizes[stack_num] == 0:
            return True
        else:
            return False

    def indexOfTop(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1

    def push(self, item, stack_num):
        if self.isFull(stack_num):
            return "The stack is full"
        else:
            self.sizes[stack_num] += 1
            self.custom_list[self.indexOfTop(stack_num)] = item

    def pop(self, stack_num):
        if self.isEmpty(stack_num):
            return " The stack is empty"
        else:
            value = self.custom_list[self.indexOfTop(stack_num)]
            self.custom_list[self.indexOfTop(stack_num)] = 0
            self.sizes[stack_num] -= 1
            return f"{value} is removed"

    def peak(self, stack_num):
        if self.isEmpty(stack_num):
            return " The stack is empty"
        else:
            value = self.custom_list[self.indexOfTop(stack_num)]
            return value


a = MultiStack(3)
print(a.sizes)
print(a.custom_list)
a.push("item", 0)
print(a.custom_list)






