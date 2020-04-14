import sys
import pandas as pd
from pandas import datetime
def parser(x):
    return datetime.strptime(x,'%d-%m-%Y')

args=sys.argv
if not (len(args)==4):
    print("No input provided..specify file_name, start date and end date separated by spaces")
    sys.exit()

print(args)

file=args[1]
start_date=args[2]
end_date=args[3]
df=pd.read_csv(file,index_col=0,date_parser=parser,parse_dates=[0])
df.index=pd.DatetimeIndex(df.index)
idx=pd.date_range(start_date,end_date,name="Date")
df=df.reindex(idx,fill_value=0)
name="DATES_FILLED_"+file
df.to_csv(name)
print("File generated : ",name)
