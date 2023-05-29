import glob
import os
import datetime

def main()->None:
    #日付取得
    datefrom_str:str=input("From:更新日を入力してください。例.2023-5-1 :")
    dateto_str:str=input("To:更新日を入力してください。例.2023-5-31 :")
    #調査対象パス
    path: str=input("調査対象パス :")
    checK_path: str=path+"/**"
    for file_path in glob.glob(checK_path, recursive=True):
        if os.path.isfile(file_path):
            file_stamp=os.path.getmtime(file_path)
            # datetimeに変換
            file_datetime: datetime = datetime.datetime.fromtimestamp(file_stamp)
            from_list: list=datefrom_str.split('-')
            from_date:datetime=datetime.datetime(int(from_list[0]),int(from_list[1]),int(from_list[2]))
            to_list: list=dateto_str.split('-')
            to_date:datetime=datetime.datetime(int(to_list[0]),int(to_list[1]),int(to_list[2]))
            #日時が範囲内のものを出力
            if from_date<=file_datetime and file_datetime<=to_date:
                print(file_path)

    


if __name__=="__main__":
    main()