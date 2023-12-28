from src.exception import CustomException
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud
from collections import Counter
import emoji
from warnings import filterwarnings

filterwarnings('ignore')



class Components:
    def __init__(self,df):
        self.df = df
    
    def get_unique_users(self):
        users = self.df['user'].unique().tolist()
        return users
    def fetch_chat_analysis(self,selected_user):
        try:
            words = []
            if selected_user != 'Overall':
                
                messages = self.df[self.df['user'] == selected_user]
                num_messages = messages['message'].shape[0]
            else:
                messages = self.df
                num_messages = messages['message'].shape[0]
                
            
            for m in messages['message'].tolist():
                word = m.split()
                words.extend(word)
            num_media = messages[(messages['message'] == ' ‎image omitted\r')|(messages['message'] == ' ‎video omitted\r')|(messages['message'] == ' ‎GIF omitted\r')|(messages['message'] == ' ‎audio omitted\r')].shape[0]
            return num_messages,len(words),num_media
        except Exception as e:
            raise(e)
    def top_users(self):
        try:
            x = self.df['user'].value_counts().head()
            x_perc = round((self.df['user'].value_counts()/self.df.shape[0])*100,2).reset_index()
            x_perc.rename(columns = {'user':'Users','count':'Total Messages (in perc%)'},inplace=True)
            fig,ax = plt.subplots()
            plt.title('Top 5 Users')
            ax = sns.barplot(x=x.index,y=x.values,color='black')
            plt.xticks(rotation='vertical')
            plt.xlabel('users')
            plt.ylabel('No. of messages')
            return fig,ax,x_perc
        except Exception as e:
            raise CustomException(e)
    def wordcloudGen(self,selected_user):
        try:
            
            if selected_user != 'Overall':
                messages = self.df[self.df['user'] == selected_user]
            else:
                messages = self.df
            rows_to_drop = messages[(messages['message'] == ' ‎image omitted\r')|(messages['message'] == ' ‎video omitted\r')|(messages['message'] == ' ‎GIF omitted\r')|(messages['message'] == ' ‎audio omitted\r')]
            messages= messages.drop(rows_to_drop.index)
            wc = WordCloud(height=500,width=500,background_color='white',min_font_size=10)
            df_wc = wc.generate(messages['message'].str.cat(sep = ' '))
            fig,ax= plt.subplots()
            ax.imshow(df_wc) 
                 
            return fig,ax
        except Exception as e:
            raise CustomException(e)
    def most_common_words(self,selected_user):
        try:
            if selected_user != 'Overall':
                messages = self.df[self.df['user'] == selected_user]
            else:
                messages = self.df
            words = []
            for i in messages['message']: 
                words.extend(i.split())
            
            common_words = Counter(words).most_common()
            # print(common_words)
            most_common = []
            for i in common_words:

                if 'omitted' in i or '\u200e' in i or '\u200eimage' in i or '\u200eaudio' in i or '\u200esticker' in i:
                    continue
                most_common.append(i)
            most_common = most_common[0:21]
            cdf = pd.DataFrame(most_common).rename(columns={0:'Words',1:'Frequency'})
            fig,ax = plt.subplots()
            
            ax = plt.barh(cdf['Words'],cdf['Frequency'])
            plt.xticks(rotation='vertical')
            return fig,ax
        except Exception as e:
            raise CustomException(e)
            
            
    def emoji_analysis(self,selected_user):
        try:
            if selected_user != 'Overall':
                messages = self.df[self.df['user'] == selected_user]
            else:
                messages = self.df
            emojis = []
            for i in messages['message']:
                emojis.extend(emoji.distinct_emoji_list(i))
            emoji_df = pd.DataFrame(Counter(emojis).most_common(20)).rename(columns={0:'Emojis',1:'Frequency'})
            return emoji_df
        except Exception as e:
            raise CustomException(e)
    def time_message_analysis(self,selected_user):
        try:
            if selected_user != 'Overall':
                messages = self.df[self.df['user'] == selected_user]
            else:
                messages = self.df
                
            messages['month_num'] = messages['dates'].dt.month
            timeline = messages.groupby(['year','month_num','month']).count()['message'].reset_index()
            time = []
            for i in range(timeline.shape[0]):
                time.append(str(timeline['month'][i]) + '-' + str(timeline['year'][i]))
            timeline['time'] = time
            fig,ax = plt.subplots()
            ax = plt.plot(timeline['time'],timeline['message'])
            plt.xticks(rotation='vertical');
            
            return fig,ax
        except Exception as e:
            raise CustomException(e)
        
        
    def day_name_analysis(self,selected_user):
        try:
            if selected_user != 'Overall':
                messages = self.df[self.df['user'] == selected_user]
            else:
                messages = self.df
            messages['day_name'] = messages['dates'].dt.day_name()
            day_name_df = messages.groupby(['day_name']).count()['message'].reset_index()
            fig,ax = plt.subplots()
            ax = plt.barh(day_name_df['day_name'],day_name_df['message'],color='purple');
            return fig,ax
        except Exception as e:
            raise CustomException(e)
    def month_name_analysis(self,selected_user):
        try:
            if selected_user != 'Overall':
                messages = self.df[self.df['user'] == selected_user]
            else:
                messages = self.df
            month_name_df = messages.groupby(['month']).count()['message'].reset_index()
            fig,ax = plt.subplots()
            ax = plt.barh(month_name_df['month'],month_name_df['message'],color='green');
            return fig,ax
        except Exception as e:
            raise CustomException(e)