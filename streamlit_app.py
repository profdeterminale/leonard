import streamlit as st
import openai

# Configurez votre clé API OpenAI
openai.api_key = "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"

# Titre de l'application
st.title("ChatGPT Team Chatbot")
st.markdown("### Posez une question à votre chatbot éducatif !")

# Initialisez la session
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": "Vous êtes un assistant éducatif amical."}]

# Fonction pour envoyer des messages à l'API OpenAI
def chat_with_gpt(user_input):
    st.session_state["messages"].append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=st.session_state["messages"]
    )
    reply = response["choices"][0]["message"]["content"]
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    return reply

# Interface utilisateur
user_input = st.text_input("Entrez votre question :")
if st.button("Envoyer"):
    if user_input:
        reply = chat_with_gpt(user_input)
        st.write(f"**Chatbot :** {reply}")
    else:
        st.warning("Veuillez entrer une question.")

# Historique des conversations
if st.session_state["messages"]:
    st.markdown("### Historique des conversations :")
    for message in st.session_state["messages"]:
        if message["role"] == "user":
            st.write(f"**Vous :** {message['content']}")
        elif message["role"] == "assistant":
            st.write(f"**Chatbot :** {message['content']}")
