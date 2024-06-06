import streamlit as st
import pandas as pd

# Sample data for AI use cases
data = {
    'Department': ['Cards', 'Cards', 'Cards', 'Cards', 'Cards', 'Operations', 'Operations', 'Operations', 'Operations', 'Operations', 
                   'Risk', 'Risk', 'Risk', 'Risk', 'Risk', 'Marketing', 'Marketing', 'Marketing', 'Marketing', 'Marketing', 
                   'Finance', 'Finance', 'Finance', 'Finance', 'Finance'],
    'Use Case': ['Credit Scoring', 'Transaction Prediction', 'Fraud Detection', 'Customer Segmentation', 'Chatbots', 
                 'Process Automation', 'Operational Efficiency', 'Supply Chain Optimization', 'Inventory Management', 'Predictive Maintenance', 
                 'Risk Assessment', 'Fraud Detection Algorithms', 'Credit Risk Modelling', 'Compliance Monitoring', 'Anomaly Detection', 
                 'Customer Segmentation', 'Campaign Optimization', 'Market Basket Analysis', 'Sentiment Analysis', 'Churn Prediction', 
                 'Financial Forecasting', 'Budget Planning', 'Expense Optimization', 'Risk Management', 'Revenue Optimization'],
    'Budget (USD)': [2, 2, 3, 2, 1, 3, 2, 2, 1, 1, 3, 2, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 1, 2]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Set the total budget
total_budget = 10

# Streamlit App
st.title('AI Use Cases for Retail Banks')

# Step 1: Choose a Department
st.header('Step 1: Choose a Department')
departments = df['Department'].unique()
selected_department = st.selectbox('Select Department', departments)

# Filter the DataFrame based on the selected department
filtered_df = df[df['Department'] == selected_department]

# Step 2: Display Relevant Use Cases
st.header('Step 2: Select Use Cases')
st.write(f'You have a total budget of ${total_budget} Mn USD to allocate.')
selected_use_cases = []
remaining_budget = total_budget

# Display use cases with checkboxes
for index, row in filtered_df.iterrows():
    if st.checkbox(f"{row['Use Case']} (${row['Budget (USD)']} Mn USD)", key=row['Use Case']):
        if remaining_budget >= row['Budget (USD)']:
            selected_use_cases.append((row['Department'], row['Use Case'], row['Budget (USD)']))
            remaining_budget -= row['Budget (USD)']
        else:
            st.warning(f"Not enough budget to select {row['Use Case']}")

# Display remaining budget
st.write(f'Remaining Budget: ${remaining_budget} Mn USD')

# Step 3: Request Roadmap
if selected_use_cases:
    st.header('Step 3: Request Roadmap')
    st.subheader('Selected Use Cases')
    for use_case in selected_use_cases:
        st.write(f"{use_case[1]}: ${use_case[2]} Mn USD")

    if st.button('Request Roadmap'):
        st.write('Roadmap Requested:')
        for use_case in selected_use_cases:
            st.write(f"{use_case[1]}")
else:
    st.write('No use cases selected.')
