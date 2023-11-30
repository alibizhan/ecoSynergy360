
import streamlit as st
st.set_page_config(
    page_title="ecoSynergy360",
    page_icon="icons8-arrows-around-circle-64.png",
    layout="wide",
)

# # Title and introductory text for the first page
# st.title('WELCOME TO THE ECOSYNERGY360 PLATFORM ON SUSTAINABILITY ASSESSMENT')
# st.markdown(
#     """
#     The EPSA is developed by Ecosynergy360 team...
#     """
# )

# st.write("---")

# st.title("Select a Section")

# # Define custom CSS for styling the buttons
# button_style = """
#     <style>
#     .button-style {
#         background-color: #f63366;
#         color: white;
#         padding: 10px 20px;
#         border-radius: 5px;
#         border: none;
#         margin-right: 10px;
#         cursor: pointer;
#     }
#     </style>
# """

# # Display the custom CSS style
# st.markdown(button_style, unsafe_allow_html=True)

# # Create buttons for different sections in the main page using HTML
# if "<button class='button-style' onclick='Sustainability()'>Sustainability</button>":
#     st.title("Sustainability Context")
#     st.markdown(
#         """
#         Welcome to Ecosynergy360, where sustainability is not just a concept but a commitment to securing the needs of the present generation without compromising the essential requirements of the generations to come.
#         ...
#         """
#     )
#     # Add more content for Sustainability section...

# if "<button class='button-style' onclick='LifeCycleAssessment()'>Life Cycle Assessment</button>":
#     st.title("Life Cycle Assessment")
#     st.markdown(
#         """
#         Welcome to Ecosynergy360, where sustainability isn't just a goal but a journey guided by Life Cycle Assessment (LCA), a powerful tool in understanding the holistic impact of projects on our environment.
#         ...
#         """
#     )
#     # Add more content for LCA section...

# if "<button class='button-style' onclick='CarbonFootprint()'>Carbon Footprint</button>":
#     st.title("Carbon Footprint")
#     st.markdown(
#         """
#         In the realm of sustainable practices, the concept of a "carbon footprint" has emerged as a crucial metric in assessing the environmental impact of human activities.
#         ...
#         """
#     )
#     # Add more content for Carbon Footprint section...

# if "<button class='button-style' onclick='Calculator()'>Calculator</button>":
#     st.title("Calculator")
#     # Add functionality for the Calculator section...


# # if st.button("Calculator", help="Explore Calculator", key="calculator_button", class_="button-style"):
# #     st.title("Calculator")
# #     phase = st.radio("Choose the phase of your project", ("Production phase", "Construction Phase"))
# #     # Add functionality for the Calculator section...


# # ##else:  # Calculator section
# #     ##st.title("Calculator")
# #     ##phase = st.radio("Choose the phase of your project", ("Production phase", "Construction Phase"))

# #     if phase == "Production phase":
# #         asphalt_type = st.radio("Choose the type of your asphalt", ("Standard Hot Mix Asphalt", "HMA with RAP"))
# #         # Add more selection choices for asphalt type and temperature...
# #         if asphalt_type == "Standard Hot Mix Asphalt":
# #             pass
# #             # Display result for Standard HMA based on selected temperature
# #             # Show the calculated CO2 emissions and details
# #             # Example: st.write(f"The total amount of CO2 for this asphalt with identifying 180 Celsius temperature in aggregate heating is...")
# #         else:
# #             pass# HMA with RAP
# #             # Display result for HMA with RAP similar to Standard HMA
# #             # Show the calculated CO2 emissions and details
# #     else:  # Construction Phase
# #         # Add functionality for the Construction Phase calculations
# #         pass
# Title and introductory text for the first page


import streamlit as st
st.title('WELCOME TO THE ECOSYNERGY360 PLATFORM ON SUSTAINABILITY ASSESSMENT')
st.markdown(
    """
    The EPSA is developed by Ecosynergy360 team, with EUs, UNEP, and UN SDG goals knowledge base that responds to infrastructure sustainability assessment in production and construction phase.
    ...
    """
)

# Create buttons for different sections
selected_section = st.sidebar.radio(
    "Select a section",
    ("Sustainability", "Life Cycle Assessment", "Carbon Footprint", "Calculator")
)

# Content for different sections
if selected_section == "Sustainability":
    st.title("Sustainability Context")
    st.markdown(
        """
        Welcome to Ecosynergy360, where sustainability is not just a concept but a commitment to securing the needs of the present generation without compromising the essential requirements of the generations to come.
        ...
        """
    )
    st.image("digital-screen-with-environment-day.jpg")
    # Add more content for Sustainability section...

elif selected_section == "Life Cycle Assessment":
    st.title("Life Cycle Assessment")
    st.markdown(
        """
        Welcome to Ecosynergy360, where sustainability isn't just a goal but a journey guided by Life Cycle Assessment (LCA), a powerful tool in understanding the holistic impact of projects on our environment.
        ...
        """
    )
    # Add more content for LCA section...

elif selected_section == "Carbon Footprint":
    st.title("Carbon Footprint")
    st.markdown(
        """
        In the realm of sustainable practices, the concept of a "carbon footprint" has emerged as a crucial metric in assessing the environmental impact of human activities.
        ...
        """
        
    )
    st.image("view-green-forest-trees-with-co2.jpg")
    # Add more content for Carbon Footprint section...

else:  # Calculator section
    # st.title("Calculator")
    # phase = st.radio("Choose the phase of your project", ("Production phase", "Construction Phase"))

    # if phase == "Production phase":
    #     asphalt_type = st.radio("Choose the type of your asphalt", ("Standard Hot Mix Asphalt", "HMA with RAP"))
    #     # Add more selection choices for asphalt type and temperature...
    #     if asphalt_type == "Standard Hot Mix Asphalt":
    #         pass
    #         # Display result for Standard HMA based on selected temperature
    #         # Show the calculated CO2 emissions and details
    #         # Example: st.write(f"The total amount of CO2 for this asphalt with identifying 180 Celsius temperature in aggregate heating is...")
    #     else:
    #         pass# HMA with RAP
    #         # Display result for HMA with RAP similar to Standard HMA
    #         # Show the calculated CO2 emissions and details
    # else:  # Construction Phase
    #     # Add functionality for the Construction Phase calculations
    #     pass
    import streamlit as st
    import pandas as pd

    # st.set_page_config(
    #     page_title="ecoSynergy360",
    #     page_icon="icons8-arrows-around-circle-64.png",
    #     #layout="wide",
    # )
    # Title and introductory text for the first page
    # st.title('WELCOME TO THE ECOSYNERGY360 PLATFORM ON SUSTAINABILITY ASSESSMENT')
    # st.markdown(
    #     """
    #     The EPSA is developed by Ecosynergy360 team...
    #     """
    # )

    # Sample data for the regression coefficients
    data = {
        'Coefficients': [0.010080678, 0.088990197],
        'Standard Error': [0.011865215, 4.86342E-05],
        't Stat': [0.849599284, 1829.786459],
        'P-value': [0.428140311, 1.79845E-18],
        'Lower 95%': [-0.018952458, 0.088871194],
        'Upper 95%': [0.039113815, 0.089109201],
        'Lower 95,0%': [-0.018952458, 0.088871194],
        'Upper 95,0%': [0.039113815, 0.089109201]
    }

    # Creating a DataFrame from the data
    df = pd.DataFrame(data, index=['Intercept', 'X Variable 1'])

    # Displaying the table using Streamlit
    st.table(df)


    # Sample coefficients data
    data = {
        "Coefficients": ["Intercept", "X Variable 1"],
        "Coeff_Values": [0.010080678, 0.088990197],
        "Std_Error": [0.011865215, 4.86342E-05]
    }
    coefficients = pd.DataFrame(data)

    # Function to calculate CO2
    def calculate_CO2(input_val, coefficients):
        intercept = coefficients.loc[coefficients['Coefficients'] == 'Intercept', 'Coeff_Values'].values[0]
        x_variable_coeff = coefficients.loc[coefficients['Coefficients'] == 'X Variable 1', 'Coeff_Values'].values[0]
        CO2 = x_variable_coeff * input_val + intercept
        return CO2

    # Streamlit app
    st.title('CO2 Calculation')

    input_val = st.number_input("Enter the value for X Variable 1:", value=0.0)
    result = calculate_CO2(input_val, coefficients)

    st.write(f"The calculated CO2 value is: {result}")
