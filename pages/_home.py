import streamlit as st

st.set_page_config(
    page_title="Project Report Generator",
    page_icon="📄",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background:linear-gradient(180deg,#030712,#111827,#020617);
color:white;
}

.title{
font-size:48px;
font-weight:800;
text-align:center;
background:linear-gradient(90deg,#8B5CF6,#3B82F6);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{
text-align:center;
color:#CBD5E1;
font-size:18px;
}

.card{
background:rgba(20,25,45,.75);
padding:25px;
border-radius:20px;
border:1px solid rgba(139,92,246,.35);
margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>📄 Project Report Generator</div>", unsafe_allow_html=True)

st.markdown(
"<div class='subtitle'>Generate professional project reports quickly and export them as PDF.</div>",
unsafe_allow_html=True
)

st.write("")

st.button("🚀 Generate Report", use_container_width=True)

st.write("")

c1, c2, c3 = st.columns(3)

c1.metric("📄 Reports Generated", "25")
c2.metric("📥 PDFs Downloaded", "25")
c3.metric("🟢 Status", "Ready")

st.write("")

st.markdown("## 📖 How It Works")

st.success("1️⃣ Enter project details")

st.success("2️⃣ Preview the report")

st.success("3️⃣ Generate PDF")

st.success("4️⃣ Download your report")

st.write("")

st.markdown("## ⭐ Quick Actions")

a, b, c = st.columns(3)

with a:
    st.button("📄 Generate")

with b:
    st.button("📚 History")

with c:
    st.button("⚙️ Settings")