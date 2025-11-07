from time import sleep
from uteis.token_manager import TokenManager as tm
from uteis.emojis import Emojis as E
import streamlit as st

class Config:
    PH_TEXTE_AREA = """  Exemplo preenchimento:
    client_id:prd-ext-cli-latam-75065-otr
    client_secret:Khgjkghkujhgkuhgkgfkyfg
    grant_type:password
    username:cliente.integration.prd
    password:Pilhgljghklujhgkjghfvkhfghgf
"""

class SidebarManager:
    def __init__(self):
        self.token_manager = tm()
        self.fill_form: bool = False
    
    def render_sidebar(self):
        st.sidebar.title(f"Token Manager {E.INFO}")

        self.fill_form = st.sidebar.checkbox("Editar credenciais como texto", value=False, key="fill_form_checkbox")

        if not self.fill_form:
            self._render_sidebar_form()
        else:
            self._render_sidebar_text_area()
            
        self._render_sidebar_token_status()
        
    def _render_sidebar_text_area(self):
        st.sidebar.text_area(
            placeholder=Config.PH_TEXTE_AREA,
            label='Preencha os dados de autenticação',
            height=200)
    
    def _render_sidebar_form(self):
        with st.sidebar.form(key="auth_form"):
            client_id = st.text_input("Client ID")
            client_secret = st.text_input("Client Secret", type="password")
            grant_type = st.text_input("Grant Type", value="password")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit_button = st.form_submit_button(label="Buscar Token")
            if submit_button:
                self._process_form_data(client_id, client_secret, grant_type, username, password)
                
    def _render_sidebar_token_status(self):
        token = ''
        if token:
            st.sidebar.success(f"{E.CHECK} Token válido!")
        else:
            st.sidebar.error(f"{E.CROSS} Nenhum token encontrado ou token inválido.")
    
    def _process_form_data(self, client_id, client_secret, grant_type, username, password):
        with st.spinner(f"{E.SEARCH}Processando dados..."):
            sleep(10)  # Simula processamento