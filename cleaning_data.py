import pandas as pd
import re

#df = pd.read_csv("Brown Softball Alumni.xlsx")

def drop_columns(df: pd.DataFrame ,column_name : str):
    df = df.drop([column_name], axis=1)
    return df

def column_lower(df: pd.DataFrame, column_name : str):
    df[column_name] = df[column_name].str.lower()

    return df

def rename_columns(df, current_name, desired_name):
    df = df.rename(columns={current_name:desired_name})

    return df

def extract_year(year_str):
    # Extract everything before the first space
    match = re.match(r'(\d{4})', str(year_str))
    if match:
        return int(match.group(1))
    else:
        return None

# Apply the extraction function to the 'Graduation Year' column



def clean_data(df):
    # Read the data
    # df = pd.read_csv(file_path)
    
    df.columns = df.columns.str.strip()
    df = df.fillna("")


    df[["First Name", "Last Name"]] = df["Name"].str.split(' ', n=1,expand=True)

    

    rename_map = {
        "LinkedIn profile link": "LinkedIn",
        "Role at Current Job": "Current Job Role",
        "Other work or roles": "Other Work or Roles",
        "Open to Zoom call": "Zoom Call Availability",
        "What was your concentration?": "Concentration", 
        "Where do you currently work?": "Current Work", 
        "What is your role?": "Current Job Role", 
        "Have you worked anywhere else or in other roles within your current firm?": "Other Work or Roles", 
        "What other extracurriculars did you participate in while at Brown?": "Extracurriculars"
    }
    for current_name, desired_name in rename_map.items():
        if current_name in df.columns:
            df = rename_columns(df, current_name, desired_name)

    # df = drop_columns(drop_columns(df, "Timestamp"), "Name")
    # df = column_lower(column_lower(df, "Mentoring Availability"), "Open to Zoom call")

    # df = rename_columns(df, "LinkedIn profile link", "LinkedIn")
    # df = rename_columns(df, "Role at Current Job", "Current Job Role")
    # df = rename_columns(df, "Other work or roles", "Other Work or Roles")
    # df = rename_columns(df, "Open to Zoom call", "Zoom Call Availability")


   
    new_columns = ["Last Name", "First Name", "Graduation Year", "Concentration", "Work Email", 
                   "Personal Email", "LinkedIn", "Current Work", "Current Job Role", "Other Work or Roles", 
                   "Mentoring Availability", "Zoom Call Availability", "Extracurriculars"]
    
    df['Graduation Year'] = df['Graduation Year'].apply(extract_year)
    
    df = df[[col for col in new_columns if col in df.columns]]  # Keep only columns that exist
    df = df.sort_values("Last Name")
    # df = df[new_columns]
    # df = df.sort_values("Last Name")
    

    
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



# if __name__ == "__main__":
#     # xlsx_data = pd.read_excel('Brown Softball Alumni.xlsx')
#     # xlsx_data.to_csv('bsb_alum_data2.csv', header=True)

#     # cleaned_df = clean_data('bsb_alum_data2.csv')
#     cleaned_df = clean_data('bsb_alum_data.csv')
#     cleaned_df.to_pickle('cleaned_data.pkl') 