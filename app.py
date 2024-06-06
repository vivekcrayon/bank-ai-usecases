import streamlit as st
import pandas as pd

# Sample data for AI use cases
data = {
    'Division': ['Credit Cards', 'Credit Cards', 'Credit Cards', 'Credit Cards', 'Credit Cards', 
                 'Debit Cards', 'Debit Cards', 'Debit Cards', 'Debit Cards', 'Debit Cards', 
                 'Branch Operations', 'Branch Operations', 'Branch Operations', 'Branch Operations', 'Branch Operations', 
                 'Risk', 'Risk', 'Risk', 'Risk', 'Risk', 
                 'Marketing', 'Marketing', 'Marketing', 'Marketing', 'Marketing', 
                 'Digital', 'Digital', 'Digital', 'Digital', 'Digital'],
    'Use Case': ['Credit Scoring', 'Transaction Prediction', 'Fraud Detection', 'Customer Segmentation', 'Chatbots', 
                 'Transaction Monitoring', 'Fraud Prevention', 'Card Activation', 'ATM Management', 'Customer Service', 
                 'Branch Efficiency', 'Customer Relationship Management', 'Transaction Processing', 'Customer Support', 'Queue Management', 
                 'Risk Assessment', 'Fraud Detection Algorithms', 'Credit Risk Modelling', 'Compliance Monitoring', 'Anomaly Detection', 
                 'Customer Segmentation', 'Campaign Optimization', 'Market Basket Analysis', 'Sentiment Analysis', 'Churn Prediction', 
                 'Digital Banking', 'Mobile Wallet', 'Online Account Opening', 'AI Chatbots', 'Customer Experience Enhancement'],
    'Budget (USD)': [2, 2, 3, 2, 1, 3, 2, 2, 1, 1, 
                     3, 2, 2, 2, 1, 2, 3, 2, 1, 2, 
                     3, 2, 2, 1, 2, 3, 2, 2, 1, 2]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

def initialize_session_state():
    if 'step' not in st.session_state:
        st.session_state.step = 1

    if 'remaining_budget' not in st.session_state:
        st.session_state.remaining_budget = None

    if 'selected_use_cases' not in st.session_state:
        st.session_state.selected_use_cases = []

def choose_division():
    st.header('Step 1: Choose a Division')
    divisions = df['Division'].unique()
    
    for division in divisions:
        if st.button(division):
            st.session_state.selected_division = division
            st.session_state.step = 2

def select_use_cases():
    st.header('Step 2: Select Use Cases')
    st.write('Allocate your budget to select the use cases.')
    
    # Filter the DataFrame based on the selected division
    filtered_df = df[df['Division'] == st.session_state.selected_division]

    # Display use cases as checkboxes
    for index, row in filtered_df.iterrows():
        budget = st.number_input(f"{row['Use Case']} (${row['Budget (USD)']} Mn USD)", min_value=0)
        if budget > 0:
            st.session_state.selected_use_cases.append((row['Use Case'], budget))

    # Proceed to the next step
    if st.button('Provide roadmap and ROI'):
        st.session_state.step = 3

def request_roadmap():
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

def reset_selections():
    st.session_state.step = 1
    if 'selected_division' in st.session_state:
        del st.session_state.selected_division
    if 'selected_use_cases' in st.session_state:
        del st.session_state.selected_use_cases
    if 'remaining_budget' in st.session_state:
        del st.session_state.remaining_budget

def main():
    st.title('AI Use Cases for Retail Banks')
    initialize_session_state()

    if st.session_state.step == 1:
        choose_division()
    elif st.session_state.step == 2:
        select_use_cases()
    elif st.session_state.step == 3:
        request_roadmap()

    if st.button('Restart'):
        reset_selections()

if __name__ == "__main__":
    main()
