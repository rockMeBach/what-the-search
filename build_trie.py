from pathlib import Path
from TrieClass import Trie

wordspath = Path(__file__).parent / "data" / "words.txt"

with open(wordspath, "r") as f:
    words = [line.strip() for line in f]

trie = Trie()

for word in words:
    trie.insert(word)