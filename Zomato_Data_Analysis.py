import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Zomato Data Analysis", layout="wide")

# Title
st.title("🍽️ Zomato Restaurant Data Analysis")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Zomato-data-.csv")
    
    # Clean rate column
    def handleRate(value):
        value = str(value).split('/')
        return float(value[0])
    
    df['rate'] = df['rate'].apply(handleRate)
    return df

df = load_data()

# Show dataset
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Sidebar filters
st.sidebar.header("Filters")

restaurant_type = st.sidebar.multiselect(
    "Select Restaurant Type",
    options=df['listed_in(type)'].unique(),
    default=df['listed_in(type)'].unique()
)

online_order = st.sidebar.multiselect(
    "Online Order Available",
    options=df['online_order'].unique(),
    default=df['online_order'].unique()
)

filtered_df = df[
    (df['listed_in(type)'].isin(restaurant_type)) &
    (df['online_order'].isin(online_order))
]

# --- Visualization 1: Restaurant Type Count
st.subheader("📊 Restaurant Type Distribution")
fig1, ax1 = plt.subplots()
sns.countplot(x=filtered_df['listed_in(type)'], ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# --- Visualization 2: Votes by Type
st.subheader("📈 Votes by Restaurant Type")
grouped_data = filtered_df.groupby('listed_in(type)')['votes'].sum()

fig2, ax2 = plt.subplots()
ax2.plot(grouped_data.index, grouped_data.values, marker='o', color='green')
plt.xticks(rotation=45)
st.pyplot(fig2)

# --- Visualization 3: Online Orders
st.subheader("🛒 Online Order Availability")
fig3, ax3 = plt.subplots()
sns.countplot(x=filtered_df['online_order'], ax=ax3)
st.pyplot(fig3)

# --- Visualization 4: Ratings Distribution
st.subheader("⭐ Rating Distribution")
fig4, ax4 = plt.subplots()
ax4.hist(filtered_df['rate'], bins=5)
st.pyplot(fig4)

# --- Visualization 5: Cost for Two
st.subheader("💰 Cost for Two Distribution")
fig5, ax5 = plt.subplots()
sns.countplot(x=filtered_df['approx_cost(for two people)'], ax=ax5)
plt.xticks(rotation=45)
st.pyplot(fig5)

# --- Visualization 6: Boxplot (Online vs Rating)
st.subheader("📦 Ratings: Online vs Offline")
fig6, ax6 = plt.subplots()
sns.boxplot(x='online_order', y='rate', data=filtered_df, ax=ax6)
st.pyplot(fig6)

# --- Visualization 7: Heatmap
st.subheader("🔥 Order Mode Preference by Type")
pivot_table = filtered_df.pivot_table(
    index='listed_in(type)',
    columns='online_order',
    aggfunc='size',
    fill_value=0
)

fig7, ax7 = plt.subplots()
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d', ax=ax7)
st.pyplot(fig7)

# --- Max Votes Restaurant
st.subheader("🏆 Most Voted Restaurant")
max_votes = filtered_df['votes'].max()
res = filtered_df[filtered_df['votes'] == max_votes]['name']
st.write(res)