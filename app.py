import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Brian's Product Bot",
    page_icon="💬"
)

st.title("Brian's Product Requirements Builder")
st.write("A product-management assistant built by Brian Subrin.")

suggested_prompt = """Suggest five ways PrePass could improve enrollment for fleet customers.

For each idea, provide:

- The customer problem
- The proposed improvement
- One user story
- One success metric

Treat all PrePass-specific details as assumptions requiring validation. Keep the entire response under 500 words."""

with st.expander("Suggested test prompt", expanded=True):
    st.write("Copy this example into the question box below, or adapt it for another product.")
    st.code(suggested_prompt, language=None)

client = OpenAI()

# Create conversation memory for the current browser session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask the bot a product-management question")

if question:
    # Save and display Brian's question
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    # Send the conversation to OpenAI
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.responses.create(
                    model="gpt-5.6",
                    instructions=(
                        "You are Brian's Product Bot, a practical and experienced "
                        "product-management assistant. Help with product strategy, "
                        "requirements, user stories, acceptance criteria, roadmaps, "
                        "stakeholder management, Agile delivery, risk analysis, and "
                        "process improvement. Ground recommendations in facts, logic, "
                        "evidence, and clear reasoning. Be candid, organized, and concise."
                    ),
                    input=st.session_state.messages
                )

                answer = response.output_text

            except Exception as error:
                answer = f"Something went wrong: {error}"

        st.write(answer)

    # Save the AI response
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
