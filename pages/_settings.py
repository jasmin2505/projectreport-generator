import streamlit as st

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

st.markdown("""
<style>
.stApp{
    background:linear-gradient(180deg,#030712,#111827,#020617);
    color:white;
}

.main-title{
    font-size:40px;
    font-weight:bold;
    color:#8B5CF6;
}

.setting-box{
    background:rgba(30,41,59,0.6);
    padding:20px;
    border-radius:15px;
    border:1px solid #3B82F6;
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>⚙️ Settings</div>", unsafe_allow_html=True)

st.write("Customize your Project Report Generator.")

st.markdown("---")

with st.container():
    st.markdown("<div class='setting-box'>", unsafe_allow_html=True)

    theme = st.selectbox(
        "🎨 Theme",
        ["Purple Galaxy", "Dark Blue"]
    )

    font = st.selectbox(
        "🔤 Font Size",
        ["Small", "Medium", "Large"]
    )

    autosave = st.toggle("💾 Auto Save", value=True)

    notifications = st.toggle("🔔 Notifications", value=True)

    if st.button("✅ Save Settings", use_container_width=True):
        st.success("Settings saved successfully!")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

st.info("Version 1.0 | Project Report Generator")