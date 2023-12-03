
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
# st.title('WELCOME TO THE ECOSYNERGY360 PLATFORM ON SUSTAINABILITY ASSESSMENT')
# st.markdown(
#     """
#     The EPSA is developed by Ecosynergy360 team, with EUs, UNEP, and UN SDG goals knowledge base that responds to infrastructure sustainability assessment in production and construction phase.
#     ...
#     """
# )

## hhh
# Streamlit app layout
st.title("Homepage with Buttons")

# Custom CSS for button background images
st.markdown(
    """
    <style>
    .button-1 {
        background-image: url('digital-screen-with-environment-day.jpg');
        background-size: cover;
        height: 150px;
        width: 150px;
        border: none;
        outline: none;
    }
    .button-2 {
        background-image: url('LCA.png');
        background-size: cover;
        height: 150px;
        width: 150px;
        border: none;
        outline: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create buttons with associated functions and custom classes
if st.button("Button 1", key="btn1", class_="button-1"):
    pass
        #st.image("digital-screen-with-environment-day.jpg")
    # Add more content for Sustainability section...

if st.button("Button 2", key="btn2", class_="button-2"):
    pass
        #st.image("LCA.png")
## hhh

# # Create buttons for different sections
# selected_section = st.sidebar.radio(
#     "Select a section",
#     ("Sustainability", "Life Cycle Assessment", "Carbon Footprint", "Calculator")
# )

# # Content for different sections
# if selected_section == "Sustainability":
#     st.title("Sustainability Context")
#     st.markdown(
#         """
#         Welcome to Ecosynergy360, where sustainability is not just a concept but a commitment to securing the needs of the present generation without compromising the essential requirements of the generations to come.
#         ...
#         """
#     )
#     st.image("digital-screen-with-environment-day.jpg")
#     # Add more content for Sustainability section...

# elif selected_section == "Life Cycle Assessment":
#     st.title("Life Cycle Assessment")
#     st.markdown(
#         """
#         Welcome to Ecosynergy360, where sustainability isn't just a goal but a journey guided by Life Cycle Assessment (LCA), a powerful tool in understanding the holistic impact of projects on our environment.
#         ...
#         """
#     )
#     st.image("LCA.png")
#     # Add more content for LCA section...

# elif selected_section == "Carbon Footprint":
#     st.title("Carbon Footprint")
#     st.markdown(
#         """
#         In the realm of sustainable practices, the concept of a "carbon footprint" has emerged as a crucial metric in assessing the environmental impact of human activities.
#         ...
#         """
        
#     )
#     st.image("view-green-forest-trees-with-co2.jpg")
#     # Add more content for Carbon Footprint section...

# else:  # Calculator section
#     st.title("Calculator")
#     st.markdown("Step 1:")
#     phase = st.radio("Choose the phase of your project", ("Production phase", "Construction Phase"))

#     st.markdown("Step 2:")
#     if phase == "Production phase":
#         asphalt_type = st.radio("Choose the type of your asphalt", ("Standard Hot Mix Asphalt", "HMA with RAP"))
#         # Add more selection choices for asphalt type and temperature...
#         if asphalt_type == "Standard Hot Mix Asphalt":
#             import streamlit as st
#             import pandas as pd

#             # Sample data for the regression coefficients
#             data = {
#                 'Coefficients': ['-6.142848146', '0.246160952'],
#                 'Standard Error': ['0.015849729', '0.000142858'],
#                 't Stat': ['-387.5680248', '1723.119208'],
#                 'P-value': ['1.99146E-14', '2.57875E-18'],
#                 'Lower 95%': ['-6.181631035', '0.245811391'],
#                 'Upper 95%': ['-6.104065256', '0.246510512'],
#                 'Lower 95,0%': ['-6.181631035', '0.245811391'],
#                 'Upper 95,0%': ['-6.104065256', '0.246510512']
#             }

#             # Creating a DataFrame from the data
#             df = pd.DataFrame(data, index=['Intercept', 'X Variable 1'])


#             # Display the table in Streamlit
#             #st.write("Coefficients Table:", df)
#             st.markdown("Step 3:")
#             # User input for X Variable
#             user_input = st.number_input("Enter the temperature in Celcius:", value=0.0)

#             # Calculate CO2 using the formula CO2 = Coefficients["X Variable 1"] * Input + Coefficients["Intercept"]
#             coefficient_x_variable = float(data['Coefficients'][1])
#             coefficient_intercept = float(data['Coefficients'][0])

#             co2 = coefficient_x_variable * user_input + coefficient_intercept
#             co2_ = co2+4.53+4.25+7.92+10.2-7.426

#             # Display the calculated CO2
#             st.write(f"Calculated CO2: {co2_}")
#         else:
#             pass# HMA with RAP
#             # Display result for HMA with RAP similar to Standard HMA
#             # Show the calculated CO2 emissions and details
#     else:  # Construction Phase
#         # Add functionality for the Construction Phase calculations
#         pass



#     # import streamlit as st
#     # import pandas as pd

#     # # Sample data for the regression coefficients
#     # data = {
#     #     'Coefficients': ['-6.142848146', '0.246160952'],
#     #     'Standard Error': ['0.015849729', '0.000142858'],
#     #     't Stat': ['-387.5680248', '1723.119208'],
#     #     'P-value': ['1.99146E-14', '2.57875E-18'],
#     #     'Lower 95%': ['-6.181631035', '0.245811391'],
#     #     'Upper 95%': ['-6.104065256', '0.246510512'],
#     #     'Lower 95,0%': ['-6.181631035', '0.245811391'],
#     #     'Upper 95,0%': ['-6.104065256', '0.246510512']
#     # }

#     # # Creating a DataFrame from the data
#     # df = pd.DataFrame(data, index=['Intercept', 'X Variable 1'])


#     # # Display the table in Streamlit
#     # #st.write("Coefficients Table:", df)

#     # # User input for X Variable
#     # user_input = st.number_input("Enter the temperature in Celcius:", value=0.0)

#     # # Calculate CO2 using the formula CO2 = Coefficients["X Variable 1"] * Input + Coefficients["Intercept"]
#     # coefficient_x_variable = float(data['Coefficients'][1])
#     # coefficient_intercept = float(data['Coefficients'][0])

#     # co2 = coefficient_x_variable * user_input + coefficient_intercept

#     # # Display the calculated CO2
#     # st.write(f"Calculated CO2: {co2}")

