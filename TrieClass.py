class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()


            node = node.children[char]

        node.is_word = True

    def returnPrefixEnd(self, prefix):
        node = self.root

        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return {}

        return node

    def returnMatches(self, prefix, max_matches):
        matches = []

        def recurseMatches(prefixNode, match_word, max_matches):
            if not prefixNode: return
            
            if prefixNode.is_word:
                matches.append(match_word)
                return

            for letter in prefixNode.children:
                if len(matches) < max_matches:
                    recurseMatches(prefixNode.children[letter], match_word + letter, max_matches)
                else:
                    return

            return

        prefixEndNode = self.returnPrefixEnd(prefix)

        if prefixEndNode:
            recurseMatches(prefixEndNode, prefix, max_matches)

        return matches