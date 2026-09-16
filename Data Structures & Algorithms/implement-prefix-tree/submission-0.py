class PrefixTree:

    class Node():
        def __init__(self, val: str):
            self.val = val
            self.cache = {}
            self.children = []
            self.counter = 0

    def __init__(self):
        self.root = self.Node("root")
        

    def insert(self, word: str) -> None:
        curr = self.root

        word += "."

        for i in range(0, len(word)):
            if word[i] in curr.cache:
                idx = curr.cache[word[i]]
                curr = curr.children[idx]

            else: 
                new_node = self.Node(word[i])
                curr.children.append(new_node)
                curr.cache[word[i]] = curr.counter
                curr.counter += 1
                curr = new_node

    def search(self, word: str) -> bool:
        curr = self.root

        for i in range(0, len(word)):
            if word[i] in curr.cache:
                idx = curr.cache[word[i]]
                curr = curr.children[idx]
            else:
                return False
        
        if len(curr.cache) > 0 and "." not in curr.cache:
            return False

        return True
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for i in range(0, len(prefix)):
            if prefix[i] in curr.cache:
                idx = curr.cache[prefix[i]]
                curr = curr.children[idx]
            else:
                return False

        return True
        
        