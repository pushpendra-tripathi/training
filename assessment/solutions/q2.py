'''
    module to return top n rows

'''

import pandas as pd

def top_n_sorted(n:int,field:str,path:str):
    '''
        function to get top n rows in descending order sorted by field 
    '''
    try:
        df = pd.read_csv(path)
    except KeyError:
        print('invalid field name')
        return
    except TypeError:
        print('invalid type for arguments') 
    else:
        result = df.sort_values(ascending=False,by=field)
        return result.head(n)

if __name__ == '__main__':
    print(top_n_sorted(5,'price','./hourly_prices.csv'))



