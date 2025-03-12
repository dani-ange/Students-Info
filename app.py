import streamlit as st
import pandas as pd
import os

# CSV file path
DATA_FILE = "members.csv"

GROUP_MEMBERS = [
    {"name": "Djofang Nkuingoua Danielle", "specialty": "IABD", "group": "2", "gender": "Female", "group_number": "21"},
    {"name":"Nchourupouo Mohamed", "speciality":"IABD","group":"2","gender":"Male","group_number":"22"},
    {"name": "Ngoue David Roger","speciality": "IABD", "group":"2", "gender":"Malde", "groupe_member":"23"}
]

# Function to save or update members in CSV
def update_csv():
    new_df = pd.DataFrame(GROUP_MEMBERS)

    if os.path.exists(DATA_FILE):
        existing_df = pd.read_csv(DATA_FILE)

        # Merging new members 
        merged_df = pd.concat([existing_df, new_df]).drop_duplicates(subset=["name"], keep="last")
        merged_df.to_csv(DATA_FILE, index=False)
    else:
        new_df.to_csv(DATA_FILE, index=False)

# Update CSV when script runs
update_csv()

# Load members
df = pd.read_csv(DATA_FILE)

st.title("👨‍🎓 Group II Git/GitHub Members")

st.sidebar.title("🔧 Admin Panel")
st.sidebar.write("📌 The list updates automatically when the script runs.")
st.sidebar.write("📝 To add members, **edit the `GROUP_MEMBERS` list in the code** and restart the script.")

# User input for searching
name = st.text_input("Enter your name (or part of it):")

if name:
    filtered_members = df[df["name"].str.contains(name, case=False, na=False)]

    if not filtered_members.empty:
        st.success("✅ Found your details!")
        for _, member in filtered_members.iterrows():
            st.write(f"**👤 Name:** {member['name']}")
            st.write(f"**👤 Gender:** {member['gender']}")
            st.write(f"**📚 Specialty:** {member['specialty']}")
            st.write(f"**📌 Group:** {member['group']}")
            st.write(f"**🔢 Group Number:** {member['group_number']}")
            st.markdown("---")
    else:
        st.error("❌ No match found! add  your name to the members lists in the script.")
