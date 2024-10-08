import streamlit as st
import pandas as pd

df = pd.read_pickle("cleaned_data.pkl")

st.title("Alumni Softball Players")




grad_years = list(df['Graduation Year'].unique())
sorted_grad_years = sorted(grad_years, reverse=True)

grad_year_options = ["ALL"] + sorted_grad_years

selected_year = st.selectbox('Select Graduation Year',grad_year_options)
# available_for_mentoring = st.checkbox('Mentoring Availability')
# zoom_availability = st.checkbox("Open to Zoom Call")
st.subheader("Alumni List")

if selected_year == "ALL":
    filtered_alum = df
else: 
    filtered_alum = df[df["Graduation Year"] == selected_year]

for index, alum in filtered_alum.iterrows():
    
    st.write(f"{alum['Last Name']}, {alum['First Name']} - {alum['Graduation Year']} - {alum['Concentration']} - {alum['Current Job Role']}")
        
        # Show more details on click

    if st.button(f"View Details for {alum['First Name']} {alum['Last Name']}"):
        st.write(f"**Work Email:** {alum['Work Email']}")
        st.write(f"**Personal Email:** {alum['Personal Email']}")
        st.write(f"**LinkedIn:** [Link]({alum['LinkedIn']})")
        st.write(f"**Other Work or Roles:** {alum['Other Work or Roles']}")
        st.write(f"**Extracurriculars:** {alum['Extracurriculars']}")



# Filter the DataFrame


# if graduation_year != "ALL":
#     fifltered_data = filtered_data[filtered_data['Graduation Year'] == graduation_year]
    
# if available_for_mentoring:
#     filtered_data = filtered_data[filtered_data['Mentoring Available'] == 'Yes']

# Display the filtered data

