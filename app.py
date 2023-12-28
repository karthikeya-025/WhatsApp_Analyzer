import streamlit as st 
from src.components.data_ingestion import DataMaker
from src.components.preprocess import Components


df = DataMaker()


uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode(encoding='utf-8')
    data = df.dfMaker(data)
    # print(data[data['message'] == ' ‎image omitted\r'])
    # st.dataframe(data)
    comp = Components(data)
    user_list = comp.get_unique_users()
    user_list.insert(0,'Overall')
    user = st.sidebar.selectbox('Select Users',user_list)
    
    if st.sidebar.button('Show Analysis'):
        st.title('Top Statistics')
        col1,col2,col3 = st.columns(3)
        num_of_messages,num_of_words,num_media = comp.fetch_chat_analysis(user)
        with col1:
            st.header("Total Messages")
            st.title(num_of_messages)
        with col2:
            st.header("Total Words")
            st.title(num_of_words)
        with col3:
            st.header("Total Media")
            st.title(num_media)
        if user == 'Overall':
            st.title("Top Users")
            col4,col5 = st.columns(2)
            fig,ax,x_perc = comp.top_users()
            with col4:
                st.pyplot(fig)
            with col5:
                st.dataframe(x_perc)
        
        fig1,ax1 = comp.wordcloudGen(user)
        st.title("Word Cloud")
        st.pyplot(fig1)
        fig2,ax2 = comp.most_common_words(user)
        st.title("Most Common Words")
        st.pyplot(fig2)
        
        emoji_df = comp.emoji_analysis(user)
        st.title('Most Used Emojis')
        st.table(emoji_df)
        
        fig5,ax5 = comp.time_message_analysis(user)
        st.title("Monthly Analysis")
        st.pyplot(fig5)
        st.title('Activity Map')
        col6,col7 = st.columns(2)
        
        with col6:
            fig6,ax6 = comp.day_name_analysis(user)
            st.title("Busy Day")
            st.pyplot(fig6)
        with col7:
            fig7,ax7 = comp.month_name_analysis(user)
            st.title("Busy Month")
            st.pyplot(fig7)
        