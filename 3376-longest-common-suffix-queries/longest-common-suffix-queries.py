class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        root = TrieNode()

        # check if idx1 is better than idx2
        def better(idx1, idx2):

            if idx2 == -1:
                return True

            if len(wordsContainer[idx1]) != len(wordsContainer[idx2]):
                return len(wordsContainer[idx1]) < len(wordsContainer[idx2])

            return idx1 < idx2

        # insert word into trie in reversed order
        def insert(word, idx):

            node = root

            if better(idx, node.best_idx):
                node.best_idx = idx

            for ch in reversed(word):

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                if better(idx, node.best_idx):
                    node.best_idx = idx

        # search best matching suffix
        def search(word):

            node = root

            for ch in reversed(word):

                if ch not in node.children:
                    break

                node = node.children[ch]

            return node.best_idx

        # build trie
        for i, word in enumerate(wordsContainer):
            insert(word, i)

        # answer queries
        ans = []

        for word in wordsQuery:
            ans.append(search(word))

        return ans