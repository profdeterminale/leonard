import streamlit as st
import openai

# Configurez votre clé API OpenAI
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

# Titre de l'application
st.title("Mon ChatGPT Personnalisé")
st.markdown("Posez vos questions au chatbot.")

# Initialisez la session pour stocker l'historique
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": "Vous êtes un assistant utile pour répondre aux questions."}]

# Fonction pour envoyer des messages à l'API OpenAI
def chat_with_gpt(user_input):
    # Ajouter l'entrée de l'utilisateur à la session
    st.session_state["messages"].append({"role": "user", "content": user_input})
    
    try:
        # Appeler l'API OpenAI pour obtenir une réponse
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Modèle à utiliser
            messages=st.session_state["messages"]  # Historique des messages
        )
        
        # Extraire la réponse du chatbot
        reply = response["choices"][0]["message"]["content"]
        
        # Ajouter la réponse du chatbot à la session
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        
        return reply
    
    except Exception as e:
        # Gérer les erreurs liées à l'API
        return f"Erreur avec l'API OpenAI : {str(e)}"

# Interface utilisateur
user_input = st.text_input("Entrez votre question :")
if st.button("Envoyer"):
    if user_input:
        reply = chat_with_gpt(user_input)
        st.write(f"**Chatbot :** {reply}")
    else:
        st.warning("Veuillez entrer une question.")

# Afficher l'historique des messages
if st.session_state["messages"]:
    st.markdown("### Historique des conversations :")
    for message in st.session_state["messages"]:
        if message["role"] == "user":
            st.write(f"**Vous :** {message['content']}")
        elif message["role"] == "assistant":
            st.write(f"**Chatbot :** {message['content']}")
