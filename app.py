import streamlit as st
import pandas as pd

# Sample data for AI use cases
data = {
    'Department': [
        'Cards', 'Cards', 'Cards', 'Cards', 'Cards', 
        'Operations', 'Operations', 'Operations', 'Operations', 'Operations', 
        'Risk', 'Risk', 'Risk', 'Risk', 'Risk', 
        'Marketing', 'Marketing', 'Marketing', 'Marketing', 'Marketing', 
        'Finance', 'Finance', 'Finance', 'Finance', 'Finance',
        'Customer Service', 'Customer Service', 'Customer Service', 'Customer Service', 'Customer Service',
        'IT', 'IT', 'IT', 'IT', 'IT',
        'Compliance', 'Compliance', 'Compliance', 'Compliance', 'Compliance',
        'HR', 'HR', 'HR', 'HR', 'HR',
        'Legal', 'Legal', 'Legal', 'Legal', 'Legal',
        'Sales', 'Sales', 'Sales', 'Sales', 'Sales'
    ],
    'Use Case': [
        'Credit Scoring', 'Transaction Prediction', 'Fraud Detection', 'Customer Segmentation', 'Chatbots',
        'Process Automation', 'Operational Efficiency', 'Supply Chain Optimization', 'Inventory Management', 'Predictive Maintenance',
        'Risk Assessment', 'Fraud Detection Algorithms', 'Credit Risk Modelling', 'Compliance Monitoring', 'Anomaly Detection',
        'Customer Segmentation', 'Campaign Optimization', 'Market Basket Analysis', 'Sentiment Analysis', 'Churn Prediction',
        'Financial Forecasting', 'Budget Planning', 'Expense Optimization', 'Risk Management', 'Revenue Optimization',
        'Chatbots', 'Sentiment Analysis', 'Customer Feedback Analysis', 'Service Automation', 'Personalized Service',
        'IT Security', 'System Optimization', 'Data Management', 'Infrastructure Monitoring', 'Incident Management',
        'Regulatory Reporting', 'Policy Management', 'Audit Trail', 'Compliance Monitoring', 'Risk Management',
        'Employee Engagement', 'Recruitment Automation', 'Performance Analysis', 'HR Analytics', 'Employee Retention',
        'Contract Analysis', 'Case Management', 'Legal Research', 'Regulatory Compliance', 'Litigation Prediction',
        'Sales Forecasting', 'Lead Scoring', 'Customer Analytics', 'Market Analysis', 'Sales Optimization'
    ],
    'Budget (USD)': [
        2, 2, 3, 2, 1, 3, 2, 2, 1, 1, 3, 2, 2, 2, 1, 2, 3, 2, 1, 2, 3, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 2, 3, 1, 1, 2, 2, 2, 1, 1, 3, 2, 1, 2, 2, 1, 2, 1, 1, 2, 2, 3, 2, 1, 2
    ]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Set the total budget
total_budget = 10

# Streamlit App
st.title('AI Use Cases for Retail Banks')

# Step control
if 'step' not in st.session_state:
    st.session_state.step = 1

# Function to reset selections
def reset_selections():
    st.session_state.step = 1
    if 'selected_department' in st.session_state:
        del st.session_state.selected_department
    if 'selected_use_cases' in st.session_state:
        del st.session_state.selected_use_cases
    if 'remaining_budget' in st.session_state:
        del st.session_state.remaining_budget

# Step 1: Choose a Department
if st.session_state.step == 1:
    st.header('Step 1: Choose a Department')
    departments = df['Department'].unique()
    
    cols = st.columns(2)
    for i, department in enumerate(departments):
        with cols[i % 2]:
            if st.button(department):
                st.session_state.selected_department = department
                st.session_state.step = 2

# Step 2: Select Use Cases
if st.session_state.step == 2:
    st.header('Step 2: Select Use Cases')
    st.write(f'You have a total budget of ${total_budget} Mn USD to allocate.')
    
    # Filter the DataFrame based on the selected department
    filtered_df = df[df['Department'] == st.session_state.selected_department]
    
    # Ensure at least 10 use cases are shown for each department
    if len(filtered_df) < 10:
        filtered_df = pd.concat([filtered_df, filtered_df.sample(10 - len(filtered_df), replace=True)])
    
    # Initialize selected use cases
    if 'selected_use_cases' not in st.session_state:
        st.session_state.selected_use_cases = []

    # Display use cases as tiles
    cols = st.columns(2)
    for index, row in filtered_df.iterrows():
        with cols[index % 2]:
            if st.button(f"{row['Use Case']} (${row['Budget (USD)']} Mn USD)", key=row['Use Case']):
                st.session_state.selected_use_cases.append((row['Use Case'], row['Budget (USD)']))
                st.session_state.remaining_budget = total_budget - sum([use_case[1] for use_case in st.session_state.selected_use_cases])

    # Display remaining budget
    st.write(f'Remaining Budget: ${st.session_state.remaining_budget} Mn USD')
    
    # Proceed to the next step
    if st.button('Provide roadmap and ROI'):
        st.session_state.step = 3

# Step 3: Request Roadmap
if st.session_state.step == 3:
    st.header('Step 3: Request Roadmap')
    
    if st.session_state.selected_use_cases:
        st.subheader('Selected Use Cases')
        for use_case in st.session_state.selected_use_cases:
            st.write(f"{use_case[0]}: ${use_case[1]} Mn USD")
        
        # Form for user details
        st.subheader('Provide your details')
        name = st.text_input('Name')
        company = st.text_input('Company')
        email = st.text_input('Email')
        phone = st.text_input('Phone (optional)')
        
        if st.button('Submit'):
            st.write(f'Thank you, {name}. The roadmap and ROI details will be sent to {email} shortly.')
            reset_selections()
    else:
        st.write('No use cases selected.')

if st.button('Restart'):
    reset_selections()

