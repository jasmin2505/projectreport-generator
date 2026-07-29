import streamlit as st
from utils.pdf_generator import generate_pdf
import json

st.set_page_config(
    page_title="Generate Report",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Project Report Generator")
st.caption("Create professional project reports easily.")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    project_title = st.text_input("Project Title")
    student_name = st.text_input("Student Name")
    roll_number = st.text_input("Roll Number")
    department = st.text_input("Department")

with col2:
    guide_name = st.text_input("Guide Name")
    college_name = st.text_input("College Name")
    project_type = st.selectbox(
        "Project Type",
        [
            "Mini Project",
            "Major Project",
            "Research Project",
            "Seminar"
        ]
    )

st.markdown("---")

abstract = st.text_area(
    "Abstract",
    height=150
)

objectives = st.text_area(
    "Objectives",
    height=120
)

methodology = st.text_area(
    "Methodology",
    height=150
)

conclusion = st.text_area(
    "Conclusion",
    height=150
)
# ==========================================
# REPORT PREVIEW
# ==========================================

st.markdown("---")
st.subheader("📋 Report Preview")

report = {
    "Project Title": project_title,
    "Student Name": student_name,
    "Roll Number": roll_number,
    "Department": department,
    "Guide Name": guide_name,
    "College Name": college_name,
    "Project Type": project_type,
    "Abstract": abstract,
    "Objectives": objectives,
    "Methodology": methodology,
    "Conclusion": conclusion
}

filled_fields = sum([
    bool(project_title),
    bool(student_name),
    bool(roll_number),
    bool(department),
    bool(guide_name),
    bool(college_name),
    bool(abstract),
    bool(objectives),
    bool(methodology),
    bool(conclusion)
])

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Fields Filled", f"{filled_fields}/10")

with c2:
    st.metric("Characters", len(abstract + objectives + methodology + conclusion))

with c3:
    if filled_fields == 10:
        st.success("Ready ✅")
    else:
        st.warning("Incomplete")

st.code(
    json.dumps(
        report,
        indent=4
    ),
    language="json"
)

st.markdown("---")

# ==========================================
# GENERATE REPORT
# ==========================================

st.subheader("🚀 Generate Report")

if st.button("📄 Generate Project Report", use_container_width=True):

    if filled_fields != 10:
        st.error("Please complete all fields before generating the report.")

    else:

        try:

            pdf_file = generate_pdf(report)

            st.success("✅ Report generated successfully!")

            with open(pdf_file, "rb") as file:

                st.download_button(
                    label="⬇ Download Project Report",
                    data=file,
                    file_name="Project_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

        except Exception as e:

            st.error(f"Error while generating report:\n{e}")

st.markdown("---")

# ==========================================
# REPORT INFORMATION
# ==========================================

st.subheader("📑 Report Information")

info1, info2 = st.columns(2)

with info1:
    st.info("✔ PDF format")
    st.info("✔ Professional layout")
    st.info("✔ Ready for submission")

with info2:
    st.info("✔ Includes all project details")
    st.info("✔ Easy to download")
    st.info("✔ Printable")
    # ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown(
    """
    <style>
    .footer{
        text-align:center;
        padding:20px;
        color:#94A3B8;
        font-size:15px;
    }

    .footer h3{
        color:#A855F7;
        margin-bottom:8px;
    }
    </style>

    <div class="footer">
        <h3>🌌 Project Report Generator</h3>
        <p>Create professional project reports in just a few clicks.</p>
        <p>Version 1.0</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# RESET FORM
# ==========================================

if st.button("🗑 Clear Preview"):
    st.rerun()

# ==========================================
# END OF FILE
# ==========================================