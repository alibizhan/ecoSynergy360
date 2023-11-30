import streamlit as st

# Define custom CSS for styling the buttons
button_style = """
    background-color: #f63366;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    border: none;
    margin-right: 10px;
    cursor: pointer;
"""

# Title and introductory text for the first page
st.title('WELCOME TO THE ECOSYNERGY360 PLATFORM ON SUSTAINABILITY ASSESSMENT')
st.markdown(
    """
    The EPSA is developed by Ecosynergy360 team...
    """
)

st.write("---")

st.title("Select a Section")

# Create buttons for different sections in the main page
if st.button("Sustainability", help="Explore Sustainability", key="sustainability_button", style=button_style):
    st.title("Sustainability Context")
    st.markdown(
        """
        Welcome to Ecosynergy360, where sustainability is not just a concept but a commitment to securing the needs of the present generation without compromising the essential requirements of the generations to come.
        ...
        """
    )
    # Add more content for Sustainability section...

if st.button("Life Cycle Assessment", help="Explore Life Cycle Assessment", key="lca_button", style=button_style):
    st.title("Life Cycle Assessment")
    st.markdown(
        """
        Welcome to Ecosynergy360, where sustainability isn't just a goal but a journey guided by Life Cycle Assessment (LCA), a powerful tool in understanding the holistic impact of projects on our environment.
        ...
        """
    )
    # Add more content for LCA section...

if st.button("Carbon Footprint", help="Explore Carbon Footprint", key="carbon_footprint_button", style=button_style):
    st.title("Carbon Footprint")
    st.markdown(
        """
        In the realm of sustainable practices, the concept of a "carbon footprint" has emerged as a crucial metric in assessing the environmental impact of human activities.
        ...
        """
    )
    # Add more content for Carbon Footprint section...

if st.button("Calculator", help="Explore Calculator", key="calculator_button", style=button_style):
    st.title("Calculator")
    phase = st.radio("Choose the phase of your project", ("Production phase", "Construction Phase"))
    # Add functionality for the Calculator section...


##else:  # Calculator section
    ##st.title("Calculator")
    ##phase = st.radio("Choose the phase of your project", ("Production phase", "Construction Phase"))

    if phase == "Production phase":
        asphalt_type = st.radio("Choose the type of your asphalt", ("Standard Hot Mix Asphalt", "HMA with RAP"))
        # Add more selection choices for asphalt type and temperature...
        if asphalt_type == "Standard Hot Mix Asphalt":
            pass
            # Display result for Standard HMA based on selected temperature
            # Show the calculated CO2 emissions and details
            # Example: st.write(f"The total amount of CO2 for this asphalt with identifying 180 Celsius temperature in aggregate heating is...")
        else:
            pass# HMA with RAP
            # Display result for HMA with RAP similar to Standard HMA
            # Show the calculated CO2 emissions and details
    else:  # Construction Phase
        # Add functionality for the Construction Phase calculations
        pass