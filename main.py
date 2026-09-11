# absolute imports
from build_trie import trie
import streamlit as st
import st_keyup as st_keyup

st.title("Autocomplete word search")

user_input = st_keyup.st_keyup("Search a word...")

if user_input:
    matches = trie.returnMatches(user_input, 5)

    for match in matches:
        st.write(f":star: {match}")

