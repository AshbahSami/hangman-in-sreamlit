import random
import streamlit as st

# List of fruits
fruits = ['banana', 'apple', 'orange', 'pineapple', 'guava']

# Streamlit app
st.title("🍌🍎🍍 Hangman Game - Guess the Fruit! 🍊🍏")

# Session state to remember the word, guesses, and chances
if 'word' not in st.session_state:
    st.session_state.word = random.choice(fruits).lower()
    st.session_state.chance = 6
    st.session_state.correct = set()
    st.session_state.used_letters = set()

word = st.session_state.word
chance = st.session_state.chance
correct = st.session_state.correct
used_letters = st.session_state.used_letters

# Display current word progress
display = ''
for char in word:
    if char in correct:
        display += char + ' '
    else:
        display += '_ '
st.subheader("Word to Guess:")
st.write(display)

# Show chances left and used letters
st.write(f"Chances left: {chance}")
st.write(f"Used Letters: {' '.join(sorted(used_letters))}")

# Input guess
guess = st.text_input("Enter a letter:", max_chars=1).lower()

if st.button('Submit Guess'):
    if not guess.isalpha():
        st.warning("⚠️ Please enter a valid letter.")
    elif guess in used_letters:
        st.warning("⚠️ You already guessed that letter.")
    else:
        used_letters.add(guess)
        if guess in word:
            correct.add(guess)
            st.success("✅ Good guess!")
        else:
            st.session_state.chance -= 1
            st.error(f"❌ Wrong guess! {st.session_state.chance} chances left.")

    # Check for win
    if set(word) <= correct:
        st.balloons()
        st.success(f"🎉 Congratulations! You guessed the word '{word.upper()}'!")
        if st.button("Play Again"):
            for key in st.session_state.keys():
                del st.session_state[key]
    elif st.session_state.chance == 0:
        st.error(f"💀 Game Over! The word was '{word.upper()}'.")
        if st.button("Try Again"):
            for key in st.session_state.keys():
                del st.session_state[key]
