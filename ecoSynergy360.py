
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

# Create buttons for different sections
options = ['Home','Sustainability', 'Life Cycle Assessment', 'Carbon Footprint','Calculator']
default_option = 'Home'  # Set 'Home' as the default selection

selected_section = st.radio('Select an option:', options, index=options.index(default_option))
#
# selected_section = st.sidebar.radio(
#     "Select a section",
#     ("Sustainability", "Life Cycle Assessment", "Carbon Footprint", "Calculator")
# )

# Content for different sections
if selected_section == "Home":
    st.title("Home")
    st.markdown(
        """
        WELCOME TO THE ECOSYNERGY360 PLATFORM ON SUSTAINABILITY ASSESSMENT

        The EPSA is developed by Ecosynergy360 team, with EUs, UNEP, and UN SDG goals knowledge base that responds to infrastructure sustainability assessment in production and construction phase.
        The EPSA supports the methodological development of Life Cycle Assessment (LCA) for the analysis of Environmental, Social and Economy aspects of a project.
        The EPSA fosters LCA as an essential integrated environmental assessment in support to minimize CO2 amount during production and construction phase of infrastructure projects.
        """
    )
elif selected_section == "Sustainability":
    st.title("Sustainability")
    st.markdown(
        """
        Welcome to Ecosynergy360, where sustainability is not just a concept but a commitment to securing the needs of the present generation without compromising the essential requirements of the generations to come.
        In the dynamic landscape of infrastructure development currently unfolding across Europe, a critical question arises – are these projects aligning with the imperatives of sustainable development goals and the zero-carbon concept?
        At Ecosynergy360, we strive to be the catalyst for positive change. We aim to assist engineers, institutions, governments, and private companies in assessing the sustainability of their projects during the crucial phases of design and planning. Our goal is clear: to align these initiatives with the Sustainable Development Goals (SDGs) set for 2030 and guide them on the path to sustainable development.
        Understanding that there are numerous methods to assess the sustainability of a project, Ecosynergy360 has adopted a Life Cycle Assessment-based methodology. This approach allows us to comprehensively evaluate the impact of projects and contribute to informed decision-making.
        The sustainability context, as we see it, encompasses three pillars – Environmental, Social, and Economic. In the current phase of development of the Ecosynergy360 web calculator, our primary focus is on the environmental sustainability pillar, specifically in the realm of road pavement infrastructure for Hot Mix Asphalt (HMA).
        While acknowledging the myriad indicators crucial for a holistic sustainability assessment, our web-based calculator is tailored to analyze and calculate the environmental sustainability of HMA road pavement infrastructure. At this juncture, our concentration is on the quantification of CO2 equivalent emissions during the production phase of Hot Mix Asphalt design.
        Join us on this journey towards a more sustainable future. Explore the Ecosynergy360 web calculator and empower your projects to lead the way in environmental sustainability.

        Sustainability starts with informed decisions – let's pave the way together.

        Ecosynergy360 Team

        """
    )
    st.image("digital-screen-with-environment-day.jpg")
    # Add more content for Sustainability section...

elif selected_section == "Life Cycle Assessment":
    st.title("Life Cycle Assessment")
    st.markdown(
        """
        Welcome to Ecosynergy360, where sustainability isn't just a goal but a journey guided by Life Cycle Assessment (LCA), a powerful tool in understanding the holistic impact of projects on our environment.
        In the ever-evolving landscape of infrastructure projects across Europe, the need for comprehensive assessments has never been more apparent. Are these endeavors aligned with sustainable development goals and the imperative to achieve a zero-carbon footprint?
        Recognizing the diverse methodologies available for assessing sustainability, Ecosynergy360 has chosen to employ Life Cycle Assessment. LCA allows us to go beyond isolated considerations and thoroughly evaluate the environmental impact of projects from inception to completion.
        LCA considers the entire life cycle of a project, encompassing raw material extraction, production, construction, operation, and end-of-life disposal or recycling. This approach enables a comprehensive understanding of the environmental, social, and economic aspects, fostering informed decision-making.
        Our web-based calculator is designed to analyze and calculate the environmental impact of HMA road pavement infrastructure projects using LCA principles. In this phase, our concentration is on quantifying CO2 equivalent emissions during the production phase of Hot Mix Asphalt design.
        Join us in this journey towards a more sustainable future. Explore the Ecosynergy360 web calculator and embrace the power of Life Cycle Assessment in steering your projects toward environmental sustainability.
        Sustainability through every phase – let's assess, adapt, and advance together.

        Ecosynergy360 Team
        """
    )
    st.image("LCA.png")
    # Add more content for LCA section...

elif selected_section == "Carbon Footprint":
    st.title("Carbon Footprint")
    st.markdown(
        """
        In the realm of sustainable practices, the concept of a "carbon footprint" has emerged as a crucial metric in assessing the environmental impact of human activities. Ecosynergy360 welcomes you to delve into the intricacies of carbon foot printing—a key tool in quantifying greenhouse gas emissions associated with the production, consumption, and disposal of goods and services.
        As the global community grapples with the urgent need for sustainable practices, understanding and mitigating carbon footprints have become imperative. Ecosynergy360, rooted in academic knowledge, endeavors to shed light on this intricate subject to facilitate informed decision-making in various sectors.
        A carbon footprint encompasses the total amount of greenhouse gases, primarily carbon dioxide (CO2) but also including methane (CH4) and nitrous oxide (N2O), emitted directly or indirectly by an individual, organization, event, or product. It serves as a tangible measure of the environmental impact, providing insights into areas where reductions and sustainable alternatives can be implemented.
        Ecosynergy360 recognizes the academic underpinnings of carbon footprint assessments. Our approach integrates established methodologies and scientific principles to offer a comprehensive understanding of emissions across the life cycle of a product or activity. By doing so, we empower individuals, businesses, and institutions to make informed choices that align with global sustainability objectives.
        Our commitment extends beyond mere awareness. In the pursuit of academic rigor, we have developed a web calculator that focuses on the precise calculation of CO2 equivalent emissions during the production phase of Hot Mix Asphalt (HMA) in road pavement infrastructure. This calculator is a testament to our dedication to integrating academic knowledge into practical tools for sustainable decision-making.
        Join us in exploring the academic intricacies of carbon footprints and discover the role it plays in shaping a sustainable future. Explore the Ecosynergy360 web calculator and embark on a journey toward reducing carbon footprints and fostering a more sustainable world.
        In academia and action, we strive for a world where every step leaves a lighter carbon imprint.

        Ecosynergy360 Team
        """
        
    )
    st.image("view-green-forest-trees-with-co2.jpg")
    # Add more content for Carbon Footprint section...

else:  # Calculator section
    st.title("Calculator")
    st.markdown("Step 1:")
    phase = st.radio("Choose the phase of your project", ("Production phase", "Construction Phase"))

    st.markdown("Step 2:")
    if phase == "Production phase":
        asphalt_type = st.radio("Choose the type of your asphalt", ("Standard Hot Mix Asphalt", "HMA with RAP"))
        # Add more selection choices for asphalt type and temperature...
        if asphalt_type == "Standard Hot Mix Asphalt":
            import streamlit as st
            import pandas as pd

            # Sample data for the regression coefficients
            data = {
                'Coefficients': ['-6.142848146', '0.246160952'],
                'Standard Error': ['0.015849729', '0.000142858'],
                't Stat': ['-387.5680248', '1723.119208'],
                'P-value': ['1.99146E-14', '2.57875E-18'],
                'Lower 95%': ['-6.181631035', '0.245811391'],
                'Upper 95%': ['-6.104065256', '0.246510512'],
                'Lower 95,0%': ['-6.181631035', '0.245811391'],
                'Upper 95,0%': ['-6.104065256', '0.246510512']
            }

            # Creating a DataFrame from the data
            df = pd.DataFrame(data, index=['Intercept', 'X Variable 1'])


            # Display the table in Streamlit
            #st.write("Coefficients Table:", df)
            st.markdown("Step 3:")
            # User input for X Variable
            user_input = st.number_input("Enter the temperature in Celcius:", value=0.0)

            # Calculate CO2 using the formula CO2 = Coefficients["X Variable 1"] * Input + Coefficients["Intercept"]
            coefficient_x_variable = float(data['Coefficients'][1])
            coefficient_intercept = float(data['Coefficients'][0])

            co2 = coefficient_x_variable * user_input + coefficient_intercept
            co2_ = co2+4.53+4.25+7.92+10.2-7.426

            # Display the calculated CO2
            st.write(f"Calculated CO2 eq amount for 1000 kg asphalt production: {co2_}")
        else:
            pass# HMA with RAP
            # Display result for HMA with RAP similar to Standard HMA
            # Show the calculated CO2 emissions and details
    else:  # Construction Phase
        # Add functionality for the Construction Phase calculations
        pass



    # import streamlit as st
    # import pandas as pd

    # # Sample data for the regression coefficients
    # data = {
    #     'Coefficients': ['-6.142848146', '0.246160952'],
    #     'Standard Error': ['0.015849729', '0.000142858'],
    #     't Stat': ['-387.5680248', '1723.119208'],
    #     'P-value': ['1.99146E-14', '2.57875E-18'],
    #     'Lower 95%': ['-6.181631035', '0.245811391'],
    #     'Upper 95%': ['-6.104065256', '0.246510512'],
    #     'Lower 95,0%': ['-6.181631035', '0.245811391'],
    #     'Upper 95,0%': ['-6.104065256', '0.246510512']
    # }

    # # Creating a DataFrame from the data
    # df = pd.DataFrame(data, index=['Intercept', 'X Variable 1'])


    # # Display the table in Streamlit
    # #st.write("Coefficients Table:", df)

    # # User input for X Variable
    # user_input = st.number_input("Enter the temperature in Celcius:", value=0.0)

    # # Calculate CO2 using the formula CO2 = Coefficients["X Variable 1"] * Input + Coefficients["Intercept"]
    # coefficient_x_variable = float(data['Coefficients'][1])
    # coefficient_intercept = float(data['Coefficients'][0])

    # co2 = coefficient_x_variable * user_input + coefficient_intercept

    # # Display the calculated CO2
    # st.write(f"Calculated CO2: {co2}")

