import streamlit as st

st.caption("This is a string that explains something above.")
st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")



# st.text

import streamlit as st

st.text("This is text\n[and more text](that's not a Markdown link).")

# st.latex
 
import streamlit as st

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# st.code

import streamlit as st

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")