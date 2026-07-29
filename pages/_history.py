import streamlit as st
import pandas as pd

st.set_page_config(page_title="History", page_icon="📚", layout="wide")

st.markdown("""
<style>
.stApp{
    background:linear-gradient(180deg,#030712,#111827,#020617);
    color:white;
}
h1,h2,h3{
    color:#8B5CF6;
}
div[data-testid="stDataFrame"]{
    border-radius:15px;
    overflow:hidden;
}
</style>
""", unsafe_allow_html=True)

st.title("📚 Report History")
st.write("View previously generated reports.")

search = st.text_input("🔍 Search Report")

df = pd.DataFrame({
    "Project Title":[
        "Library Management System",
        "Project Report Generator",
        "Student Attendance System",
        "Hospital Management System"
    ],
    "Department":[
        "Computer Science",
        "Computer Science",
        "Information Technology",
        "Computer Science"
    ],
    "Date":[
        "27-07-2026",
        "26-07-2026",
        "25-07-2026",
        "24-07-2026"
    ],
    "Status":[
        "Completed",
        "Completed",
        "Completed",
        "Completed"
    ]
})

if search:
    df = df[df["Project Title"].str.contains(search, case=False)]

st.dataframe(df, use_container_width=True)

st.download_button(
    "⬇ Export History",
    df.to_csv(index=False),
    file_name="report_history.csv",
    mime="text/csv"
)