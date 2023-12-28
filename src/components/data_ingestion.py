import pandas as pd
import re
from warnings import filterwarnings
from src.exception import CustomException

filterwarnings('ignore')

# fp = r'C:\Users\Lenovo\Desktop\webapps\whatsappAnalyzer\data\_chat.txt'

    

class DataMaker:
    def __init__(self) -> None:
        pass
    
    def dfMaker(self,chats):
        try:
            # with open(file_path,'r',encoding='utf-8') as file_obj:
            #     chats = file_obj.read()
        
            pattern = "^U[+]200E|\[\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{1,2}:\d{1,2}\s[A-Z]{1,2}\]\s"

            messages = re.split(pattern,chats)[1:]

            pattern2 = "\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{1,2}:\d{1,2}\s[A-Z]{1,2}"

            dates = re.findall(pattern2,chats)

            df = pd.DataFrame({'dates':dates,'messages':messages})

            df['dates'] = df['dates'].str.replace(',','')

            df['dates'] = pd.to_datetime(df['dates'],format='%d/%m/%y %I:%M:%S %p')

            df['year'] = df['dates'].dt.year
            df['month'] = df['dates'].dt.month_name()
            df['day'] = df['dates'].dt.day

            df['messages'] = df['messages'].str.replace('\n','')
            df['user'] = df['messages'].str.split(':').str[0]
            df['message'] = df['messages'].str.split(':').str[1]
            df.drop('messages',axis=1,inplace=True)
            
            return df
        except Exception as e:
            raise CustomException(e)
