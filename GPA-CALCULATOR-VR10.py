import streamlit as st

# Title
st.title("🎓 GPA Calculator")

# Grade to Point Mapping
grade_to_point = {
    'O': 10,
    'A+': 9,
    'A': 8,
    'B+': 7,
    'B': 6,
    'C': 5,
    'U': 0
}

# Get number of subjects
subject_count = st.number_input("Enter number of subjects", min_value=1, max_value=20, step=1)

# Input fields
subjects = []
st.subheader("Enter Subject Details")

for i in range(subject_count):
    st.markdown(f"**Subject {i+1}**")
    col1, col2, col3 = st.columns(3)
    with col1:
        name = st.text_input(f"Subject Name {i+1}", key=f"name_{i}")
    with col2:
        credit = st.number_input(f"Credit {i+1}", min_value=1, max_value=20, key=f"credit_{i}")
    with col3:
        grade = st.selectbox(f"Grade {i+1}", options=list(grade_to_point.keys()), key=f"grade_{i}")
    
    subjects.append((name, credit, grade))

# GPA Calculation
if st.button("Calculate GPA"):
    total_credits = 0
    total_points = 0

    for name, credit, grade in subjects:
        grade_point = grade_to_point.get(grade, 0)
        total_credits += credit
        total_points += credit * grade_point

    if total_credits == 0:
        st.error("Total credits cannot be zero.")
    else:
        gpa = total_points / total_credits
        st.success(f"✅ GPA: {gpa:.2f}")
