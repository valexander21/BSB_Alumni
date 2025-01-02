import streamlit as st
import pandas as pd
import gspread 
from google.oauth2.service_account import Credentials


###### Design #########
# have blocks to separate each alum info
# button to open addiitonal informaiton
# button to close additional information

###### Upkeep ##########
# ability to pass on and keep updated
# possibly easier through excel file instead of csv
    # maintain excel file and add in rows for subseuqnet alums (will need to fill out form)
    # cleaning_data.py should be able to clean additional data
    # may need to use pip install to help read in xlsx
    # whoever handles this after would just need github? and vscode? to push changes becuase Heroku should update app when github receives changes
        # would need to save changes in xlsx and run command lines in terminal to push changes
        # git add .
        # git commit -m "message"
        # git origin push main 
# reset button being a bitch

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("softball-alumni-a0a84a5b98fc.json", scopes=scope)
client = gspread.authorize(creds)


sheet = client.open("Brown Softball Alumni Portal").sheet1

data = sheet.get_all_records()

raw_df = pd.DataFrame(data)

from cleaning_data import clean_data

df = clean_data(raw_df)
# df = pd.read_pickle("cleaned_data.pkl")

st.title("BSB Alumni <3")


if "search_query" not in st.session_state:
    st.session_state.search_query = ""


def reset_search():
    st.session_state.search_query_reset = True

if "search_query_reset" not in st.session_state:
    st.session_state.search_query_reset = False 

grad_years = list(df['Graduation Year'].unique())
sorted_grad_years = sorted(grad_years, reverse=True)

grad_year_options = ["ALL"] + sorted_grad_years

#search_query = st.text_input("Search for a name:")
#search_query = st.text_input("Search for a name:", value=st.session_state.search_query)

selected_year = st.selectbox(
    'Select Graduation Year', 
    grad_year_options,
)

# if st.session_state.search_query_reset:
#     default_search_query = ""
#     st.session_state.search_query_reset = False  # Reset the flag after handling
#

if selected_year == "ALL":
    filtered_alum = df
else: 
    filtered_alum = df[df["Graduation Year"] == selected_year]



if st.button("Reset Search Query"):
    reset_search()
    if st.session_state.search_query_reset:
        default_search_query = ""
        st.session_state.search_query_reset = False
else:
    default_search_query = st.session_state.search_query
    filtered_alum = filtered_alum[
        filtered_alum['First Name'].str.contains(default_search_query, case=False, na=False) | 
        filtered_alum['Last Name'].str.contains(default_search_query, case=False, na=False)
    ]

search_query = st.text_input("Search for a name:", value=default_search_query, key="search_query")
    



# if st.session_state.search_query:
    

if not filtered_alum.empty:
    for index, alum in filtered_alum.iterrows():
        # alum_name = alum["First Name"] + "'s" + " Current Position: "


        # Render each alumnus's block
        st.markdown(
            f"""
            <div style="
                background-color: #f9f9f9; 
                border: 1px solid #ddd; 
                border-radius: 8px; 
                padding: 16px; 
                margin-bottom: 16px;">
                <h3 style="margin-top: 0;">{alum['Last Name']}, {alum['First Name']} - {alum['Graduation Year']} - {alum['Concentration']}</h3>
                <p><strong>Current Role:</strong> {alum['Current Job Role']} at {alum['Current Work']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Add expander for additional details
        with st.expander("View Details for: " + str(alum['First Name']) + " " + str(alum['Last Name']), expanded=False):
            st.write(f"**Work Email:** {alum['Work Email']}")
            st.write(f"**Personal Email:** {alum['Personal Email']}")
            st.write(f"**LinkedIn:** [Profile]({alum['LinkedIn']})")
            st.write(f"**Other Work or Roles:** {alum['Other Work or Roles']}")
            st.write(f"**Extracurriculars:** {alum['Extracurriculars']}")
        
        # st.subheader(f"{alum['Last Name']}, {alum['First Name']} - {alum['Graduation Year']} - {alum['Concentration']}")
        # st.write(f"{alum['Current Job Role']} - {alum['Current Work']}")
        #     # Show more details on click

        # if st.button(f"View Details for {alum['First Name']} {alum['Last Name']}"):
        #     st.write(f"**Work Email:** {alum['Work Email']}")
        #     st.write(f"**Personal Email:** {alum['Personal Email']}")
        #     st.write(f"**LinkedIn:** [Profile]({alum['LinkedIn']})")
        #     st.write(f"**Other Work or Roles:** {alum['Other Work or Roles']}")
        #     st.write(f"**Extracurriculars:** {alum['Extracurriculars']}")
else: st.write("No results found.")


