
import streamlit as st

st.set_page_config(page_title="Student Marks Predictor", page_icon="📚")

st.markdown("""
<style>
.stApp {background-color: #edf2f7;}
.title {text-align:center; color:#24568f; font-size:34px; font-weight:bold;}
.result {background:#e5f5e9; padding:20px; border-radius:12px; text-align:center;}
.info {background:#e5efff; padding:15px; border-radius:10px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">Student Marks Predictor</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>Using Linear Regression</p>", unsafe_allow_html=True)

hours = [1,2,3,4,5,6,7,8]
marks = [35,40,50,55,65,70,80,90]

x = sum(hours)/len(hours)
y = sum(marks)/len(marks)

m = sum((a-x)*(b-y) for a,b in zip(hours,marks)) / sum((a-x)**2 for a in hours)
c = y - m*x

st.subheader("Enter Your Study Details")
h = st.number_input("Enter Study Hours:", 0.0, 10.0, 5.0, 0.5)

if st.button("Predict Marks", use_container_width=True):
    result = round(m*h+c, 2)
    st.markdown(f"""
    <div class="result">
    <h3 style="color:#237a3b">Your Predicted Marks</h3>
    <h1 style="color:#176b32">{result} / 100</h1>
    <p>Study Hours: {h}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="info">
<h4>About This Project</h4>
<p>This project uses Linear Regression to predict student marks based on study hours.</p>
<p>The prediction is calculated using sample student data.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("Sample Student Data")
st.table({"Study Hours": hours, "Student Marks": marks})

st.subheader("Mathematical Formula")
st.latex("y = mx + c")
st.write("Here, x represents study hours and y represents predicted marks.")
