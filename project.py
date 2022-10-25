import pandas as pd
import streamlit as st
from pickle import load



Data = load(open('data.sav','rb'))
user_sim_df = load(open('user_sim_df.sav','rb'))
st.title('Book Recommendtion System')

user_id = st.number_input('User_ID')



def recommend_book_to(user_id):
    if user_id in list(user_sim_df):
        sim_user = list(user_sim_df.sort_values([user_id],ascending=False).head(1).index)
        print("Similar User:",sim_user)
        
    else:
        return 'Invalid Entry'
    book = Data[Data['User_Id'] == sim_user[0]]                   
    top = pd.DataFrame(book.sort_values('Book_Rating',ascending=False).head(3),columns=Data.columns,)
    return top[['ISBN','Title']]
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.wallpapersafari.com/17/17/reoxDu.png");
             background-attachment: fixed;
             background-size: 60
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
    
st.button('Enter')
st.write(recommend_book_to(user_id))

