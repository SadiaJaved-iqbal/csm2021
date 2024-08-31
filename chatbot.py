import streamlit as st
import PyPDF2

# Load the PDF
def load_pdf(pdf_path):
    with open(r"C:\Users\hp\Downloads\CSM2021\CSM2021.pdf", "rb") as file:
        reader = PyPDF2.PdfReader(file)
        pdf_text = ""
        for page in reader.pages:
            pdf_text += page.extract_text()
    return pdf_text

# Sample knowledge base
knowledge_base = {
    "new connection": "To apply for a new electricity connection, you need to submit a completed application form, copies of your national ID card, and proof of ownership of the property. The process takes around 2-4 weeks.",
    "billing issue": "If you have a billing discrepancy, you can file a complaint through the nearest customer service center or online. NEPRA requires resolution within 15 days.",
    "disconnection": "Electricity disconnection can occur due to unpaid bills or meter tampering. Reconnection can be requested after payment of dues and a reconnection fee.",
    "tariff": "NEPRA offers various tariff categories such as residential, commercial, and industrial. You can apply to switch your tariff category if you meet the eligibility criteria.",
    "load shedding": "Load shedding is scheduled due to supply constraints. You can check your load shedding schedule with your local distribution company.",
    "complaint resolution": "NEPRA’s complaint resolution timeline is typically 15 to 30 days, depending on the type of complaint.",
    "safety": "NEPRA advises keeping clear of high voltage wires and not tampering with meters. Any meter tampering may lead to heavy penalties.",
    "consumer rights": "As a consumer, you have the right to fair billing, safe electricity supply, and a complaint mechanism through NEPRA.",
    "dispute resolution": "If your complaint is not resolved, you can escalate it to the NEPRA dispute resolution body for further action.",
    "energy conservation": "To save on electricity, use energy-efficient appliances, turn off unnecessary lights, and consider using solar panels if possible."
}

# Chatbot response function
def get_response(user_query):
    for key in knowledge_base.keys():
        if key in user_query.lower():
            return knowledge_base[key]
    return "Sorry, I don't have information on that. Please refer to the NEPRA manual."

# Streamlit UI
def main():
    st.title("NEPRA Customer Support Chatbot")
    st.write("This chatbot provides information from the NEPRA Consumer Service Manual (CSM 2021). Ask your questions below.")
    
    # Input for user query
    user_query = st.text_input("Enter your query:")
    
    if user_query:
        # Get chatbot response
        response = get_response(user_query)
        
        # Display the response
        st.write("**Response:**")
        st.write(response)

if __name__ == '__main__':
    main()
