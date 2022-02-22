#functions 

import os
import pickle

def return_value(item, row):
    for key, value in row.items():
        if key.lower() == item:
            return value
    return None



def extract_items(df):
    df = df.reset_index() 
    user_item_list = []
    for index, row in df.iterrows():
        if row['Items'] != 'Key Not Found':
            for item in row['Items']:
                for key,value in item.items():
                    if key.lower() == 'menuitem':
                        user_item_list.append((row['OrderId'],row['UserId'],value,row['RestaurantId'],row['Date'],row['Rating'],row['Comments'],row['Address']))

    return user_item_list    


def save_file(data, fname, dname):
    """Save a datafile (data) to a specific location (dname) and filename (fname)
    
    Currently valid formats are limited to CSV or PKL."""
    
    if not os.path.exists(dname):
        os.mkdir(dname)
        print(f'Directory {dname} was created.')
        
    fpath = os.path.join(dname, fname)
     
    if os.path.exists(fpath):
        print("A file already exists with this name.\n")

    else:  # path does not exist, ok to save the file
        print(f'Writing file.  "{fpath}"')
        _save_file(data, fpath)
        
        
        
        
        
        
def _save_file(data, fpath):
    valid_ftypes = ['.csv', '.pkl']
    
    assert (fpath[-4:] in valid_ftypes), "Invalid file type.  Use '.csv' or '.pkl'"

    # Figure out what kind of file we're dealing with by name
    if fpath[-3:] == 'csv':
        data.to_csv(fpath, index=False)
    elif fpath[-3:] == 'pkl':
        with open(fpath, 'wb') as f:
            pickle.dump(data, f)
