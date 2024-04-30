
class Queue:
    def __init__(self, elements = [], sortingKey = lambda x: x, idKey = lambda x: x):
        self.elements = elements
        self.sortingKey = sortingKey
        self.idKey = idKey

    def print_queue(self):
        for i in self.elements:
            print(i)
    
    def empty(self):
        return not self.elements

    def put_s(self, items):
        for item in items:
            self.put(item)
    
    def put(self, item):
        for i in self.elements:
            if self.idKey(i) == self.idKey(item):
                if self.sortingKey(i) <= self.sortingKey(item):
                    return
                else:
                    self.elements.remove(i)

        self.elements.append(item)
        #self.remove_duplicates(item)
        self.elements = sorted(self.elements, key = self.sortingKey)
    
    def get(self):
        return self.elements.pop(0)

    def has_better_eq(self, state):
        for e in self.elements:
            if self.idKey(e) == self.idKey(state) and self.sortingKey(e) <= self.sortingKey(state):
                return True
        return False

    def get_by_key(self, key):
        for i in range(len(self.elements)):
            if self.idKey(self.elements[i]) == key:
                return self.elements.pop(i)
        return None

    def has(self, state):
        if state in list(map(self.idKey, self.elements)):
            return True
        return False

