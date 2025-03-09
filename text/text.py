import streamlit as st

#streamlit App Title
st.title("Text Analyser App")

#User Input:paragraph input
text=st.text_area("Enter a paragraph:","")

#word count
words=text.split()
word_count=len(words)

#character count
char_count=len(text)

#vowel
vowels="aeiou"
vowel_count =sum(1 for char in text if char in vowels)

#search and replace
search_word = st.text_input("Enter a word to search for:")
replace_word = st.text_input("Enter a word to replace it with:")

if search_word and replace_word:
    modified_text = text.replace(search_word,replace_word)
    st.write("Modified Paragraph:",modified_text)

    #upper case
    st.write("Uppercase:",text.upper())
    st.write("Lowercase:",text.lower)

    #Type casting
    st.write(f"Word Count: {str(word_count)}")
    st.write(f"Vowel Count: {str(vowel_count)}")

    #operators
    contains_python = "Python" in text
    st.write(f"Does the paragraph contain 'python'?{contains_python}")

    #Average word length
    avg_word_length = char_count / word_count if word_count else 0
    st.write(f"Average Word Length:{avg_word_length:.2f}")

else:
    st.warning("please enter some text to analyze")
    