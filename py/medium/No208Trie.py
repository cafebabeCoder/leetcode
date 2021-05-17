class TrieNode(object):
    def __init__(self):
        self.is_leaf = False
        self.content = dict()

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        if word is None or len(word) == 0:
            return
        node = self.root
        for c in word:
            tmpNode = node.content.get(c)
            if tmpNode is None:
                print(c)
                tmpNode = TrieNode()
                node.content[c] = tmpNode
            node = tmpNode
        node.is_leaf = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word is None or len(word) == 0:
            return True
        node = self.root
        for c in word:
            tmpNode = node.content.get(c)
            if tmpNode is None:
                return False
            node = tmpNode
        return node.is_leaf


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if prefix is None or len(prefix) == 0:
            return
        node = self.root
        for c in prefix:
            tmpNode = node.content.get(c)
            if tmpNode is None:
                return False
            node = tmpNode
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("word")
print(obj.root.content.keys())
param_2 = obj.search("rwordr")
print(param_2)
param_3 = obj.startsWith("rwo")
print(param_3)