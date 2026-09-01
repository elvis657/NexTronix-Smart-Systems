import streamlit as st
from openai import OpenAI
import os

# ==========================================================
# CONFIGURACIÓN DE PÁGINA
# ==========================================================

st.set_page_config(
    page_title="Ing. Elvis Bot | NEXTRONIX",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# ESTILOS CSS
# ==========================================================

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at top left, rgba(0, 102, 255, 0.18), transparent 30%),
        radial-gradient(circle at bottom right, rgba(255, 193, 7, 0.08), transparent 30%),
        linear-gradient(135deg, #020914 0%, #07172b 50%, #03101d 100%);
    color: white;
}

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #04101f 0%, #0b2447 55%, #06111f 100%);
    border-right: 1px solid rgba(62, 144, 255, 0.35);
}

section[data-testid="stSidebar"] * {
    color: white;
}

.nex-header {
    background: linear-gradient(120deg, rgba(8, 48, 101, 0.97), rgba(5, 17, 35, 0.98));
    border: 1px solid rgba(69, 151, 255, 0.55);
    border-radius: 24px;
    padding: 30px 34px;
    margin-bottom: 25px;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.35), 0 0 30px rgba(0, 119, 255, 0.10);
}

.company {
    font-size: 31px;
    font-weight: 900;
    letter-spacing: 1.2px;
    color: #ffffff;
}

.company-small {
    margin-top: 5px;
    font-size: 13px;
    letter-spacing: 2px;
    color: #a8c8f5;
}

.bot-name {
    margin-top: 18px;
    font-size: 52px;
    font-weight: 900;
    background: linear-gradient(90deg, #ffffff, #7cbcff, #ffd76b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.bot-subtitle {
    margin-top: 8px;
    font-size: 17px;
    color: #d5e7ff;
    line-height: 1.6;
}

.status {
    display: inline-block;
    margin-top: 18px;
    padding: 7px 15px;
    border-radius: 30px;
    background: rgba(29, 175, 90, 0.15);
    border: 1px solid rgba(72, 236, 136, 0.40);
    color: #76f3a7;
    font-weight: 700;
    font-size: 13px;
}

.nex-card {
    min-height: 150px;
    background: rgba(8, 28, 54, 0.90);
    border: 1px solid rgba(67, 149, 255, 0.28);
    border-radius: 20px;
    padding: 20px;
    margin-bottom: 12px;
    box-shadow: 0 8px 22px rgba(0, 0, 0, 0.24);
}

.nex-card h3 {
    color: #7bbcff;
    margin-top: 0;
}

.nex-card p {
    color: #dbe9ff;
    line-height: 1.5;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: 1px solid #3d91ff;
    background: linear-gradient(90deg, #0750a7, #0e73e8);
    color: white;
    font-weight: 700;
}

.stButton > button:hover {
    border-color: #ffd45f;
    background: linear-gradient(90deg, #0c61c8, #1687ff);
    color: white;
    box-shadow: 0 0 18px rgba(47, 137, 255, 0.32);
}

div[data-baseweb="select"] > div {
    background: #091c35;
    color: white;
    border: 1px solid #3279d0;
    border-radius: 12px;
}

[data-testid="stChatMessage"] {
    border-radius: 18px;
    padding: 8px;
    margin-bottom: 10px;
}

[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
    background: rgba(28, 93, 174, 0.18);
    border: 1px solid rgba(76, 159, 255, 0.23);
}

[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
    background: rgba(10, 31, 59, 0.86);
    border: 1px solid rgba(255, 200, 70, 0.22);
}

[data-testid="stChatInput"] {
    background: rgba(7, 23, 44, 0.96);
    border-radius: 18px;
}

.footer {
    margin-top: 42px;
    padding: 22px;
    text-align: center;
    border-top: 1px solid rgba(75, 147, 240, 0.20);
    color: #8fa9ca;
    font-size: 13px;
}

.footer strong {
    color: white;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: transparent;
}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""
<div class="nex-header">
<div class="company">⚡ NEXTRONIX SMART SYSTEMS S.A.C.</div>
<div class="company-small">ELECTRICIDAD • ELECTRÓNICA • AUTOMATIZACIÓN • HVAC • INTELIGENCIA ARTIFICIAL</div>
<div class="bot-name">🤖 Ing. Elvis Bot</div>
<div class="bot-subtitle">
Asistente técnico inteligente para electrónica, electricidad, PLC,
automatización industrial, motores, HVAC, mantenimiento e inteligencia artificial.
</div>
<div class="status">● SISTEMA ACTIVO</div>
</div>
""", unsafe_allow_html=True)

# ==========================================================
# OPENAI
# ==========================================================

api_key = os.getenv("OPENAI_API_KEY")

# En Streamlit Cloud, guarda la clave en Settings > Secrets como:
# OPENAI_API_KEY = "sk-..."
if not api_key:
    try:
        api_key = st.secrets.get("OPENAI_API_KEY", None)
    except Exception:
        api_key = None

client = None
if api_key:
    try:
        client = OpenAI(api_key=api_key)
    except Exception:
        client = None

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.markdown("""
<div style="text-align:center; padding:10px 0 25px 0;">
<div style="font-size:30px; font-weight:900; color:#72b5ff;">⚡ NEXTRONIX</div>
<div style="color:#b5cae6; font-size:12px; letter-spacing:1.5px;">SMART SYSTEMS S.A.C.</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("## 🤖 Ing. Elvis Bot")

especialidad = st.sidebar.selectbox(
    "Selecciona una especialidad",
    [
        "⚡ Electricidad",
        "🔌 Electrónica",
        "🏭 PLC y Automatización",
        "⚙️ Motores eléctricos",
        "❄️ HVAC y Refrigeración",
        "🧠 Inteligencia Artificial",
        "🛠️ Mantenimiento industrial",
        "💬 Consulta general"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📡 Modo actual")
st.sidebar.success(especialidad)

# ==========================================================
# SESSION STATE
# ==========================================================

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

if "modo" not in st.session_state:
    st.session_state.modo = "chat"

st.sidebar.markdown("---")

if st.sidebar.button("➕ Nueva conversación"):
    st.session_state.mensajes = []
    st.session_state.modo = "chat"
    st.rerun()

st.sidebar.markdown("### 🧰 Herramientas")

if st.sidebar.button("💬 Chat técnico"):
    st.session_state.modo = "chat"

if st.sidebar.button("🧮 Calculadora eléctrica"):
    st.session_state.modo = "calculadora"

if st.sidebar.button("❄️ Calculadora HVAC"):
    st.session_state.modo = "hvac"

if st.sidebar.button("📷 Analizar equipo"):
    st.session_state.modo = "imagen"

if st.sidebar.button("📄 Generar informe"):
    st.session_state.modo = "informe"

st.sidebar.markdown("---")
st.sidebar.caption("NEXTRONIX SMART SYSTEMS S.A.C.")

if client is None:
    st.sidebar.warning("IA sin conexión")
else:
    st.sidebar.success("IA conectada")

# ==========================================================
# INICIO
# ==========================================================

if st.session_state.modo == "chat" and len(st.session_state.mensajes) == 0:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
<div class="nex-card">
<h3>⚡ Electricidad</h3>
<p>Ley de Ohm, corriente, potencia, protecciones, cables, caída de tensión y diagnóstico.</p>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div class="nex-card">
<h3>🏭 Automatización</h3>
<p>PLC, HMI, SCADA, sensores, relés, contactores, motores y control industrial.</p>
</div>
""", unsafe_allow_html=True)

    with col3:
        st.markdown("""
<div class="nex-card">
<h3>❄️ HVAC</h3>
<p>Refrigeración, compresores, presiones, diagnóstico y mantenimiento.</p>
</div>
""", unsafe_allow_html=True)

# ==========================================================
# CALCULADORA ELÉCTRICA
# ==========================================================

if st.session_state.modo == "calculadora":
    st.markdown("## 🧮 Calculadora eléctrica")

    tipo = st.selectbox(
        "Selecciona el cálculo",
        [
            "Ley de Ohm - Voltaje",
            "Ley de Ohm - Corriente",
            "Ley de Ohm - Resistencia",
            "Potencia DC",
            "Potencia monofásica",
            "Potencia trifásica"
        ]
    )

    if tipo == "Ley de Ohm - Voltaje":
        corriente = st.number_input("Corriente (A)", min_value=0.0, value=10.0)
        resistencia = st.number_input("Resistencia (Ω)", min_value=0.0, value=10.0)

        if st.button("Calcular"):
            voltaje = corriente * resistencia
            st.success(f"Voltaje = {voltaje:.2f} V")

    elif tipo == "Ley de Ohm - Corriente":
        voltaje = st.number_input("Voltaje (V)", min_value=0.0, value=220.0)
        resistencia = st.number_input("Resistencia (Ω)", min_value=0.1, value=22.0)

        if st.button("Calcular"):
            corriente = voltaje / resistencia
            st.success(f"Corriente = {corriente:.2f} A")

    elif tipo == "Ley de Ohm - Resistencia":
        voltaje = st.number_input("Voltaje (V)", min_value=0.0, value=220.0)
        corriente = st.number_input("Corriente (A)", min_value=0.1, value=10.0)

        if st.button("Calcular"):
            resistencia = voltaje / corriente
            st.success(f"Resistencia = {resistencia:.2f} Ω")

    elif tipo == "Potencia DC":
        voltaje = st.number_input("Voltaje (V)", min_value=0.0, value=24.0)
        corriente = st.number_input("Corriente (A)", min_value=0.0, value=5.0)

        if st.button("Calcular"):
            potencia = voltaje * corriente
            st.success(f"Potencia = {potencia:.2f} W")

    elif tipo == "Potencia monofásica":
        voltaje = st.number_input("Voltaje (V)", min_value=0.0, value=220.0)
        corriente = st.number_input("Corriente (A)", min_value=0.0, value=10.0)
        fp = st.number_input("Factor de potencia", min_value=0.0, max_value=1.0, value=0.90)

        if st.button("Calcular"):
            potencia = voltaje * corriente * fp
            st.success(f"Potencia activa = {potencia:.2f} W")

    elif tipo == "Potencia trifásica":
        voltaje = st.number_input("Voltaje línea-línea (V)", min_value=0.0, value=380.0)
        corriente = st.number_input("Corriente (A)", min_value=0.0, value=10.0)
        fp = st.number_input("Factor de potencia", min_value=0.0, max_value=1.0, value=0.90)

        if st.button("Calcular"):
            potencia = 1.732 * voltaje * corriente * fp
            st.success(f"Potencia activa trifásica = {potencia:.2f} W")

# ==========================================================
# HVAC
# ==========================================================

elif st.session_state.modo == "hvac":
    st.markdown("## ❄️ Calculadora / Diagnóstico HVAC")

    refrigerante = st.selectbox("Refrigerante", ["R410A", "R32", "R134a", "R404A", "Otro"])
    succion = st.number_input("Presión de succión (psi)", value=0.0)
    descarga = st.number_input("Presión de descarga (psi)", value=0.0)
    temp_ambiente = st.number_input("Temperatura ambiente (°C)", value=25.0)

    st.info("Este módulo irá creciendo para incluir sobrecalentamiento, subenfriamiento y diagnóstico.")

    if st.button("Analizar valores"):
        st.write("### Datos ingresados")
        st.write(f"Refrigerante: {refrigerante}")
        st.write(f"Succión: {succion:.1f} psi")
        st.write(f"Descarga: {descarga:.1f} psi")
        st.write(f"Temperatura ambiente: {temp_ambiente:.1f} °C")
        st.warning("La interpretación exacta requiere conocer modelo del equipo, temperatura interior, carga térmica y condiciones de operación.")

# ==========================================================
# IMAGEN
# ==========================================================

elif st.session_state.modo == "imagen":
    st.markdown("## 📷 Analizar equipo")

    archivo = st.file_uploader("Sube una fotografía", type=["jpg", "jpeg", "png"])

    if archivo:
        st.image(archivo, caption="Imagen cargada", use_container_width=True)
        st.info("La carga de imágenes ya funciona. La interpretación con IA se activará cuando conectemos un modelo con visión.")

# ==========================================================
# INFORME
# ==========================================================

elif st.session_state.modo == "informe":
    st.markdown("## 📄 Generador de informes")

    titulo = st.text_input("Título del informe")
    equipo = st.text_input("Equipo / TAG")
    descripcion = st.text_area("Descripción del trabajo")
    observaciones = st.text_area("Observaciones")

    if st.button("Preparar informe"):
        st.success("Información registrada.")
        st.markdown("### Vista previa")
        st.write(f"**Título:** {titulo}")
        st.write(f"**Equipo / TAG:** {equipo}")
        st.write(f"**Descripción:** {descripcion}")
        st.write(f"**Observaciones:** {observaciones}")

# ==========================================================
# CHAT
# ==========================================================

elif st.session_state.modo == "chat":
    for mensaje in st.session_state.mensajes:
        avatar = "👷" if mensaje["role"] == "user" else "🤖"
        with st.chat_message(mensaje["role"], avatar=avatar):
            st.markdown(mensaje["content"])

    instrucciones = f"""
Tu nombre es Ing. Elvis Bot.
Representas a NEXTRONIX SMART SYSTEMS S.A.C.

Eres un asistente técnico de ingeniería especializado en:
- Electricidad residencial.
- Electricidad industrial.
- Electrónica.
- Automatización industrial.
- PLC.
- HMI.
- SCADA.
- Motores eléctricos.
- Variadores de frecuencia.
- Instrumentación.
- HVAC y refrigeración.
- Mantenimiento industrial.
- Inteligencia artificial.

Especialidad seleccionada:
{especialidad}

Responde siempre en español.
Explica paso a paso.
No inventes mediciones.
"""

    pregunta = st.chat_input("💬 Escribe tu consulta técnica...")

    if pregunta:
        st.session_state.mensajes.append({"role": "user", "content": pregunta})

        with st.chat_message("user", avatar="👷"):
            st.markdown(pregunta)

        if client is None:
            with st.chat_message("assistant", avatar="🤖"):
                st.warning("Ing. Elvis Bot está funcionando, pero todavía no hay conexión disponible con la IA.")
        else:
            try:
                with st.chat_message("assistant", avatar="🤖"):
                    with st.spinner("⚙️ Ing. Elvis Bot está analizando..."):
                        response = client.responses.create(
                            model="gpt-5.6-luna",
                            instructions=instrucciones,
                            input=pregunta
                        )
                        texto = response.output_text
                        st.markdown(texto)

                st.session_state.mensajes.append({"role": "assistant", "content": texto})

            except Exception as error:
                error_texto = str(error)
                st.error("❌ No fue posible obtener una respuesta de la IA.")

                if "429" in error_texto:
                    st.warning("La API Key está siendo reconocida, pero no tienes créditos disponibles.")
                elif "401" in error_texto:
                    st.warning("La API Key no es válida o no está siendo reconocida.")
                else:
                    st.code(error_texto)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("""
<div class="footer">
<strong>⚡ NEXTRONIX SMART SYSTEMS S.A.C.</strong>
<br><br>
Electricidad • Electrónica • Automatización • HVAC • Inteligencia Artificial
<br>
<strong>Ing. Elvis Bot</strong>
<br>
Asistente Técnico Inteligente
</div>
""", unsafe_allow_html=True)