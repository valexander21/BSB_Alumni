import pandas as pd

df = pd.read_csv("bsb_alum_data.csv")

def drop_columns(df: pd.DataFrame ,column_name : str):
    df = df.drop([column_name], axis=1)
    return df

def column_lower(df: pd.DataFrame, column_name : str):
    df[column_name] = df[column_name].str.lower()

    return df

def rename_columns(df, current_name, desired_name):
    df = df.rename(columns={current_name:desired_name})

    return df


def clean_data(file_path):
    # Read the data
    df = pd.read_csv(file_path)
    
    df.columns = df.columns.str.strip()
    df = df.fillna("")


    df[["First Name", "Last Name"]] = df["Name"].str.split(' ', n=1,expand=True)

    df = drop_columns(drop_columns(df, "Timestamp"), "Name")
    df = column_lower(column_lower(df, "Mentoring Availability"), "Open to Zoom call")
    df = rename_columns(df, "LinkedIn profile link", "LinkedIn")
    df = rename_columns(df, "Role at Current Job", "Current Job Role")
    df = rename_columns(df, "Other work or roles", "Other Work or Roles")
    df = rename_columns(df, "Open to Zoom call", "Zoom Call Availability")


   
    new_columns = ["Last Name", "First Name", "Graduation Year", "Concentration", "Work Email", "Personal Email", "LinkedIn", "Current Work", "Current Job Role", "Other Work or Roles", "Mentoring Availability", "Zoom Call Availability", "Extracurriculars"]
    df = df[new_columns]
    df = df.sort_values("Last Name")
    

    
    return df


#print(df.sort_values("Last Name"))
#print(clean_data("bsb_alum.csv").sort_values("Last Name"))

# concentration column: casing issues, multiple concentrations, abbreviations, inclusion of BA vs SCB
# GOOD Work Email: nan values
# GOOD Personal Emai: seems good
#LinkedIn: Nan values and one string, username not link (could find link and insert)
# Current work: not consistent, strings lots of freedom
# GOOD Role at Current Job: NaN values
# GOOD other work or roles: Nan values
# mentoring availability: yes,no, maybe values, and one long response
# open to zoom call: yes, no, maybe
# 
#  
#print(clean_data("bsb_alum.csv").columns[6])
#print(clean_data("bsb_alum.csv"))



if __name__ == "__main__":
    cleaned_df = clean_data('bsb_alum.csv')
    cleaned_df.to_pickle('cleaned_data.pkl') 