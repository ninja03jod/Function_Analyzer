import streamlit as st
from langchain_community.llms import Ollama

# Initialize the Llama model from Ollama
llm = Ollama(model='llama3')

def generate_function_details(function_code):
    prompt = f"""
Analyze the following function and generate the following details:
1. Description
2. Parameters
3. Return Types
4. Test Cases
5. Optimized and Rewritten Functions
6. Detect the bugs in code and make it correct
7. Variable Descriptions

Function:
{function_code}

Details:
"""
    # Generate the response
    response = llm(prompt)
    return response

def parse_details(details):
    parts = ["Description", "Parameters", "Return Types", "Test Cases", "Optimized and Rewritten Functions", "Bugs", "Variable Descriptions"]
    details_dict = {part: "" for part in parts}
    
    for i, part in enumerate(parts):
        start = details.find(part)
        if start != -1:
            if i + 1 < len(parts):
                end = details.find(parts[i + 1])
            else:
                end = len(details)
            details_dict[part] = details[start + len(part) + 1:end].strip()
    
    return details_dict

# Streamlit app
st.title("Function Analyzer")

function_code = st.text_area("Enter the function code here:")

if st.button("Analyze Function"):
    if function_code:
        details = generate_function_details(function_code)
        details_dict = parse_details(details)
        
        for part, content in details_dict.items():
            st.header(part)
            st.text_area(f"{part}:", content, height=150)
    else:
        st.warning("Please enter the function code.")