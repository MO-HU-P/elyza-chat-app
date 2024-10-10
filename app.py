from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
import streamlit as st

def initialize_session_state():
    if "memory" not in st.session_state:
        st.session_state.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
    if "messages" not in st.session_state:
        st.session_state.messages = []

def generate_response(query):
    try:
        llm = ChatOllama(
            model="elyza:jp8b",
            base_url="http://ollama-container:11434",
            temperature=0,
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", """あなたは誠実で優秀なAIアシスタントです。
            ユーザーとの会話履歴を考慮しながら、丁寧に日本語で回答してください。"""),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])

        chain = prompt | llm

        response = chain.invoke({
            "input": query,
            "chat_history": st.session_state.memory.chat_memory.messages
        })

        st.session_state.memory.chat_memory.add_user_message(query)
        st.session_state.memory.chat_memory.add_ai_message(response.content)

        return response.content
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"

def main():
    st.title("Chat with AI Assistant")
    initialize_session_state()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    query = st.chat_input("ここにメッセージを入力してください")
    
    if query:
        st.session_state.messages.append({"role": "user", "content": query})
        st.chat_message("user").markdown(query)

        response = generate_response(query)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").markdown(response)

if __name__ == "__main__":
    main()