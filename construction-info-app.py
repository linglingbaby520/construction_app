import streamlit as st

# Updated App Title and Intro
st.title("🏗️ Blueprint: Construction Expert Assistant")
st.write("Ask any question related to construction, building codes, materials, or site safety, and get an instant professional answer!")

# Input box for the user's construction question
user_question = st.text_input(
    "What do you want to know about construction?", 
    placeholder="e.g., What is the standard spacing for residential wall studs?"
)

# Generate answer logic when the button is clicked
if st.button("Ask Blueprint 🛠️"):
    if user_question.strip() == "":
        st.warning("Please type a question first!")
    else:
        st.markdown("---")
        st.subheader("💡 Expert Answer")
        
        # Simple simulated knowledge base or rules for construction answers
        question_lower = user_question.lower()
        
        if "stud" in question_lower or "wall" in question_lower:
            answer = (
                "For standard residential wood-framed construction, wall studs are typically spaced "
                "either **16 inches on center (oc)** or **24 inches on center (oc)**, depending on the load "
                "requirements and exterior finishing materials used."
            )
        elif "concrete" in question_lower or "foundation" in question_lower:
            answer = (
                "Standard residential concrete foundations typically require a minimum compressive strength "
                "of **2,500 to 3,000 PSI (pounds per square inch)**, though local building codes and frost-line "
                "depths will dictate exact thickness, reinforcement rebar placement, and footing dimensions."
            )
        elif "safety" in question_lower or "ppe" in question_lower:
            answer = (
                "Standard job site Personal Protective Equipment (PPE) requirements typically include: "
                "a certified hard hat, safety glasses with side shields, high-visibility vests, steel-toe boots, "
                "and hearing protection when operating heavy machinery or loud power tools."
            )
        else:
            answer = (
                f"That is a great question about **'{user_question}'**. In general, successful construction projects "
                "depend heavily on clear architectural blueprints, strict adherence to local building codes, proper site safety "
                "protocols, and continuous communication between subtrades, project managers, and general contractors."
            )
            
        st.write(answer)
        st.info("Tip: You can expand this logic or connect it to an AI language model API later to answer any custom question dynamically!")
