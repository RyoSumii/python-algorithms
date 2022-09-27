class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, species):
        if species == "Cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeue_cat(self):
        if len(self.cats) == 0:
            return None
        else:
            cat = self.cats.pop(0)
            return cat

    def dequeue_dog(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog = self.dogs.pop(0)
            return dog

    def dequeue_any(self):
        if len(self.cats) == 0 and len(self.dogs) == 0:
            return "there are no cats and dogs"
        elif len(self.cats) == 0:
            result = self.dogs.pop(0)
        else:
            result = self.cats.pop(0)
        return result


que = AnimalShelter()
que.enqueue("Cat1", "Cat")
que.enqueue("Cat2", "Cat")
que.enqueue("dog1", "Dog")
que.enqueue("Cat3", "Cat")
que.enqueue("dog2", "Dog")
que.enqueue("dog3", "Dog")
print(que.dequeue_dog())







