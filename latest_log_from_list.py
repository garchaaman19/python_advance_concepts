# From the given files_list,fetch the latest file present based on the timestamp attached
files_list=['logs_21122021.logs','logs_29122021.logs',0,'logs_231220s21.logs']

from datetime import datetime
def fetch_latest_timestamp(files_list):
        max_date=None
        date_index=0
        for index,log in enumerate(files_list,0):
            if type(log)==str:
                try:
                    date=datetime(year=int(log[9:13]),month=int(log[7:9]),day=int(log[5:7]))
                    if index==0:
                        max_date=date
                    if date> max_date:
                        max_date=date
                        date_index=index
                except ValueError as e:
                    print(f"Incorrect format - {log} , format needs to be in logs_ddmmyyyy.logs ")                
        return files_list[date_index]
    

            

print(fetch_latest_timestamp(files_list))
