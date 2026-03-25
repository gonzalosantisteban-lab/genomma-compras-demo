import streamlit as st
import time
import pandas as pd

st.set_page_config(
    page_title="Agente de Compras — Genomma Lab",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── ESTILOS ───────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background-color: #0a0f1e;
    color: #e2e8f0;
}

[data-testid="stSidebar"] {
    background-color: #0f172a;
    border-right: 1px solid #1e293b;
}

[data-testid="stSidebar"] [data-testid="stMarkdown"] p {
    color: #94a3b8;
}

.main-header {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 50%, #0f172a 100%);
    border: 1px solid #1e40af;
    border-radius: 16px;
    padding: 32px 40px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}

.main-header::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at 70% 50%, rgba(59,130,246,0.08) 0%, transparent 60%);
}

.main-header h1 {
    font-size: 32px;
    font-weight: 700;
    color: #f1f5f9;
    margin: 0 0 8px 0;
}

.main-header p {
    color: #94a3b8;
    font-size: 16px;
    margin: 0;
}

.area-card {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 16px;
    transition: border-color 0.2s;
}

.area-card:hover {
    border-color: #3b82f6;
}

.area-card h3 {
    color: #f1f5f9;
    font-size: 16px;
    font-weight: 600;
    margin: 0 0 8px 0;
}

.area-card p {
    color: #64748b;
    font-size: 13px;
    margin: 0;
    line-height: 1.5;
}

.area-icon {
    font-size: 28px;
    margin-bottom: 12px;
}

.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #f1f5f9;
    margin-bottom: 4px;
}

.section-sub {
    font-size: 14px;
    color: #64748b;
    margin-bottom: 24px;
}

.flow-box {
    background: #0f172a;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 14px 20px;
    text-align: center;
    color: #e2e8f0;
    font-size: 14px;
    font-weight: 500;
}

.flow-arrow {
    text-align: center;
    color: #3b82f6;
    font-size: 20px;
    padding: 4px 0;
}

.cotizacion-card {
    background: #0f172a;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 20px;
}

.cotizacion-card h4 {
    color: #94a3b8;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin: 0 0 4px 0;
}

.cotizacion-card .valor {
    color: #f1f5f9;
    font-size: 15px;
    font-weight: 500;
}

.thinking-line {
    background: #0a0f1e;
    border: 1px solid #1e293b;
    border-radius: 6px;
    padding: 10px 14px;
    font-family: 'Courier New', monospace;
    font-size: 13px;
    color: #64748b;
    margin: 4px 0;
}

.thinking-line.active {
    border-color: #3b82f6;
    color: #93c5fd;
}

.thinking-line.done {
    border-color: #166534;
    color: #4ade80;
}

.result-rojo {
    background: #1a0505;
    border: 2px solid #dc2626;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 16px;
}

.result-amarillo {
    background: #1a0d00;
    border: 2px solid #d97706;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 16px;
}

.result-verde {
    background: #010f05;
    border: 2px solid #16a34a;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 16px;
}

.badge-rojo {
    display: inline-block;
    background: #dc2626;
    color: white;
    padding: 6px 18px;
    border-radius: 20px;
    font-weight: 700;
    font-size: 20px;
    letter-spacing: 1px;
}

.badge-amarillo {
    display: inline-block;
    background: #d97706;
    color: white;
    padding: 6px 18px;
    border-radius: 20px;
    font-weight: 700;
    font-size: 20px;
    letter-spacing: 1px;
}

.badge-verde {
    display: inline-block;
    background: #16a34a;
    color: white;
    padding: 6px 18px;
    border-radius: 20px;
    font-weight: 700;
    font-size: 20px;
    letter-spacing: 1px;
}

.desviacion-rojo {
    color: #f87171;
    font-size: 28px;
    font-weight: 700;
}

.desviacion-amarillo {
    color: #fbbf24;
    font-size: 28px;
    font-weight: 700;
}

.precio-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid #1e293b;
}

.precio-label {
    color: #94a3b8;
    font-size: 14px;
}

.precio-valor {
    color: #f1f5f9;
    font-size: 15px;
    font-weight: 600;
}

.precio-cotizado {
    color: #f87171;
    font-size: 22px;
    font-weight: 700;
}

.precio-should {
    color: #4ade80;
    font-size: 22px;
    font-weight: 700;
}

.arg-box {
    background: #0c1a2e;
    border: 1px solid #1e40af;
    border-radius: 10px;
    padding: 20px;
    font-size: 14px;
    line-height: 1.7;
    color: #bfdbfe;
    margin-top: 8px;
}

.obs-box {
    background: #0f1a0f;
    border: 1px solid #166534;
    border-radius: 10px;
    padding: 16px 20px;
    font-size: 14px;
    line-height: 1.6;
    color: #86efac;
    margin-top: 8px;
}

.ahorro-box {
    background: linear-gradient(135deg, #052e16, #0a3d20);
    border: 1px solid #16a34a;
    border-radius: 12px;
    padding: 20px 24px;
    text-align: center;
    margin-top: 12px;
}

.ahorro-label {
    color: #4ade80;
    font-size: 13px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.ahorro-valor {
    color: #f1f5f9;
    font-size: 32px;
    font-weight: 800;
    margin: 4px 0;
}

.breakdown-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    margin-top: 8px;
}

.breakdown-table th {
    text-align: left;
    color: #64748b;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 8px 12px;
    border-bottom: 1px solid #1e293b;
}

.breakdown-table td {
    padding: 9px 12px;
    color: #e2e8f0;
    border-bottom: 1px solid #0f172a;
}

.breakdown-table tr:last-child td {
    border-bottom: 2px solid #3b82f6;
    font-weight: 700;
    color: #4ade80;
    font-size: 15px;
}

.breakdown-table tr:last-child td:last-child {
    color: #4ade80;
}

.stat-mini {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 8px;
    padding: 12px 16px;
    text-align: center;
}

.stat-mini .label {
    color: #64748b;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.stat-mini .value {
    color: #f1f5f9;
    font-size: 20px;
    font-weight: 700;
    margin-top: 2px;
}

.tag {
    display: inline-block;
    background: #1e293b;
    color: #94a3b8;
    padding: 2px 10px;
    border-radius: 12px;
    font-size: 12px;
    margin: 2px 3px;
}

.stButton > button {
    background: linear-gradient(135deg, #1d4ed8, #1e40af);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 14px 0;
    font-size: 15px;
    font-weight: 600;
    width: 100%;
    cursor: pointer;
    letter-spacing: 0.3px;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    transform: translateY(-1px);
    box-shadow: 0 4px 20px rgba(59,130,246,0.3);
}

.stRadio > div {
    gap: 0;
}

.stRadio label {
    color: #94a3b8 !important;
    font-size: 14px;
    padding: 8px 0;
}

.divider {
    border: none;
    border-top: 1px solid #1e293b;
    margin: 24px 0;
}

[data-testid="metric-container"] {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 8px;
    padding: 12px;
}
</style>
""", unsafe_allow_html=True)

# ─── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 8px 0 20px 0;">
        <div style="font-size: 22px; font-weight: 800; color: #f1f5f9; letter-spacing: -0.5px;">⚡ ComprasAI</div>
        <div style="font-size: 12px; color: #475569; margin-top: 2px;">Genomma Lab · Demo v0.1</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    page = st.radio(
        "nav",
        ["Inicio", "Arquitectura", "Demo: Cajilla Flanax", "Demo: Frasco HDPE"],
        label_visibility="collapsed",
        format_func=lambda x: {
            "Inicio": "  Inicio",
            "Arquitectura": "  Arquitectura del Sistema",
            "Demo: Cajilla Flanax": "  Demo 1 — Cajilla",
            "Demo: Frasco HDPE": "  Demo 2 — Frasco HDPE",
        }[x]
    )

    st.markdown("---")
    st.markdown("""
    <div style="font-size: 12px; color: #475569; line-height: 1.6;">
        <div style="margin-bottom: 8px;"><span style="color: #4ade80;">●</span> Verde — precio justo (±5%)</div>
        <div style="margin-bottom: 8px;"><span style="color: #fbbf24;">●</span> Amarillo — negociar (5–10%)</div>
        <div><span style="color: #f87171;">●</span> Rojo — renegociar (>10%)</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style="font-size: 11px; color: #334155; line-height: 1.5;">
        Modelo: Claude Opus 4.6<br>
        Datos: ICIS · Banxico · RISI<br>
        Base: PostgreSQL + pgvector
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# PAGINA: INICIO
# ═══════════════════════════════════════════════════════════════════════════════
if page == "Inicio":

    st.markdown("""
    <div class="main-header">
        <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 12px;">
            <div style="background: #1d4ed8; border-radius: 12px; width: 48px; height: 48px; display: flex; align-items: center; justify-content: center; font-size: 24px;">⚡</div>
            <div>
                <div style="font-size: 26px; font-weight: 800; color: #f1f5f9; letter-spacing: -0.5px;">Agente de Compras Genomma Lab</div>
                <div style="color: #64748b; font-size: 14px;">Plataforma multi-agente de IA para negociacion con datos duros de mercado</div>
            </div>
        </div>
        <div style="display: flex; gap: 24px; margin-top: 20px; padding-top: 20px; border-top: 1px solid #1e293b;">
            <div><span style="color: #3b82f6; font-weight: 700;">4</span> <span style="color: #64748b; font-size: 13px;">areas de compras</span></div>
            <div><span style="color: #3b82f6; font-weight: 700;">12+</span> <span style="color: #64748b; font-size: 13px;">agentes especializados</span></div>
            <div><span style="color: #3b82f6; font-weight: 700;">Top 0.01%</span> <span style="color: #64748b; font-size: 13px;">expertise por categoria</span></div>
            <div><span style="color: #3b82f6; font-weight: 700;">Tiempo real</span> <span style="color: #64748b; font-size: 13px;">ICIS · Banxico · RISI</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Que hace el sistema</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Cada cotizacion que entra es analizada por un agente experto PhD-level en ese material especifico</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="area-card">
            <div style="font-size: 26px; margin-bottom: 10px;">🧮</div>
            <h3>Should Cost en tiempo real</h3>
            <p>Calcula el precio justo descomponiendo cada material: resina, proceso, molde, logistica, margen. Con precios de mercado de hoy — no del contrato anterior.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="area-card">
            <div style="font-size: 26px; margin-bottom: 10px;">🎯</div>
            <h3>Verde / Amarillo / Rojo</h3>
            <p>Cada cotizacion recibe un semaforo automatico comparando precio cotizado vs. should cost calculado + historial Genomma + compras publicas IMSS.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="area-card">
            <div style="font-size: 26px; margin-bottom: 10px;">💬</div>
            <h3>Argumentos de negociacion</h3>
            <p>El agente genera el texto listo para usar con el proveedor. Datos duros: precio ICIS de la semana, tipo de cambio Banxico, caida del feedstock.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">Areas cubiertas</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Cuatro gerentes de area, cada uno con sub-agentes expertos en su categoria</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="area-card" style="border-color: #1e40af;">
            <div style="font-size: 28px; margin-bottom: 12px;">📦</div>
            <h3 style="color: #93c5fd;">Empaque</h3>
            <p>Cajillas · Etiquetas · Botellas PET · Botes HDPE · Tapas · Corrugados · Vidrio · Tubos · Valvulas</p>
            <div style="margin-top: 12px; font-size: 12px; color: #1d4ed8; font-weight: 600;">9 agentes expertos</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="area-card" style="border-color: #166534;">
            <div style="font-size: 28px; margin-bottom: 12px;">🧪</div>
            <h3 style="color: #86efac;">Materias Primas</h3>
            <p>APIs farmaceuticos · Excipientes · Saborizantes · Solventes · Activos cosmeticos</p>
            <div style="margin-top: 12px; font-size: 12px; color: #16a34a; font-weight: 600;">5 agentes expertos</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="area-card" style="border-color: #7c3aed;">
            <div style="font-size: 28px; margin-bottom: 12px;">🏭</div>
            <h3 style="color: #c4b5fd;">Maquiladores</h3>
            <p>Maquila farmaceutica · Maquila cosmetica · Toll manufacturing · Semi-toll</p>
            <div style="margin-top: 12px; font-size: 12px; color: #7c3aed; font-weight: 600;">4 agentes expertos</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="area-card" style="border-color: #c2410c;">
            <div style="font-size: 28px; margin-bottom: 12px;">🛠️</div>
            <h3 style="color: #fdba74;">Indirectos</h3>
            <p>POP · Tecnologia · Mantenimiento de plantas · Servicios generales</p>
            <div style="margin-top: 12px; font-size: 12px; color: #ea580c; font-weight: 600;">4 agentes expertos</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">Impacto del proyecto</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Dos problemas que resuelve de raiz</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="area-card" style="border-color: #1e40af; padding: 28px;">
            <div style="font-size: 24px; margin-bottom: 12px;">📉</div>
            <h3 style="color: #93c5fd; font-size: 18px;">Ahorro economico recurrente</h3>
            <p style="font-size: 14px; line-height: 1.7;">El equipo de compras negocia con datos duros de mercado en tiempo real, no con intuicion. Cada punto porcentual recuperado en el precio de materiales tiene impacto directo en margen de Genomma a escala de millones de pesos anuales.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="area-card" style="border-color: #7c3aed; padding: 28px;">
            <div style="font-size: 24px; margin-bottom: 12px;">🔍</div>
            <h3 style="color: #c4b5fd; font-size: 18px;">Eliminacion estructural de corrupcion</h3>
            <p style="font-size: 14px; line-height: 1.7;">La asimetria de informacion entre el proveedor y el comprador es la raiz de la corrupcion en compras. Cuando el comprador tiene los mismos datos que el proveedor —o mas— la negociacion es transparente por diseno.</p>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGINA: ARQUITECTURA
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "Arquitectura":

    st.markdown("""
    <div class="main-header">
        <div style="font-size: 24px; font-weight: 800; color: #f1f5f9;">Arquitectura del Sistema</div>
        <div style="color: #64748b; font-size: 14px; margin-top: 4px;">Como fluye una cotizacion a traves de los agentes</div>
    </div>
    """, unsafe_allow_html=True)

    # Flujo principal
    st.markdown('<div class="section-title">Flujo de evaluacion</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Desde que el comprador sube la cotizacion hasta el argumento de negociacion</div>', unsafe_allow_html=True)

    col1, col_arr, col2, col_arr2, col3, col_arr3, col4, col_arr4, col5 = st.columns([3, 0.5, 3, 0.5, 3, 0.5, 3, 0.5, 3])

    with col1:
        st.markdown("""
        <div class="flow-box" style="border-color: #3b82f6; background: #0c1a2e;">
            <div style="font-size: 20px; margin-bottom: 6px;">📄</div>
            <div style="font-weight: 600; color: #93c5fd;">Comprador</div>
            <div style="font-size: 12px; color: #64748b; margin-top: 4px;">Sube cotizacion del proveedor</div>
        </div>
        """, unsafe_allow_html=True)
    with col_arr:
        st.markdown("<div style='text-align:center; color:#3b82f6; font-size:22px; padding-top:28px;'>→</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="flow-box" style="border-color: #7c3aed; background: #150d2e;">
            <div style="font-size: 20px; margin-bottom: 6px;">🧠</div>
            <div style="font-weight: 600; color: #c4b5fd;">Orquestador</div>
            <div style="font-size: 12px; color: #64748b; margin-top: 4px;">Identifica area y enruta</div>
        </div>
        """, unsafe_allow_html=True)
    with col_arr2:
        st.markdown("<div style='text-align:center; color:#3b82f6; font-size:22px; padding-top:28px;'>→</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="flow-box" style="border-color: #1e40af; background: #0c1a2e;">
            <div style="font-size: 20px; margin-bottom: 6px;">👔</div>
            <div style="font-weight: 600; color: #93c5fd;">Gerente de Area</div>
            <div style="font-size: 12px; color: #64748b; margin-top: 4px;">Lanza sub-agentes en paralelo</div>
        </div>
        """, unsafe_allow_html=True)
    with col_arr3:
        st.markdown("<div style='text-align:center; color:#3b82f6; font-size:22px; padding-top:28px;'>→</div>", unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="flow-box" style="border-color: #166534; background: #010f05;">
            <div style="font-size: 20px; margin-bottom: 6px;">🔬</div>
            <div style="font-weight: 600; color: #86efac;">Experto PhD</div>
            <div style="font-size: 12px; color: #64748b; margin-top: 4px;">Calcula should cost + benchmark</div>
        </div>
        """, unsafe_allow_html=True)
    with col_arr4:
        st.markdown("<div style='text-align:center; color:#3b82f6; font-size:22px; padding-top:28px;'>→</div>", unsafe_allow_html=True)
    with col5:
        st.markdown("""
        <div class="flow-box" style="border-color: #ea580c; background: #1a0800;">
            <div style="font-size: 20px; margin-bottom: 6px;">⚡</div>
            <div style="font-weight: 600; color: #fdba74;">Resultado</div>
            <div style="font-size: 12px; color: #64748b; margin-top: 4px;">Semaforo + argumento listo</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 32px'></div>", unsafe_allow_html=True)

    # Jerarquia de agentes
    st.markdown('<div class="section-title">Jerarquia de agentes</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">El sistema escala horizontalmente — multiples cotizaciones evaluadas en paralelo simultaneamente</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div style="background: #0c1a2e; border: 1px solid #1e40af; border-radius: 12px; padding: 20px; margin-bottom: 16px;">
            <div style="text-align: center; background: #1d4ed8; border-radius: 8px; padding: 10px; margin-bottom: 16px;">
                <div style="font-size: 14px; font-weight: 700; color: #f1f5f9;">GERENTE EMPAQUE</div>
            </div>
            <div style="font-size: 12px; color: #64748b; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">9 Sub-agentes</div>
            <div style="display: flex; flex-direction: column; gap: 6px;">
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">📦 Cajillas</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">🏷️ Etiquetas</div>
                <div style="background: #0f1a0f; border: 1px solid #166534; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #86efac; font-weight: 500;">🧴 Botes HDPE ← PILOTO</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">🍶 Botellas PET</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">🔩 Tapas</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">📫 Corrugados</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">🍾 Vidrio</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">💧 Valvulas</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">🔧 Tubos</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background: #010f05; border: 1px solid #166534; border-radius: 12px; padding: 20px; margin-bottom: 16px;">
            <div style="text-align: center; background: #166534; border-radius: 8px; padding: 10px; margin-bottom: 16px;">
                <div style="font-size: 14px; font-weight: 700; color: #f1f5f9;">GERENTE MAT. PRIMAS</div>
            </div>
            <div style="font-size: 12px; color: #64748b; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">5 Sub-agentes</div>
            <div style="display: flex; flex-direction: column; gap: 6px;">
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">💊 APIs farmaceuticos</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">⚗️ Excipientes</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">🍋 Saborizantes</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">🧫 Solventes</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">✨ Activos cosmeticos</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="background: #150d2e; border: 1px solid #7c3aed; border-radius: 12px; padding: 20px; margin-bottom: 16px;">
            <div style="text-align: center; background: #6d28d9; border-radius: 8px; padding: 10px; margin-bottom: 16px;">
                <div style="font-size: 14px; font-weight: 700; color: #f1f5f9;">GERENTE MAQUILADORES</div>
            </div>
            <div style="font-size: 12px; color: #64748b; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">4 Sub-agentes</div>
            <div style="display: flex; flex-direction: column; gap: 6px;">
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">💉 Maquila farmaceutica</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">💄 Maquila cosmetica</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">🔄 Toll manufacturing</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">🔀 Semi-toll</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style="background: #1a0800; border: 1px solid #c2410c; border-radius: 12px; padding: 20px; margin-bottom: 16px;">
            <div style="text-align: center; background: #c2410c; border-radius: 8px; padding: 10px; margin-bottom: 16px;">
                <div style="font-size: 14px; font-weight: 700; color: #f1f5f9;">GERENTE INDIRECTOS</div>
            </div>
            <div style="font-size: 12px; color: #64748b; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">4 Sub-agentes</div>
            <div style="display: flex; flex-direction: column; gap: 6px;">
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">🎯 POP & Publicidad</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">💻 Tecnologia</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">⚙️ Mantenimiento</div>
                <div style="background: #0f172a; border: 1px solid #334155; border-radius: 6px; padding: 8px 10px; font-size: 13px; color: #e2e8f0;">🏢 Servicios generales</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 16px'></div>", unsafe_allow_html=True)

    # Fuentes de datos
    st.markdown('<div class="section-title">Fuentes de datos en tiempo real</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">El agente no opera con supuestos — opera con precios de mercado de hoy</div>', unsafe_allow_html=True)

    fuentes = [
        ("ICIS Americas", "Precios de resinas plasticas (HDPE, PET, PP) — fuente global de la industria petroquimica", "Semanal", "#3b82f6"),
        ("Fastmarkets RISI", "Precios de papel y carton por tonelada (SBS, FBB, CRB) — referencia global", "Semanal", "#3b82f6"),
        ("Banxico API", "Tipo de cambio MXN/USD en tiempo real — todos los calculos se ajustan automaticamente", "Diaria", "#16a34a"),
        ("Perplexity API", "Noticias de mercado, movimientos de commodities, novedades de proveedores con citas verificables", "Tiempo real", "#7c3aed"),
        ("CompraNet / IMSS", "Precios de compras publicas del gobierno — benchmark independiente para farmaceutico", "Mensual", "#d97706"),
        ("Base Genomma (SAP)", "Historial de precios pagados, contratos vigentes, especificaciones tecnicas por codigo SAP", "Continuo", "#64748b"),
    ]

    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    for i, (nombre, desc, freq, color) in enumerate(fuentes):
        with cols[i % 3]:
            st.markdown(f"""
            <div style="background: #0f172a; border: 1px solid #1e293b; border-radius: 10px; padding: 16px; margin-bottom: 12px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div style="font-size: 14px; font-weight: 600; color: #f1f5f9;">{nombre}</div>
                    <div style="font-size: 11px; background: #1e293b; color: {color}; padding: 2px 8px; border-radius: 10px; white-space: nowrap;">{freq}</div>
                </div>
                <div style="font-size: 13px; color: #64748b; margin-top: 6px; line-height: 1.5;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGINA: DEMO CAJILLA
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "Demo: Cajilla Flanax":

    st.markdown("""
    <div class="main-header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div style="font-size: 11px; color: #475569; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px;">AREA: EMPAQUE · AGENTE EXPERTO EN CAJILLAS</div>
                <div style="font-size: 24px; font-weight: 800; color: #f1f5f9;">Cajilla Flanax 500mg 20 Tabletas</div>
                <div style="color: #64748b; font-size: 14px; margin-top: 4px;">Grupo Cartonero del Bajio · Cotizacion 24 marzo 2026</div>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 11px; color: #475569; margin-bottom: 4px;">SAP</div>
                <div style="font-size: 18px; font-weight: 700; color: #93c5fd; font-family: monospace;">1000234-M</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_izq, col_der = st.columns([1, 1.2])

    with col_izq:
        st.markdown('<div style="font-size: 16px; font-weight: 700; color: #f1f5f9; margin-bottom: 16px;">Cotizacion recibida</div>', unsafe_allow_html=True)

        specs = [
            ("Material", "Cajilla plegadiza farmaceutica"),
            ("Sustrato", "SBS 350 g/m² · Calibre 12 pt"),
            ("Area desarrollada", "452 cm²"),
            ("Impresion", "4 Pantones + barniz UV full"),
            ("Acabados", "Hot stamping dorado en logo"),
            ("Proceso", "Troquel Bobst + folder-gluer"),
            ("Volumen cotizado", "150,000 piezas"),
            ("Precio cotizado", "$1.85 MXN / pieza"),
            ("Total cotizacion", "$277,500 MXN"),
            ("Dias de credito", "60 dias"),
            ("Proveedor", "Grupo Cartonero del Bajio"),
        ]

        for label, valor in specs:
            color_val = "#f87171" if "cotizado" in label.lower() or "Total" in label else "#e2e8f0"
            size_val = "16px" if "cotizado" in label.lower() else "14px"
            weight = "700" if "cotizado" in label.lower() else "500"
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; padding: 9px 0; border-bottom: 1px solid #0f172a;">
                <span style="color: #64748b; font-size: 13px;">{label}</span>
                <span style="color: {color_val}; font-size: {size_val}; font-weight: {weight};">{valor}</span>
            </div>
            """, unsafe_allow_html=True)

    with col_der:
        st.markdown('<div style="font-size: 16px; font-weight: 700; color: #f1f5f9; margin-bottom: 16px;">Analizar con agente experto</div>', unsafe_allow_html=True)

        if "cajilla_analizado" not in st.session_state:
            st.session_state.cajilla_analizado = False

        if not st.session_state.cajilla_analizado:
            st.markdown("""
            <div style="background: #0f172a; border: 1px solid #1e293b; border-radius: 10px; padding: 20px; margin-bottom: 20px;">
                <div style="font-size: 13px; color: #64748b; line-height: 1.7;">
                    El agente experto en Cajillas tiene conocimiento PhD-level en ciencia del papel, procesos de conversion y mercados globales de cartulina. Va a:
                    <br><br>
                    • Consultar precio SBS hoy en RISI via Perplexity<br>
                    • Calcular should cost con tipo de cambio Banxico actual<br>
                    • Comparar contra historial de Genomma<br>
                    • Evaluar si el hot stamping esta bien costeado<br>
                    • Generar argumento de negociacion con datos duros
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Analizar cotizacion", key="btn_cajilla"):
                steps = [
                    ("Consultando codigo SAP 1000234-M en base de datos Genomma...", 0.8),
                    ("Obteniendo precio cartulina SBS via Fastmarkets RISI...", 1.0),
                    ("Verificando tipo de cambio MXN/USD · Banxico API...", 0.7),
                    ("Calculando costo de material (452 cm² · 350 g/m²)...", 0.8),
                    ("Evaluando costo de impresion: 4 Pantones + barniz UV...", 0.7),
                    ("Auditando costo de hot stamping vs benchmark industria...", 0.9),
                    ("Calculando costo de conversion (troquel + pegado Bobst)...", 0.7),
                    ("Comparando contra historial de precios Genomma...", 0.8),
                    ("Consultando compras publicas IMSS para SKU equivalente...", 0.9),
                    ("Generando argumento de negociacion...", 1.0),
                ]

                placeholder = st.empty()
                completed = []

                for step_text, duration in steps:
                    completed.append(step_text)
                    with placeholder.container():
                        for prev in completed[:-1]:
                            st.markdown(f"""
                            <div class="thinking-line done">
                                ✓ {prev}
                            </div>
                            """, unsafe_allow_html=True)
                        st.markdown(f"""
                        <div class="thinking-line active">
                            ⟳ {completed[-1]}
                        </div>
                        """, unsafe_allow_html=True)
                    time.sleep(duration)

                st.session_state.cajilla_analizado = True
                st.rerun()

        if st.session_state.cajilla_analizado:

            st.markdown("""
            <div class="result-rojo">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                    <span class="badge-rojo">🔴 ROJO</span>
                    <div style="text-align: right;">
                        <div style="color: #94a3b8; font-size: 12px;">Desviacion sobre should cost</div>
                        <div class="desviacion-rojo">+42.3%</div>
                    </div>
                </div>
                <div style="display: flex; gap: 16px; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 120px;">
                        <div style="color: #94a3b8; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;">Precio cotizado</div>
                        <div class="precio-cotizado">$1.85</div>
                        <div style="color: #475569; font-size: 11px;">MXN / pieza</div>
                    </div>
                    <div style="flex: 1; min-width: 120px;">
                        <div style="color: #94a3b8; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;">Should cost hoy</div>
                        <div class="precio-should">$1.30</div>
                        <div style="color: #475569; font-size: 11px;">MXN / pieza</div>
                    </div>
                    <div style="flex: 1; min-width: 120px;">
                        <div style="color: #94a3b8; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;">Historico Genomma</div>
                        <div style="color: #93c5fd; font-size: 22px; font-weight: 700;">$1.26</div>
                        <div style="color: #475569; font-size: 11px;">Contrato Abr 2024</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Desglose
            st.markdown('<div style="font-size: 15px; font-weight: 700; color: #f1f5f9; margin: 20px 0 10px 0;">Desglose del should cost</div>', unsafe_allow_html=True)

            breakdown = pd.DataFrame({
                "Componente": [
                    "Material SBS (452 cm² · 350 g/m² · desperdicio 18%)",
                    "Impresion offset (4 Pantones, placas amortizadas)",
                    "Barniz UV full",
                    "Hot stamping dorado (troquel especial)",
                    "Conversion (troquel + pegado Bobst)",
                    "Logistica a planta Genomma",
                    "Margen fabricante (25%)",
                    "SHOULD COST TOTAL",
                ],
                "MXN / pieza": ["$0.31", "$0.19", "$0.09", "$0.12", "$0.27", "$0.06", "$0.26", "$1.30"],
                "% del total": ["24%", "15%", "7%", "9%", "21%", "5%", "20%", "100%"],
            })

            st.dataframe(
                breakdown,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Componente": st.column_config.TextColumn("Componente", width="large"),
                    "MXN / pieza": st.column_config.TextColumn("MXN/pieza", width="small"),
                    "% del total": st.column_config.TextColumn("% total", width="small"),
                }
            )

            # Alertas
            st.markdown('<div style="font-size: 15px; font-weight: 700; color: #f1f5f9; margin: 20px 0 10px 0;">Observaciones del agente</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="obs-box">
                ⬇ <strong>Papel SBS bajo 8.3% en los ultimos 60 dias</strong> segun Fastmarkets RISI (Americas index). La cotizacion no refleja esta reduccion.<br><br>
                💱 <strong>Tipo de cambio actual: $17.19 MXN/USD</strong> vs $18.10 en el contrato anterior de Abr 2024. El proveedor se beneficio de la depreciacion pasada pero no lo transfiere ahora que el peso se fortalecio.<br><br>
                🔍 <strong>Hot stamping sobrecosteado:</strong> El agente detecta $0.12/pieza para hot stamping dorado en un tiraje de 150,000 pzas. El benchmark de industria para este acabado en ese volumen es $0.07-0.09/pieza. Diferencia: $0.03-0.05/pieza adicional.<br><br>
                📋 <strong>Referencia IMSS CompraNet:</strong> Cajilla farmaceutica SBS 4 colores comparable en licitacion reciente: $1.19-1.31 MXN/pieza.
            </div>
            """, unsafe_allow_html=True)

            # Argumento
            st.markdown('<div style="font-size: 15px; font-weight: 700; color: #f1f5f9; margin: 20px 0 10px 0;">Argumento de negociacion — listo para usar</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="arg-box">
                "Gracias por su cotizacion. Hemos realizado nuestro analisis de costos y tenemos algunas observaciones.<br><br>
                El precio de cartulina SBS ha bajado 8.3% en las ultimas 8 semanas segun el indice Fastmarkets RISI Americas, pasando de ~$940 a ~$862 USD/tonelada. Adicionalmente, el tipo de cambio actual es de $17.19 MXN/USD, significativamente por debajo del nivel del ano pasado.<br><br>
                Nuestro calculo de should cost para este material —considerando sustrato, impresion, barniz UV, hot stamping, conversion y margen razonable de fabricante— arroja <strong>$1.30 MXN/pieza</strong>. El precio de referencia en nuestro ultimo contrato fue de $1.26 MXN/pieza en condiciones de mercado menos favorables para nosotros.<br><br>
                Solicitamos revisar su cotizacion al rango de <strong>$1.28 – $1.35 MXN/pieza</strong> para los 150,000 piezas. Estamos abiertos a discutir condiciones de pago a 30 dias si eso ayuda a llegar al precio objetivo."
            </div>
            """, unsafe_allow_html=True)

            # Ahorro
            st.markdown("""
            <div class="ahorro-box">
                <div class="ahorro-label">Ahorro potencial en esta orden</div>
                <div class="ahorro-valor">$82,500 MXN</div>
                <div style="color: #4ade80; font-size: 13px; opacity: 0.8;">($1.85 − $1.30) × 150,000 piezas</div>
                <div style="color: #64748b; font-size: 12px; margin-top: 8px;">Precio objetivo: $1.28 – $1.35 MXN/pieza</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Nueva consulta", key="btn_cajilla_reset"):
                st.session_state.cajilla_analizado = False
                st.rerun()


# ═══════════════════════════════════════════════════════════════════════════════
# PAGINA: DEMO FRASCO HDPE
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "Demo: Frasco HDPE":

    st.markdown("""
    <div class="main-header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div style="font-size: 11px; color: #475569; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px;">AREA: EMPAQUE · AGENTE EXPERTO EN BOTES Y FRASCOS PLASTICO</div>
                <div style="font-size: 24px; font-weight: 800; color: #f1f5f9;">Frasco HDPE 120ml — Cicatricure Gel</div>
                <div style="color: #64748b; font-size: 14px; margin-top: 4px;">Envases Plasticos del Norte · Cotizacion 24 marzo 2026</div>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 11px; color: #475569; margin-bottom: 4px;">SAP</div>
                <div style="font-size: 18px; font-weight: 700; color: #93c5fd; font-family: monospace;">2001089-B</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_izq, col_der = st.columns([1, 1.2])

    with col_izq:
        st.markdown('<div style="font-size: 16px; font-weight: 700; color: #f1f5f9; margin-bottom: 16px;">Cotizacion recibida</div>', unsafe_allow_html=True)

        specs = [
            ("Material", "Frasco rigido plastico 120ml"),
            ("Resina", "HDPE virgen"),
            ("Gramaje", "22 gramos"),
            ("Color", "Blanco (masterbatch 2%)"),
            ("Rosca", "38mm estandar"),
            ("Proceso", "Extrusion-soplado"),
            ("Molde", "2 cavidades (propiedad del proveedor)"),
            ("Certificacion", "USP Class VI"),
            ("Volumen cotizado", "80,000 piezas"),
            ("Precio cotizado", "$4.20 MXN / pieza"),
            ("Total cotizacion", "$336,000 MXN"),
            ("Dias de credito", "45 dias"),
            ("Proveedor", "Envases Plasticos del Norte"),
        ]

        for label, valor in specs:
            color_val = "#fbbf24" if "cotizado" in label.lower() or "Total" in label else "#e2e8f0"
            size_val = "16px" if "cotizado" in label.lower() else "14px"
            weight = "700" if "cotizado" in label.lower() else "500"
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; padding: 9px 0; border-bottom: 1px solid #0f172a;">
                <span style="color: #64748b; font-size: 13px;">{label}</span>
                <span style="color: {color_val}; font-size: {size_val}; font-weight: {weight};">{valor}</span>
            </div>
            """, unsafe_allow_html=True)

    with col_der:
        st.markdown('<div style="font-size: 16px; font-weight: 700; color: #f1f5f9; margin-bottom: 16px;">Analizar con agente experto</div>', unsafe_allow_html=True)

        if "hdpe_analizado" not in st.session_state:
            st.session_state.hdpe_analizado = False

        if not st.session_state.hdpe_analizado:
            st.markdown("""
            <div style="background: #0f172a; border: 1px solid #1e293b; border-radius: 10px; padding: 20px; margin-bottom: 20px;">
                <div style="font-size: 13px; color: #64748b; line-height: 1.7;">
                    El agente experto en Botes y Frascos tiene conocimiento PhD-level en ciencia de polimeros, procesos de soplado y mercados globales de resinas. Va a:
                    <br><br>
                    • Calcular should cost con precio HDPE Americas (ICIS) de hoy<br>
                    • Auditar el costo de transformacion vs benchmark por region<br>
                    • Verificar si el molde ya esta amortizado por el proveedor<br>
                    • Evaluar el gramaje vs benchmark industria (oportunidad light-weighting)<br>
                    • Revisar si el HDPE esta bajando en mercado y cotizacion lo refleja
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Analizar cotizacion", key="btn_hdpe"):
                steps = [
                    ("Consultando codigo SAP 2001089-B en base de datos Genomma...", 0.8),
                    ("Obteniendo precio HDPE Americas via ICIS · Perplexity API...", 1.1),
                    ("Verificando tipo de cambio MXN/USD · Banxico API...", 0.6),
                    ("Calculando costo de resina: 22g HDPE virgen + merma 3%...", 0.8),
                    ("Evaluando costo transformacion extrusion-soplado 2 cavidades...", 0.9),
                    ("Auditando amortizacion del molde: ciclos producidos vs vida util...", 1.0),
                    ("Comparando gramaje 22g vs benchmark industria para 120ml HDPE...", 0.8),
                    ("Calculando certificacion USP Class VI por pieza...", 0.7),
                    ("Comparando contra historial de precios Genomma SAP...", 0.8),
                    ("Detectando movimientos de feedstock etileno/etano...", 0.9),
                    ("Generando argumento de negociacion con datos ICIS...", 1.0),
                ]

                placeholder = st.empty()
                completed = []

                for step_text, duration in steps:
                    completed.append(step_text)
                    with placeholder.container():
                        for prev in completed[:-1]:
                            st.markdown(f"""
                            <div class="thinking-line done">
                                ✓ {prev}
                            </div>
                            """, unsafe_allow_html=True)
                        st.markdown(f"""
                        <div class="thinking-line active">
                            ⟳ {completed[-1]}
                        </div>
                        """, unsafe_allow_html=True)
                    time.sleep(duration)

                st.session_state.hdpe_analizado = True
                st.rerun()

        if st.session_state.hdpe_analizado:

            st.markdown("""
            <div class="result-amarillo">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                    <span class="badge-amarillo">🟡 AMARILLO</span>
                    <div style="text-align: right;">
                        <div style="color: #94a3b8; font-size: 12px;">Desviacion sobre should cost</div>
                        <div class="desviacion-amarillo">+12.9%</div>
                    </div>
                </div>
                <div style="display: flex; gap: 16px; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 120px;">
                        <div style="color: #94a3b8; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;">Precio cotizado</div>
                        <div style="color: #fbbf24; font-size: 22px; font-weight: 700;">$4.20</div>
                        <div style="color: #475569; font-size: 11px;">MXN / pieza</div>
                    </div>
                    <div style="flex: 1; min-width: 120px;">
                        <div style="color: #94a3b8; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;">Should cost hoy</div>
                        <div class="precio-should">$3.72</div>
                        <div style="color: #475569; font-size: 11px;">MXN / pieza</div>
                    </div>
                    <div style="flex: 1; min-width: 120px;">
                        <div style="color: #94a3b8; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;">Historico Genomma</div>
                        <div style="color: #93c5fd; font-size: 22px; font-weight: 700;">$3.91</div>
                        <div style="color: #475569; font-size: 11px;">Contrato Jul 2024</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Desglose
            st.markdown('<div style="font-size: 15px; font-weight: 700; color: #f1f5f9; margin: 20px 0 10px 0;">Desglose del should cost</div>', unsafe_allow_html=True)

            breakdown = pd.DataFrame({
                "Componente": [
                    "Resina HDPE virgen  (22g · merma 3% · HDPE $20.83/kg ICIS hoy)",
                    "Masterbatch blanco (22g · dosif. 2% · $82/kg)",
                    "Transformacion extrusion-soplado (benchmark region Monterrey)",
                    "Molde amortizado (2 cav. · $240k MXN · vida util 800k ciclos)",
                    "Certificacion USP Class VI + COA por lote",
                    "Logistica a planta Genomma",
                    "Margen fabricante (18%)",
                    "SHOULD COST TOTAL",
                ],
                "MXN / pieza": ["$0.47", "$0.04", "$2.27", "$0.15", "$0.15", "$0.09", "$0.55", "$3.72"],
                "% del total": ["13%", "1%", "61%", "4%", "4%", "2%", "15%", "100%"],
            })

            st.dataframe(
                breakdown,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Componente": st.column_config.TextColumn("Componente", width="large"),
                    "MXN / pieza": st.column_config.TextColumn("MXN/pieza", width="small"),
                    "% del total": st.column_config.TextColumn("% total", width="small"),
                }
            )

            # Alertas
            st.markdown('<div style="font-size: 15px; font-weight: 700; color: #f1f5f9; margin: 20px 0 10px 0;">Observaciones del agente</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="obs-box">
                ⬇ <strong>HDPE Americas bajo 3.2% en las ultimas 4 semanas</strong> segun ICIS (de $1.21 a $1.17 USD/kg). La cotizacion no refleja esta reduccion reciente.<br><br>
                ⚖️ <strong>Oportunidad de light-weighting:</strong> El gramaje declarado es 22g para una botella de 120ml en HDPE. El benchmark de industria para este volumen es 18-20g. Con un rediseno de pared, Genomma podria reducir 2-4g por pieza sin comprometer resistencia (top load). Ahorro adicional potencial: $0.04-0.08 MXN/pieza sobre el should cost ya negociado.<br><br>
                🔧 <strong>Molde casi al limite de vida util:</strong> El proveedor tiene 850,000 ciclos producidos sobre una vida util estimada de 800,000. El molde ya esta amortizado. El proveedor no deberia incluir cargo de amortizacion de molde en el precio — o si lo hace, es para el molde de reemplazo, lo cual debe negociarse explicitamente.<br><br>
                📉 <strong>Precio historico Genomma $3.91</strong> (Jul 2024) con HDPE mas caro que hoy. La cotizacion actual a $4.20 representa un incremento injustificado dado el movimiento del mercado.
            </div>
            """, unsafe_allow_html=True)

            # Argumento
            st.markdown('<div style="font-size: 15px; font-weight: 700; color: #f1f5f9; margin: 20px 0 10px 0;">Argumento de negociacion — listo para usar</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="arg-box">
                "Gracias por su cotizacion del frasco HDPE 120ml para Cicatricure. Hemos realizado nuestro analisis y queremos compartir algunas observaciones antes de tomar una decision.<br><br>
                El precio de HDPE Americas segun ICIS ha bajado 3.2% en las ultimas cuatro semanas, cerrando hoy en $1.17 USD/kg. Nuestro ultimo contrato con ustedes fue a $3.91 MXN/pieza en julio 2024, cuando el HDPE cotizaba mas caro y el tipo de cambio era diferente. La cotizacion actual de $4.20 representa un incremento que no esta alineado con la direccion del mercado.<br><br>
                Nuestro analisis de should cost —resina, colorante, transformacion, molde, certificacion USP y logistica— arroja <strong>$3.72 MXN/pieza</strong> con margen razonable de 18%.<br><br>
                Adicionalmente, notamos que el molde tiene 850,000 ciclos producidos. Si el molde esta praxticamente amortizado, solicitamos que se refleje en el precio. Si anticipan necesidad de molde nuevo, hagamos esa conversion por separado.<br><br>
                Nuestro precio objetivo es <strong>$3.72 – $3.85 MXN/pieza</strong>. Podemos hablar tambien de condiciones de pago a 30 dias o consolidacion de volumen trimestral para llegar ahi."
            </div>
            """, unsafe_allow_html=True)

            # Ahorro
            st.markdown("""
            <div class="ahorro-box">
                <div class="ahorro-label">Ahorro potencial en esta orden</div>
                <div class="ahorro-valor">$38,400 MXN</div>
                <div style="color: #4ade80; font-size: 13px; opacity: 0.8;">($4.20 − $3.72) × 80,000 piezas</div>
                <div style="color: #64748b; font-size: 12px; margin-top: 8px;">Precio objetivo: $3.72 – $3.85 MXN/pieza · + oportunidad light-weighting $6,400 adicionales</div>
            </div>
            """, unsafe_allow_html=True)

            # Bonus: oportunidad adicional
            st.markdown("""
            <div style="background: #0c1a2e; border: 1px solid #1e40af; border-radius: 10px; padding: 16px; margin-top: 16px;">
                <div style="font-size: 13px; font-weight: 600; color: #93c5fd; margin-bottom: 8px;">Oportunidad adicional detectada</div>
                <div style="font-size: 13px; color: #94a3b8; line-height: 1.6;">
                    El agente recomienda iniciar un proyecto de <strong>light-weighting</strong>: reducir gramaje de 22g a 19g para la botella de 120ml. Los grandes fabricadores como Graham Packaging y Plastipak han logrado reducciones de 12-18% de gramaje en HDPE farmaceutico manteniendo top load y USP Class VI. Ahorro estimado adicional: <strong>$0.06/pieza</strong> en produccion recurrente.
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Nueva consulta", key="btn_hdpe_reset"):
                st.session_state.hdpe_analizado = False
                st.rerun()
