import streamlit as st
import pandas as pd
import os

# CSV file path
DATA_FILE = "members.csv"

#Group members list 
GROUP_MEMBERS = [
    {"name": "Djofang Nkuingoua Danielle", "specialty": "IABD", "group": "2","gender":"Female", "group_number": "21"},
   
]

def save_members_to_csv():
    df = pd.DataFrame(GROUP_MEMBERS)
    df.to_csv(DATA_FILE, index=False)

if not os.path.exists(DATA_FILE):
    save_members_to_csv()

df = pd.read_csv(DATA_FILE)

st.title("👨‍🎓 Group II Git/GitHub Members")

st.sidebar.title("🔧 Admin Panel")
st.sidebar.write("📌 This list is stored in `members.csv`.")
st.sidebar.write("📝 To add members, **edit the `GROUP_MEMBERS` list in the code** and restart the script.")

# User input for searching
name = st.text_input("Enter your name (or part of it):")

if name:
    filtered_members = df[df["name"].str.contains(name, case=False, na=False)]

    if not filtered_members.empty:
        st.success("✅ Found your details!")
        for _, member in filtered_members.iterrows():
            st.write(f"**👤 Name:** {member['name']}")
            st.write(f"**🚻 Gender:** {member['gender']}")
            st.write(f"**📚 Specialty:** {member['specialty']}")
            st.write(f"**📌 Group:** {member['group']}")
            st.write(f"**🔢 Group Number:** {member['group_number']}")
            st.markdown("---")  
    else:
        st.error("❌ No match found! Contact the admin to add your name.")
