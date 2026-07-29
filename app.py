import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title=" Project Report Generator",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Main Background */
.stApp{
background:linear-gradient(180deg,#020617,#071330,#090b18);
color:white;
overflow-x:hidden;
}

/* Animated Stars */
.stApp::before{
content:"";
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
background-image:
radial-gradient(white 1px, transparent 1px),
radial-gradient(#60a5fa 1px, transparent 1px),
radial-gradient(#a855f7 1px, transparent 1px);
background-size:120px 120px,180px 180px,250px 250px;
animation:starsMove 70s linear infinite;
opacity:.35;
z-index:-1;
}

@keyframes starsMove{
from{transform:translateY(0);}
to{transform:translateY(-300px);}
}

/* Sidebar */
section[data-testid="stSidebar"]{
background:rgba(10,15,35,.85);
backdrop-filter:blur(18px);
border-right:1px solid rgba(168,85,247,.3);
}

/* Header */
.title{
font-size:46px;
font-weight:800;
background:linear-gradient(90deg,#60a5fa,#a855f7,#38bdf8);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{
color:#cbd5e1;
font-size:18px;
}

/* Cards */
.card{
background:rgba(20,25,45,.55);
backdrop-filter:blur(18px);
border:1px solid rgba(168,85,247,.35);
border-radius:22px;
padding:22px;
box-shadow:0 0 25px rgba(99,102,241,.25);
transition:.3s;
}

.card:hover{
transform:translateY(-6px);
box-shadow:0 0 35px rgba(168,85,247,.6);
}

.metric{
font-size:40px;
font-weight:bold;
color:white;
}

.label{
color:#94a3b8;
font-size:14px;
letter-spacing:1px;
}

.badge{
background:#1e293b;
padding:5px 12px;
border-radius:20px;
color:#38bdf8;
font-size:12px;
}

/* Buttons */
.stButton>button{
background:linear-gradient(90deg,#3b82f6,#a855f7);
color:white;
border:none;
border-radius:12px;
padding:10px 24px;
font-weight:bold;
}

.stButton>button:hover{
box-shadow:0 0 20px #a855f7;
}

/* Tables */
[data-testid="stDataFrame"]{
background:rgba(20,25,45,.55);
border-radius:18px;
}

/* Footer */
.footer{
text-align:center;
color:#94a3b8;
padding:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.image("https://img.icons8.com/fluency/96/rocket.png", width=80)

    st.markdown("## 🚀 Navigation")

    st.markdown("---")

    st.button("🏠 Dashboard", use_container_width=True)
    st.button("📄 Generate Report", use_container_width=True)
    st.button("📚 History", use_container_width=True)
    st.button("📊 Analytics", use_container_width=True)
    st.button("⚙ Settings", use_container_width=True)

    st.markdown("---")

    st.success("🟢 AI Online")

    st.info("✨ Gemini Connected")

# ---------------- HEADER ----------------

st.markdown('<div class="title">🌌  Project Report Generator</div>', unsafe_allow_html=True)

st.markdown(
'<div class="subtitle">Create professional AI-powered project reports with futuristic analytics.</div>',
unsafe_allow_html=True)

st.write("")

# ---------------- METRIC CARDS ----------------

c1,c2,c3,c4=st.columns(4)

with c1:
    st.markdown("""
<div class="card">
<div class="label">TOTAL REPORTS</div>
<div class="metric">120</div>
<div class="badge">+15%</div>
</div>
""",unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="card">
<div class="label">ACTIVE USERS</div>
<div class="metric">35</div>
<div class="badge">ONLINE</div>
</div>
""",unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="card">
<div class="label">PROJECTS</div>
<div class="metric">18</div>
<div class="badge">RUNNING</div>
</div>
""",unsafe_allow_html=True)

with c4:
    st.markdown("""
<div class="card">
<div class="label">AI ACCURACY</div>
<div class="metric">98%</div>
<div class="badge">EXCELLENT</div>
</div>
""",unsafe_allow_html=True)

    # =======================
# FUTURISTIC CHARTS
# =======================

st.write("")
st.markdown("## 📊 AI Analytics Dashboard")

left,right=st.columns([2,1])

months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]
reports=[5,8,15,18,20,28,34,40,48,55]

with left:

    fig=px.line(
        x=months,
        y=reports,
        markers=True
    )

    fig.update_traces(
        line_color="#8b5cf6",
        line_width=5,
        marker=dict(
            size=10,
            color="#38bdf8"
        ),
        fill="tozeroy",
        fillcolor="rgba(168,85,247,.15)"
    )

    fig.update_layout(
        title="🚀 Monthly AI Report Generation",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis=dict(gridcolor="#1e293b"),
        yaxis=dict(gridcolor="#1e293b"),
        height=420
    )

    st.plotly_chart(fig,use_container_width=True)

with right:

    pie=go.Figure()

    pie.add_trace(
        go.Pie(
            labels=[
                "Research",
                "Technical",
                "Academic",
                "Final Year"
            ],
            values=[
                35,
                25,
                20,
                20
            ],
            hole=.72,
            marker=dict(
                colors=[
                    "#8b5cf6",
                    "#3b82f6",
                    "#06b6d4",
                    "#ec4899"
                ]
            )
        )
    )

    pie.update_layout(
        title="📄 Reports Category",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        height=420
    )

    st.plotly_chart(pie,use_container_width=True)

# =======================
# AI INSIGHTS
# =======================

st.write("")
st.markdown("## 🤖 AI Insights")

a,b,c=st.columns(3)

with a:
    st.metric(
        "Completion Rate",
        "96%",
        "+4%"
    )
    st.progress(.96)

with b:
    st.metric(
        "Gemini Accuracy",
        "98%",
        "+1%"
    )
    st.progress(.98)

with c:
    st.metric(
        "System Health",
        "100%",
        "Stable"
    )
    st.progress(1.0)

# =======================
# LIVE ACTIVITY
# =======================

st.write("")
st.markdown("## ⭐ Live AI Activity")

activity=pd.DataFrame({

"Time":[
"09:30",
"09:42",
"10:05",
"10:28",
"10:40",
"11:10"
],

"Activity":[
"Generated AI Report",
"PDF Exported",
"Gemini Analysis Completed",
"History Updated",
"Analytics Refreshed",
"Dashboard Synced"
],

"Status":[
"✅",
"✅",
"✅",
"🟢",
"🟣",
"🚀"
]

})

st.dataframe(
activity,
use_container_width=True,
hide_index=True
)

# =======================
# ACTIVITY CONSTELLATION
# =======================

st.write("")
st.markdown("## 🌌 Activity Constellation")

stars=pd.DataFrame({

"x":np.random.randint(1,100,160),
"y":np.random.randint(1,100,160),
"size":np.random.randint(20,220,160)

})

scatter=(
alt.Chart(stars)
.mark_circle(
opacity=.8,
color="#8b5cf6"
)
.encode(
x="x",
y="y",
size="size",
tooltip=["x","y"]
)
.properties(
height=450
)
)

st.altair_chart(
scatter,
use_container_width=True
)

# =====================================================
# REPORT HISTORY
# =====================================================

st.write("")
st.markdown("## 📜 Recent Report History")

history = pd.DataFrame({

"Project":[
"AI Report Generator",
"Hospital Management",
"Attendance System",
"Face Recognition",
"Weather Prediction",
"Chatbot Assistant"
],

"Department":[
"CSE",
"IT",
"CSE",
"ECE",
"AI",
"CSE"
],

"Generated":[
"Today",
"Today",
"Yesterday",
"2 Days Ago",
"4 Days Ago",
"1 Week Ago"
],

"Status":[
"Completed ✅",
"Completed ✅",
"In Review 🟡",
"Completed ✅",
"Completed ✅",
"Archived 📦"
]

})

st.dataframe(
history,
use_container_width=True,
hide_index=True
)

# =====================================================
# AI ASSISTANT
# =====================================================

st.write("")
st.markdown("## 🤖 AI Assistant")

with st.container():

    st.markdown("""

<div class="card">

<h3 style="color:#8b5cf6;">
🧠 Gemini AI Assistant
</h3>

<p style="color:#CBD5E1;">

• AI is connected successfully.<br>

• Ready to generate reports.<br>

• PDF Export Enabled.<br>

• Smart Formatting Enabled.<br>

• Grammar Check Active.<br>

• Citation Generator Active.

</p>

</div>

""",unsafe_allow_html=True)

# =====================================================
# SYSTEM STATUS
# =====================================================

st.write("")
st.markdown("## 🚀 System Status")

col1,col2,col3=st.columns(3)

with col1:
    st.success("🟢 Gemini AI Connected")

with col2:
    st.success("📄 PDF Generator Ready")

with col3:
    st.success("🌐 Streamlit Running")

# =====================================================
# QUICK ACTIONS
# =====================================================

st.write("")
st.markdown("## ⚡ Quick Actions")

a,b,c,d=st.columns(4)

with a:
    st.button("➕ Generate")

with b:
    st.button("📄 Download")

with c:
    st.button("📚 History")

with d:
    st.button("⚙ Settings")

# =====================================================
# NOTIFICATIONS
# =====================================================

st.write("")
st.markdown("## 🔔 Notifications")

notifications=[

"✅ AI generated a report successfully.",

"🚀 Dashboard updated.",

"📄 PDF exported successfully.",

"🌌 Gemini AI responded in 1.2 seconds.",

"⭐ Analytics refreshed."

]

for note in notifications:

    st.info(note)

# =====================================================
# DIGITAL CLOCK
# =====================================================

st.write("")
st.markdown("## 🕒 Current Time")

st.metric(
"System Time",
datetime.now().strftime("%H:%M:%S")
)

# =====================================================
# FOOTER
# =====================================================

st.write("")
st.markdown("---")

st.markdown("""

<div class="footer">

<h3>

🌌  Project Report Generator

</h3>

<p>

Built with ❤️ using

Python • Streamlit • Gemini AI • Plotly

</p>

<p>

© 2024 AI Project Report Generator. All rights reserved.

</p>

</div>

""",unsafe_allow_html=True)