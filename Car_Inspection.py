import streamlit as st

# Function to generate car inspection report
def generate_report(paint_quality, is_accidental, other_issues):
    report = f"""
    ## Car Inspection Report
    **Paint Quality:** {paint_quality}
    
    **Accidental Status:** {'Yes' if is_accidental else 'No'}
    
    **Additional Issues:**
    {other_issues if other_issues else 'No other issues reported.'}
    """
    return report

# Streamlit App Interface
st.title("Car Inspection Application")
st.header("Check Car Paint Quality and Accidental Status")

# User input for paint quality
paint_quality = st.selectbox(
    "Select the paint quality of the car:",
    ["Excellent", "Good", "Fair", "Poor"]
)

# User input for accidental check
is_accidental = st.radio(
    "Has the car been in an accident?",
    ("Yes", "No")
)

# Additional information input
other_issues = st.text_area(
    "Enter any additional issues (if any):",
    ""
)

# Button to generate report
if st.button("Generate Inspection Report"):
    # Generate the report based on inputs
    report = generate_report(paint_quality, is_accidental == "Yes", other_issues)
    
    # Display the report
    st.markdown(report)
