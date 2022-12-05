import streamlit as st
import plotly.express as px
import pandas as pd




#load scrapped data
df = pd.read_csv("C:\\Users\\Yacine Mam'd\\Desktop\\2IA\\delpha\\collected_data\\delpha_data.txt")

#STREAMLIT WEBAPP

#configuration
st.set_page_config(page_title="Companies Dashboard",
                   layout="wide")

#TITLE
st.title("What's About Companies :question: ")



# WEBSITE AND SOCIAL MEDIA

# With a Sidebar: select the companies whose links you want

#Subheader 
st.header(":link: Links")

#Sidebar

#instanciate object st.sidebar
company = st.sidebar.multiselect("Select the Company:",
                                   options=df["Name"],
                                   default=df["Name"][0]
                                       )

#save the selected companies in the variable df_selection
df_selection = df.query(
    "Name == @company"
    )


#Display website and linkedin links on the left and right respectively

#left and right
linkedin_column, website_column = st.columns(2)

#Display
linkedin = df_selection["LinkedIn"]
website = df_selection["Site Web"]

with linkedin_column :
    
    st.subheader("LinkedIn :")
    for link in list(linkedin) :
        st.write(f"{link}")

with website_column :
    
    st.subheader(f"Site Web :")
    for web in list(website):
        st.write(f"{web}")

#Make a  visible separation
st.markdown("---")

#Display barplots of "Effectif" and "Revenue"
st.header("Workforce and Revenue")

#plotly barplots figures
fig_effectif = px.bar(df_selection, x="Name", y="Effectif", title="<b> Comparaison des effectifs </b>")
fig_revenue = px.bar(df_selection, x="Name", y="Revenue", title="<b> Comparaison des revenues </b>")

#Display respectively on left and right side
effectif_column, revenue_column = st.columns(2)

effectif_column.plotly_chart(fig_effectif, use_container_width=True)
revenue_column.plotly_chart(fig_revenue, use_container_width=True)

#Make a  visible separation
st.markdown("---")

#Map
st.header(":round_pushpin: Headquarters")

#plotly map
fig_map = px.scatter_geo(df_selection, lat="Latitude", lon="Longitude", hover_name="Name")

#display
st.plotly_chart(fig_map, use_container_width=True)

# HIDE STRAMLIT STYLE

hide_st_style = """
            <style>
            #MainMenu {visibility : hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

