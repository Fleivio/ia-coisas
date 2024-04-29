
class Queue:
    def __init__(self, elements = [], sortingKey = lambda x: x, idKey = lambda x: x):
        self.elements = elements
        self.sortingKey = sortingKey
        self.idKey = idKey

    def __str__(self):
       return f'{[str(a) for a in self.elements]}'
    
    def empty(self):
        return not self.elements

    def put_s(self, items):
        for item in items:
            self.put(item)
    
    def put(self, item):
        self.elements.append(item)
        self.remove_duplicates(item)
        self.elements = sorted(self.elements, key = self.sortingKey)
    
    def get(self):
        return self.elements.pop(0)

    def remove_duplicates(self, state):
        def is_better(s1):
            return self.sortingKey(s1) >= self.sortingKey(state)
        
        find_itself = False
        for i in range(len(self.elements)-1, -1, -1):
            e = self.elements[i]
            if self.idKey(e) == self.idKey(state) and is_better(e):
                if not find_itself and self.sortingKey(e) == self.sortingKey(state):
                    find_itself = True
                    continue
                self.elements.pop(i)

