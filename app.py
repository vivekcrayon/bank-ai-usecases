import streamlit as st
import pandas as pd

# Sample data for AI use cases
data = {
    'Department': ['Cards', 'Loans', 'Customer Service', 'Fraud Detection', 'Marketing'],
    'Use Case': [
        'Credit Scoring', 'Loan Approval Automation', 'Chatbots', 'Fraud Detection Algorithms', 'Customer Segmentation',
        'Transaction Prediction', 'Risk Assessment', 'Sentiment Analysis', 'Anomaly Detection', 'Campaign Optimization'
    ],
    'Budget (USD)': [2, 3, 1, 2, 2, 2, 2, 1, 1, 3]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Set the total budget
total_budget = 10

# Streamlit App
st.title('AI Use Cases for Retail Banks')

st.write(f'You have a total budget of ${total_budget} Mn USD to allocate.')

# Display use cases with checkboxes
selected_use_cases = []
remaining_budget = total_budget

for index, row in df.iterrows():
    if st.checkbox(f"{row['Department']} - {row['Use Case']} (${row['Budget (USD)']} Mn USD)", key=index):
        selected_use_cases.append((row['Department'], row['Use Case'], row['Budget (USD)']))
        remaining_budget -= row['Budget (USD)']

# Display remaining budget
st.write(f'Remaining Budget: ${remaining_budget} Mn USD')

# Display selected use cases and option to request a roadmap
if selected_use_cases:
    st.subheader('Selected Use Cases')
    for use_case in selected_use_cases:
        st.write(f"{use_case[0]} - {use_case[1]}: ${use_case[2]} Mn USD")

    if st.button('Request Roadmap'):
        st.write('Roadmap Requested:')
        for use_case in selected_use_cases:
            st.write(f"{use_case[0]} - {use_case[1]}")
else:
    st.write('No use cases selected.')
