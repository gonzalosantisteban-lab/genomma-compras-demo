import streamlit as st
import time
import pandas as pd

st.set_page_config(
    page_title="AI Procurement Cerebro — Genomma Lab",
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
    background-color: #f8fafc;
    color: #0f172a;
}

[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e2e8f0;
}

[data-testid="stSidebar"] [data-testid="stMarkdown"] p {
    color: #64748b;
}

.main-header {
    background: linear-gradient(135deg, #1e3a5f 0%, #1d4ed8 50%, #1e3a5f 100%);
    border-radius: 14px;
    padding: 24px 32px;
    margin-bottom: 24px;
}

.main-header h1 {
    font-size: 24px;
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 4px 0;
}

.main-header p {
    color: #bfdbfe;
    font-size: 14px;
    margin: 0;
}

.area-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 12px;
}

.area-card h3 {
    color: #0f172a;
    font-size: 15px;
    font-weight: 600;
    margin: 0 0 6px 0;
}

.area-card p {
    color: #64748b;
    font-size: 13px;
    margin: 0;
    line-height: 1.5;
}

.section-title {
    font-size: 18px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 2px;
}

.section-sub {
    font-size: 13px;
    color: #64748b;
    margin-bottom: 20px;
}

.flow-box {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 14px 16px;
    text-align: center;
    color: #0f172a;
    font-size: 13px;
    font-weight: 500;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}

.thinking-line {
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 8px 12px;
    font-family: 'Courier New', monospace;
    font-size: 12px;
    color: #64748b;
    margin: 3px 0;
}

.thinking-line.active {
    border-color: #3b82f6;
    background: #eff6ff;
    color: #1d4ed8;
}

.thinking-line.done {
    border-color: #86efac;
    background: #f0fdf4;
    color: #16a34a;
}

.result-rojo {
    background: #fff1f2;
    border: 2px solid #f43f5e;
    border-radius: 10px;
    padding: 16px 20px;
    margin-bottom: 12px;
}

.result-amarillo {
    background: #fffbeb;
    border: 2px solid #f59e0b;
    border-radius: 10px;
    padding: 16px 20px;
    margin-bottom: 12px;
}

.result-verde {
    background: #f0fdf4;
    border: 2px solid #22c55e;
    border-radius: 10px;
    padding: 16px 20px;
    margin-bottom: 12px;
}

.badge-rojo {
    display: inline-block;
    background: #f43f5e;
    color: white;
    padding: 4px 14px;
    border-radius: 20px;
    font-weight: 700;
    font-size: 16px;
}

.badge-amarillo {
    display: inline-block;
    background: #f59e0b;
    color: white;
    padding: 4px 14px;
    border-radius: 20px;
    font-weight: 700;
    font-size: 16px;
}

.desviacion-rojo {
    color: #f43f5e;
    font-size: 26px;
    font-weight: 800;
}

.desviacion-amarillo {
    color: #f59e0b;
    font-size: 26px;
    font-weight: 800;
}

.precio-cotizado {
    color: #f43f5e;
    font-size: 26px;
    font-weight: 800;
}

.precio-amarillo {
    color: #f59e0b;
    font-size: 26px;
    font-weight: 800;
}

.precio-should {
    color: #16a34a;
    font-size: 26px;
    font-weight: 800;
}

.precio-hist {
    color: #1d4ed8;
    font-size: 22px;
    font-weight: 700;
}

.arg-box {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-radius: 10px;
    padding: 16px 20px;
    font-size: 13px;
    line-height: 1.7;
    color: #1e3a5f;
}

.obs-box {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-radius: 10px;
    padding: 14px 18px;
    font-size: 13px;
    line-height: 1.6;
    color: #14532d;
}

.ahorro-box {
    background: linear-gradient(135deg, #166534, #15803d);
    border-radius: 10px;
    padding: 16px 20px;
    text-align: center;
}

.ahorro-label {
    color: #bbf7d0;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.ahorro-valor {
    color: #ffffff;
    font-size: 28px;
    font-weight: 800;
    margin: 2px 0;
}

.spec-row {
    display: flex;
    justify-content: space-between;
    padding: 7px 0;
    border-bottom: 1px solid #f1f5f9;
    font-size: 13px;
}

.spec-label { color: #94a3b8; }
.spec-val { color: #0f172a; font-weight: 500; }
.spec-val-highlight { color: #f43f5e; font-weight: 700; font-size: 15px; }
.spec-val-highlight-amber { color: #f59e0b; font-weight: 700; font-size: 15px; }

.divider { border: none; border-top: 1px solid #e2e8f0; margin: 20px 0; }

.stButton > button {
    background: linear-gradient(135deg, #1d4ed8, #2563eb);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 0;
    font-size: 14px;
    font-weight: 600;
    width: 100%;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #1e40af, #1d4ed8);
}

.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: #f1f5f9;
    border-radius: 8px;
    padding: 4px;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 6px;
    color: #64748b;
    font-size: 13px;
    font-weight: 500;
}

.stTabs [aria-selected="true"] {
    background: #ffffff !important;
    color: #0f172a !important;
}

/* Sidebar radio menu — texto visible */
[data-testid="stSidebar"] .stRadio label {
    color: #1e293b !important;
    font-size: 14px !important;
    font-weight: 500 !important;
}

[data-testid="stSidebar"] .stRadio label:hover {
    color: #1d4ed8 !important;
}

[data-testid="stSidebar"] .stRadio [aria-checked="true"] + div label,
[data-testid="stSidebar"] .stRadio [data-checked="true"] label {
    color: #1d4ed8 !important;
    font-weight: 600 !important;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] div {
    color: #334155;
}
</style>
""", unsafe_allow_html=True)

# ─── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 8px 0 20px 0;">
        <div style="font-size: 18px; font-weight: 800; color: #0f172a; letter-spacing: -0.5px;">⚡ AI PROCUREMENT CEREBRO</div>
        <div style="font-size: 12px; color: #94a3b8; margin-top: 2px;">Genomma Lab · Demo v0.1</div>
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
    <div style="font-size: 12px; color: #94a3b8; line-height: 1.8;">
        <div><span style="color: #22c55e; font-weight: 700;">●</span> Verde — precio justo (±5%)</div>
        <div><span style="color: #f59e0b; font-weight: 700;">●</span> Amarillo — negociar (5–10%)</div>
        <div><span style="color: #f43f5e; font-weight: 700;">●</span> Rojo — renegociar (>10%)</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style="font-size: 11px; color: #cbd5e1; line-height: 1.6;">
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
        <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 10px;">
            <div style="background: rgba(255,255,255,0.15); border-radius: 10px; width: 44px; height: 44px; display: flex; align-items: center; justify-content: center; font-size: 22px;">⚡</div>
            <div>
                <div style="font-size: 22px; font-weight: 800; color: #fff;">AI Procurement Cerebro</div>
                <div style="color: #bfdbfe; font-size: 13px;">Plataforma multi-agente de IA para negociacion con datos duros de mercado</div>
            </div>
        </div>
        <div style="display: flex; gap: 28px; margin-top: 16px; padding-top: 16px; border-top: 1px solid rgba(255,255,255,0.15);">
            <div><span style="color: #fff; font-weight: 700;">4</span> <span style="color: #bfdbfe; font-size: 12px;">areas de compras</span></div>
            <div><span style="color: #fff; font-weight: 700;">12+</span> <span style="color: #bfdbfe; font-size: 12px;">agentes especializados</span></div>
            <div><span style="color: #fff; font-weight: 700;">Top 0.01%</span> <span style="color: #bfdbfe; font-size: 12px;">expertise por categoria</span></div>
            <div><span style="color: #fff; font-weight: 700;">Tiempo real</span> <span style="color: #bfdbfe; font-size: 12px;">ICIS · Banxico · RISI</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Que hace el sistema</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Cada cotizacion es analizada por un agente experto PhD-level en ese material especifico</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="area-card" style="border-top: 3px solid #3b82f6;">
            <div style="font-size: 24px; margin-bottom: 8px;">🧮</div>
            <h3>Should Cost en tiempo real</h3>
            <p>Descompone cada material: resina, proceso, molde, logistica, margen. Con precios de mercado de hoy — no del contrato anterior.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="area-card" style="border-top: 3px solid #22c55e;">
            <div style="font-size: 24px; margin-bottom: 8px;">🎯</div>
            <h3>Verde / Amarillo / Rojo</h3>
            <p>Semaforo automatico comparando precio cotizado vs. should cost + historial Genomma + compras publicas IMSS.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="area-card" style="border-top: 3px solid #f59e0b;">
            <div style="font-size: 24px; margin-bottom: 8px;">💬</div>
            <h3>Argumentos de negociacion</h3>
            <p>Genera el texto listo para usar con el proveedor. Datos duros: ICIS de la semana, tipo de cambio Banxico, caida del feedstock.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">Areas cubiertas</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Cuatro gerentes de area, cada uno con sub-agentes expertos en su categoria</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="area-card" style="border-top: 3px solid #3b82f6;">
            <div style="font-size: 26px; margin-bottom: 10px;">📦</div>
            <h3 style="color: #1d4ed8;">Empaque</h3>
            <p>Cajillas · Etiquetas · Botellas PET · Botes HDPE · Tapas · Corrugados · Vidrio · Tubos · Valvulas</p>
            <div style="margin-top: 10px; font-size: 12px; color: #3b82f6; font-weight: 600;">9 agentes expertos</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="area-card" style="border-top: 3px solid #22c55e;">
            <div style="font-size: 26px; margin-bottom: 10px;">🧪</div>
            <h3 style="color: #16a34a;">Materias Primas</h3>
            <p>APIs farmaceuticos · Excipientes · Saborizantes · Solventes · Activos cosmeticos</p>
            <div style="margin-top: 10px; font-size: 12px; color: #16a34a; font-weight: 600;">5 agentes expertos</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="area-card" style="border-top: 3px solid #a855f7;">
            <div style="font-size: 26px; margin-bottom: 10px;">🏭</div>
            <h3 style="color: #7c3aed;">Maquiladores</h3>
            <p>Maquila farmaceutica · Maquila cosmetica · Toll manufacturing · Semi-toll</p>
            <div style="margin-top: 10px; font-size: 12px; color: #7c3aed; font-weight: 600;">4 agentes expertos</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="area-card" style="border-top: 3px solid #f97316;">
            <div style="font-size: 26px; margin-bottom: 10px;">🛠️</div>
            <h3 style="color: #ea580c;">Indirectos</h3>
            <p>POP · Tecnologia · Mantenimiento de plantas · Servicios generales</p>
            <div style="margin-top: 10px; font-size: 12px; color: #ea580c; font-weight: 600;">4 agentes expertos</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="area-card" style="border-top: 3px solid #3b82f6; padding: 24px;">
            <div style="font-size: 22px; margin-bottom: 10px;">📉</div>
            <h3 style="font-size: 16px; color: #1d4ed8;">Ahorro economico recurrente</h3>
            <p style="font-size: 13px; line-height: 1.7;">El equipo negocia con datos duros de mercado en tiempo real. Cada punto porcentual recuperado tiene impacto directo en margen a escala de millones de pesos anuales.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="area-card" style="border-top: 3px solid #a855f7; padding: 24px;">
            <div style="font-size: 22px; margin-bottom: 10px;">🔍</div>
            <h3 style="font-size: 16px; color: #7c3aed;">Eliminacion estructural de corrupcion</h3>
            <p style="font-size: 13px; line-height: 1.7;">Cuando el comprador tiene los mismos datos que el proveedor —o mas— la negociacion es transparente por diseno. La asimetria de informacion es la raiz del problema.</p>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGINA: ARQUITECTURA
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "Arquitectura":

    st.markdown("""
    <div class="main-header">
        <div style="font-size: 22px; font-weight: 800; color: #fff;">Arquitectura del Sistema</div>
        <div style="color: #bfdbfe; font-size: 13px; margin-top: 4px;">Como fluye una cotizacion a traves de los agentes</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Flujo de evaluacion</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Desde que el comprador sube la cotizacion hasta el argumento de negociacion</div>', unsafe_allow_html=True)

    col1, ca, col2, cb, col3, cc, col4, cd, col5 = st.columns([3, 0.4, 3, 0.4, 3, 0.4, 3, 0.4, 3])

    boxes = [
        (col1, "📄", "Comprador", "Sube cotizacion del proveedor", "#3b82f6"),
        (col2, "🧠", "Orquestador", "Identifica area y enruta", "#7c3aed"),
        (col3, "👔", "Gerente de Area", "Lanza sub-agentes en paralelo", "#1d4ed8"),
        (col4, "🔬", "Experto PhD", "Calcula should cost + benchmark", "#16a34a"),
        (col5, "⚡", "Resultado", "Semaforo + argumento listo", "#ea580c"),
    ]
    arrows = [ca, cb, cc, cd]

    for col, icon, title, desc, color in boxes:
        with col:
            st.markdown(f"""
            <div class="flow-box" style="border-top: 3px solid {color};">
                <div style="font-size: 18px; margin-bottom: 6px;">{icon}</div>
                <div style="font-weight: 600; color: {color}; font-size: 13px;">{title}</div>
                <div style="font-size: 11px; color: #64748b; margin-top: 4px;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    for col in arrows:
        with col:
            st.markdown("<div style='text-align:center; color:#94a3b8; font-size:20px; padding-top:26px;'>→</div>", unsafe_allow_html=True)

    st.markdown("<div style='height: 24px'></div>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">Jerarquia de agentes</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">El sistema evalua multiples cotizaciones en paralelo simultaneamente</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    areas = [
        (col1, "#3b82f6", "#dbeafe", "GERENTE EMPAQUE", "9 Sub-agentes", [
            ("📦", "Cajillas"), ("🏷️", "Etiquetas"), ("🧴", "Botes HDPE ← PILOTO"),
            ("🍶", "Botellas PET"), ("🔩", "Tapas"), ("📫", "Corrugados"),
            ("🍾", "Vidrio"), ("💧", "Valvulas"), ("🔧", "Tubos"),
        ]),
        (col2, "#16a34a", "#dcfce7", "GERENTE MAT. PRIMAS", "5 Sub-agentes", [
            ("💊", "APIs farmaceuticos"), ("⚗️", "Excipientes"),
            ("🍋", "Saborizantes"), ("🧫", "Solventes"), ("✨", "Activos cosmeticos"),
        ]),
        (col3, "#7c3aed", "#ede9fe", "GERENTE MAQUILADORES", "4 Sub-agentes", [
            ("💉", "Maquila farmaceutica"), ("💄", "Maquila cosmetica"),
            ("🔄", "Toll manufacturing"), ("🔀", "Semi-toll"),
        ]),
        (col4, "#ea580c", "#ffedd5", "GERENTE INDIRECTOS", "4 Sub-agentes", [
            ("🎯", "POP & Publicidad"), ("💻", "Tecnologia"),
            ("⚙️", "Mantenimiento"), ("🏢", "Servicios generales"),
        ]),
    ]

    for col, color, bg, title, subtitle, agents in areas:
        with col:
            agents_html = "".join([
                f'<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 7px 10px; font-size: 12px; color: #0f172a; margin-bottom: 5px;">{icon} {name}</div>'
                for icon, name in agents
            ])
            st.markdown(f"""
            <div style="background: {bg}; border: 1px solid {color}30; border-radius: 10px; padding: 16px;">
                <div style="text-align: center; background: {color}; border-radius: 6px; padding: 8px; margin-bottom: 12px;">
                    <div style="font-size: 12px; font-weight: 700; color: #fff;">{title}</div>
                </div>
                <div style="font-size: 11px; color: {color}; font-weight: 600; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">{subtitle}</div>
                {agents_html}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height: 16px'></div>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">Fuentes de datos en tiempo real</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">El agente opera con precios de mercado de hoy, no con supuestos</div>', unsafe_allow_html=True)

    fuentes = [
        ("ICIS Americas", "Precios de resinas plasticas (HDPE, PET, PP)", "Semanal", "#3b82f6"),
        ("Fastmarkets RISI", "Precios de papel y carton (SBS, FBB, CRB)", "Semanal", "#3b82f6"),
        ("Banxico API", "Tipo de cambio MXN/USD en tiempo real", "Diaria", "#16a34a"),
        ("Perplexity API", "Noticias de mercado y commodities con citas verificables", "Tiempo real", "#7c3aed"),
        ("CompraNet / IMSS", "Precios de compras publicas — benchmark independiente", "Mensual", "#f59e0b"),
        ("Base Genomma (SAP)", "Historial de precios, contratos y specs por codigo SAP", "Continuo", "#64748b"),
    ]

    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    for i, (nombre, desc, freq, color) in enumerate(fuentes):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="area-card">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div style="font-size: 13px; font-weight: 600; color: #0f172a;">{nombre}</div>
                    <div style="font-size: 11px; background: #f1f5f9; color: {color}; padding: 2px 8px; border-radius: 10px; white-space: nowrap; font-weight: 600;">{freq}</div>
                </div>
                <div style="font-size: 12px; color: #64748b; margin-top: 5px;">{desc}</div>
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
                <div style="font-size: 11px; color: #bfdbfe; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px;">EMPAQUE · AGENTE EXPERTO EN CAJILLAS</div>
                <div style="font-size: 20px; font-weight: 800; color: #fff;">Cajilla Flanax 500mg 20 Tabletas</div>
                <div style="color: #bfdbfe; font-size: 13px; margin-top: 2px;">Grupo Cartonero del Bajio · 24 marzo 2026</div>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 11px; color: #bfdbfe;">SAP</div>
                <div style="font-size: 16px; font-weight: 700; color: #fff; font-family: monospace;">1000234-M</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if "cajilla_analizado" not in st.session_state:
        st.session_state.cajilla_analizado = False

    tab1, tab2, tab3 = st.tabs(["  Cotizacion recibida  ", "  Analisis del agente  ", "  Argumento y ahorro  "])

    with tab1:
        # Fila de precios destacados
        pc1, pc2, pc3, pc4 = st.columns(4)
        with pc1:
            st.markdown("""
            <div style="background:#fff1f2;border:1.5px solid #fecdd3;border-radius:10px;padding:16px 18px;">
                <div style="font-size:11px;color:#94a3b8;text-transform:uppercase;letter-spacing:1px;font-weight:600;">Precio cotizado</div>
                <div style="font-size:28px;font-weight:800;color:#f43f5e;margin:4px 0;">$1.85</div>
                <div style="font-size:12px;color:#64748b;">MXN / pieza</div>
            </div>""", unsafe_allow_html=True)
        with pc2:
            st.markdown("""
            <div style="background:#f0fdf4;border:1.5px solid #bbf7d0;border-radius:10px;padding:16px 18px;">
                <div style="font-size:11px;color:#94a3b8;text-transform:uppercase;letter-spacing:1px;font-weight:600;">Total cotizacion</div>
                <div style="font-size:28px;font-weight:800;color:#16a34a;margin:4px 0;">$277,500</div>
                <div style="font-size:12px;color:#64748b;">MXN · 150,000 pzas</div>
            </div>""", unsafe_allow_html=True)
        with pc3:
            st.markdown("""
            <div style="background:#f8fafc;border:1.5px solid #e2e8f0;border-radius:10px;padding:16px 18px;">
                <div style="font-size:11px;color:#94a3b8;text-transform:uppercase;letter-spacing:1px;font-weight:600;">Proveedor</div>
                <div style="font-size:15px;font-weight:700;color:#0f172a;margin:6px 0;">Grupo Cartonero del Bajio</div>
                <div style="font-size:12px;color:#64748b;">60 dias de credito</div>
            </div>""", unsafe_allow_html=True)
        with pc4:
            st.markdown("""
            <div style="background:#f8fafc;border:1.5px solid #e2e8f0;border-radius:10px;padding:16px 18px;">
                <div style="font-size:11px;color:#94a3b8;text-transform:uppercase;letter-spacing:1px;font-weight:600;">Fecha</div>
                <div style="font-size:15px;font-weight:700;color:#0f172a;margin:6px 0;">24 marzo 2026</div>
                <div style="font-size:12px;color:#64748b;">SAP: 1000234-M</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

        # Grid de especificaciones
        g1, g2, g3 = st.columns(3)
        specs_grid = [
            (g1, "Material", "Cajilla plegadiza farmaceutica", "📦"),
            (g2, "Sustrato", "SBS 350 g/m² · Calibre 12 pt", "📋"),
            (g3, "Area desarrollada", "452 cm²", "📐"),
            (g1, "Impresion", "4 Pantones + barniz UV full", "🎨"),
            (g2, "Acabados", "Hot stamping dorado en logo", "✨"),
            (g3, "Proceso", "Troquel Bobst + folder-gluer", "⚙️"),
        ]
        for col, label, valor, icon in specs_grid:
            with col:
                st.markdown(f"""
                <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;padding:12px 14px;margin-bottom:10px;">
                    <div style="font-size:11px;color:#94a3b8;text-transform:uppercase;letter-spacing:0.5px;font-weight:600;margin-bottom:4px;">{icon} {label}</div>
                    <div style="font-size:14px;font-weight:600;color:#0f172a;">{valor}</div>
                </div>""", unsafe_allow_html=True)

    with tab2:
        if not st.session_state.cajilla_analizado:
            st.markdown("""
            <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px 18px; margin-bottom: 16px; font-size: 13px; color: #1e3a5f; line-height: 1.7;">
                El agente consultara RISI para precio SBS · Banxico para tipo de cambio · historial Genomma · benchmark hot stamping · referencia IMSS CompraNet
            </div>
            """, unsafe_allow_html=True)

            if st.button("Analizar cotizacion", key="btn_cajilla"):
                steps = [
                    ("Consultando codigo SAP 1000234-M en base Genomma...", 0.7),
                    ("Obteniendo precio cartulina SBS · Fastmarkets RISI...", 0.9),
                    ("Verificando tipo de cambio MXN/USD · Banxico API...", 0.6),
                    ("Calculando costo material (452 cm² · 350 g/m²)...", 0.7),
                    ("Evaluando impresion: 4 Pantones + barniz UV...", 0.7),
                    ("Auditando hot stamping vs benchmark industria...", 0.8),
                    ("Calculando conversion (troquel + pegado Bobst)...", 0.6),
                    ("Comparando historial precios Genomma...", 0.7),
                    ("Consultando IMSS CompraNet SKU equivalente...", 0.8),
                    ("Generando argumento de negociacion...", 0.9),
                ]
                placeholder = st.empty()
                completed = []
                for step_text, duration in steps:
                    completed.append(step_text)
                    with placeholder.container():
                        for prev in completed[:-1]:
                            st.markdown(f'<div class="thinking-line done">✓ {prev}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div class="thinking-line active">⟳ {completed[-1]}</div>', unsafe_allow_html=True)
                    time.sleep(duration)
                st.session_state.cajilla_analizado = True
                st.rerun()
        else:
            col1, col2 = st.columns([1.1, 1])

            with col1:
                st.markdown("""
                <div class="result-rojo">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
                        <span class="badge-rojo">🔴 ROJO</span>
                        <div style="text-align: right;">
                            <div style="color: #64748b; font-size: 11px;">Desviacion sobre should cost</div>
                            <div class="desviacion-rojo">+42.3%</div>
                        </div>
                    </div>
                    <div style="display: flex; gap: 16px;">
                        <div style="flex: 1;">
                            <div style="color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;">Cotizado</div>
                            <div class="precio-cotizado">$1.85</div>
                            <div style="color: #94a3b8; font-size: 11px;">MXN / pieza</div>
                        </div>
                        <div style="flex: 1;">
                            <div style="color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;">Should cost</div>
                            <div class="precio-should">$1.30</div>
                            <div style="color: #94a3b8; font-size: 11px;">MXN / pieza</div>
                        </div>
                        <div style="flex: 1;">
                            <div style="color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;">Historico</div>
                            <div class="precio-hist">$1.26</div>
                            <div style="color: #94a3b8; font-size: 11px;">Abr 2024</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown('<div style="font-size: 13px; font-weight: 600; color: #0f172a; margin: 12px 0 6px 0;">Desglose should cost</div>', unsafe_allow_html=True)
                breakdown = pd.DataFrame({
                    "Componente": ["Material SBS", "Impresion 4 col", "Barniz UV", "Hot stamping", "Conversion", "Logistica", "Margen 25%", "TOTAL"],
                    "MXN/pza": ["$0.31", "$0.19", "$0.09", "$0.12", "$0.27", "$0.06", "$0.26", "$1.30"],
                })
                st.dataframe(breakdown, use_container_width=True, hide_index=True)

            with col2:
                st.markdown('<div style="font-size: 13px; font-weight: 600; color: #0f172a; margin-bottom: 8px;">Observaciones</div>', unsafe_allow_html=True)
                st.markdown("""
                <div class="obs-box">
                    ⬇ <strong>SBS bajo 8.3%</strong> en 60 dias (Fastmarkets RISI). No reflejado en cotizacion.<br><br>
                    💱 <strong>TC actual $17.19</strong> vs $18.10 en contrato anterior. MXN fortalecido.<br><br>
                    🔍 <strong>Hot stamping sobrecosteado:</strong> $0.12/pza vs benchmark $0.07-0.09 para 150k pzas.<br><br>
                    📋 <strong>IMSS CompraNet:</strong> cajilla comparable $1.19-1.31 MXN/pza en licitacion reciente.
                </div>
                """, unsafe_allow_html=True)

            if st.button("Nueva consulta", key="btn_cajilla_reset"):
                st.session_state.cajilla_analizado = False
                st.rerun()

    with tab3:
        if not st.session_state.cajilla_analizado:
            st.info("Primero ejecuta el analisis en la pestana anterior.")
        else:
            col1, col2 = st.columns([1.6, 1])
            with col1:
                st.markdown('<div style="font-size: 13px; font-weight: 600; color: #0f172a; margin-bottom: 8px;">Argumento de negociacion — listo para usar</div>', unsafe_allow_html=True)
                st.markdown("""
                <div class="arg-box">
                    "Gracias por su cotizacion. Hemos realizado nuestro analisis de costos y tenemos algunas observaciones.<br><br>
                    El precio de cartulina SBS ha bajado 8.3% en las ultimas 8 semanas segun Fastmarkets RISI Americas, de ~$940 a ~$862 USD/ton. El tipo de cambio actual es $17.19 MXN/USD, por debajo del nivel del ano pasado.<br><br>
                    Nuestro should cost para este material — sustrato, impresion, barniz UV, hot stamping, conversion y margen razonable — arroja <strong>$1.30 MXN/pieza</strong>. Nuestro ultimo contrato fue $1.26 en condiciones menos favorables para nosotros.<br><br>
                    Solicitamos revisar al rango de <strong>$1.28 – $1.35 MXN/pieza</strong> para las 150,000 piezas. Podemos discutir pago a 30 dias si ayuda a llegar al precio objetivo."
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown("""
                <div class="ahorro-box">
                    <div class="ahorro-label">Ahorro potencial</div>
                    <div class="ahorro-valor">$82,500 MXN</div>
                    <div style="color: #bbf7d0; font-size: 12px;">($1.85 − $1.30) × 150,000 pzas</div>
                    <div style="color: #86efac; font-size: 11px; margin-top: 8px;">Precio objetivo: $1.28 – $1.35</div>
                </div>
                """, unsafe_allow_html=True)
                st.markdown("""
                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px; margin-top: 12px; font-size: 12px; color: #1e3a5f; line-height: 1.6;">
                    <strong>Precio objetivo:</strong> $1.28 – $1.35 MXN/pieza<br>
                    <strong>Palanca adicional:</strong> Pago a 30 dias<br>
                    <strong>Referencia IMSS:</strong> $1.19 – $1.31 MXN/pieza
                </div>
                """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PAGINA: DEMO FRASCO HDPE
# ═══════════════════════════════════════════════════════════════════════════════
elif page == "Demo: Frasco HDPE":

    st.markdown("""
    <div class="main-header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div style="font-size: 11px; color: #bfdbfe; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px;">EMPAQUE · AGENTE EXPERTO EN BOTES Y FRASCOS PLASTICO</div>
                <div style="font-size: 20px; font-weight: 800; color: #fff;">Frasco HDPE 120ml — Cicatricure Gel</div>
                <div style="color: #bfdbfe; font-size: 13px; margin-top: 2px;">Envases Plasticos del Norte · 24 marzo 2026</div>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 11px; color: #bfdbfe;">SAP</div>
                <div style="font-size: 16px; font-weight: 700; color: #fff; font-family: monospace;">2001089-B</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if "hdpe_analizado" not in st.session_state:
        st.session_state.hdpe_analizado = False

    tab1, tab2, tab3 = st.tabs(["  Cotizacion recibida  ", "  Analisis del agente  ", "  Argumento y ahorro  "])

    with tab1:
        pc1, pc2, pc3, pc4 = st.columns(4)
        with pc1:
            st.markdown("""
            <div style="background:#fffbeb;border:1.5px solid #fde68a;border-radius:10px;padding:16px 18px;">
                <div style="font-size:11px;color:#94a3b8;text-transform:uppercase;letter-spacing:1px;font-weight:600;">Precio cotizado</div>
                <div style="font-size:28px;font-weight:800;color:#f59e0b;margin:4px 0;">$4.20</div>
                <div style="font-size:12px;color:#64748b;">MXN / pieza</div>
            </div>""", unsafe_allow_html=True)
        with pc2:
            st.markdown("""
            <div style="background:#f0fdf4;border:1.5px solid #bbf7d0;border-radius:10px;padding:16px 18px;">
                <div style="font-size:11px;color:#94a3b8;text-transform:uppercase;letter-spacing:1px;font-weight:600;">Total cotizacion</div>
                <div style="font-size:28px;font-weight:800;color:#16a34a;margin:4px 0;">$336,000</div>
                <div style="font-size:12px;color:#64748b;">MXN · 80,000 pzas</div>
            </div>""", unsafe_allow_html=True)
        with pc3:
            st.markdown("""
            <div style="background:#f8fafc;border:1.5px solid #e2e8f0;border-radius:10px;padding:16px 18px;">
                <div style="font-size:11px;color:#94a3b8;text-transform:uppercase;letter-spacing:1px;font-weight:600;">Proveedor</div>
                <div style="font-size:15px;font-weight:700;color:#0f172a;margin:6px 0;">Envases Plasticos del Norte</div>
                <div style="font-size:12px;color:#64748b;">45 dias de credito</div>
            </div>""", unsafe_allow_html=True)
        with pc4:
            st.markdown("""
            <div style="background:#f8fafc;border:1.5px solid #e2e8f0;border-radius:10px;padding:16px 18px;">
                <div style="font-size:11px;color:#94a3b8;text-transform:uppercase;letter-spacing:1px;font-weight:600;">Fecha</div>
                <div style="font-size:15px;font-weight:700;color:#0f172a;margin:6px 0;">24 marzo 2026</div>
                <div style="font-size:12px;color:#64748b;">SAP: 2001089-B</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

        g1, g2, g3 = st.columns(3)
        specs_grid = [
            (g1, "Material", "Frasco rigido plastico 120ml", "🧴"),
            (g2, "Resina", "HDPE virgen", "⚗️"),
            (g3, "Gramaje", "22 gramos", "⚖️"),
            (g1, "Color", "Blanco (masterbatch 2%)", "🎨"),
            (g2, "Proceso", "Extrusion-soplado · 2 cavidades", "⚙️"),
            (g3, "Certificacion", "USP Class VI", "✅"),
        ]
        for col, label, valor, icon in specs_grid:
            with col:
                st.markdown(f"""
                <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;padding:12px 14px;margin-bottom:10px;">
                    <div style="font-size:11px;color:#94a3b8;text-transform:uppercase;letter-spacing:0.5px;font-weight:600;margin-bottom:4px;">{icon} {label}</div>
                    <div style="font-size:14px;font-weight:600;color:#0f172a;">{valor}</div>
                </div>""", unsafe_allow_html=True)

    with tab2:
        if not st.session_state.hdpe_analizado:
            st.markdown("""
            <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px 18px; margin-bottom: 16px; font-size: 13px; color: #1e3a5f; line-height: 1.7;">
                El agente consultara ICIS para precio HDPE Americas · Banxico para TC · auditara amortizacion del molde · evaluara gramaje vs benchmark de industria
            </div>
            """, unsafe_allow_html=True)

            if st.button("Analizar cotizacion", key="btn_hdpe"):
                steps = [
                    ("Consultando codigo SAP 2001089-B en base Genomma...", 0.7),
                    ("Obteniendo precio HDPE Americas · ICIS via Perplexity...", 1.0),
                    ("Verificando tipo de cambio MXN/USD · Banxico API...", 0.6),
                    ("Calculando costo resina: 22g HDPE virgen + merma 3%...", 0.7),
                    ("Evaluando costo transformacion extrusion-soplado 2 cav...", 0.8),
                    ("Auditando amortizacion molde: ciclos producidos vs vida util...", 0.9),
                    ("Comparando gramaje 22g vs benchmark 120ml HDPE...", 0.7),
                    ("Calculando certificacion USP Class VI por pieza...", 0.6),
                    ("Comparando historial precios Genomma SAP...", 0.7),
                    ("Detectando movimientos feedstock etileno/etano...", 0.8),
                    ("Generando argumento de negociacion con datos ICIS...", 0.9),
                ]
                placeholder = st.empty()
                completed = []
                for step_text, duration in steps:
                    completed.append(step_text)
                    with placeholder.container():
                        for prev in completed[:-1]:
                            st.markdown(f'<div class="thinking-line done">✓ {prev}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div class="thinking-line active">⟳ {completed[-1]}</div>', unsafe_allow_html=True)
                    time.sleep(duration)
                st.session_state.hdpe_analizado = True
                st.rerun()
        else:
            col1, col2 = st.columns([1.1, 1])

            with col1:
                st.markdown("""
                <div class="result-amarillo">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
                        <span class="badge-amarillo">🟡 AMARILLO</span>
                        <div style="text-align: right;">
                            <div style="color: #64748b; font-size: 11px;">Desviacion sobre should cost</div>
                            <div class="desviacion-amarillo">+12.9%</div>
                        </div>
                    </div>
                    <div style="display: flex; gap: 16px;">
                        <div style="flex: 1;">
                            <div style="color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;">Cotizado</div>
                            <div class="precio-amarillo">$4.20</div>
                            <div style="color: #94a3b8; font-size: 11px;">MXN / pieza</div>
                        </div>
                        <div style="flex: 1;">
                            <div style="color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;">Should cost</div>
                            <div class="precio-should">$3.72</div>
                            <div style="color: #94a3b8; font-size: 11px;">MXN / pieza</div>
                        </div>
                        <div style="flex: 1;">
                            <div style="color: #64748b; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;">Historico</div>
                            <div class="precio-hist">$3.91</div>
                            <div style="color: #94a3b8; font-size: 11px;">Jul 2024</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown('<div style="font-size: 13px; font-weight: 600; color: #0f172a; margin: 12px 0 6px 0;">Desglose should cost</div>', unsafe_allow_html=True)
                breakdown = pd.DataFrame({
                    "Componente": ["Resina HDPE 22g", "Colorante blanco", "Transformacion", "Molde amortizado", "Calidad USP", "Logistica", "Margen 18%", "TOTAL"],
                    "MXN/pza": ["$0.47", "$0.04", "$2.27", "$0.15", "$0.15", "$0.09", "$0.55", "$3.72"],
                })
                st.dataframe(breakdown, use_container_width=True, hide_index=True)

            with col2:
                st.markdown('<div style="font-size: 13px; font-weight: 600; color: #0f172a; margin-bottom: 8px;">Observaciones</div>', unsafe_allow_html=True)
                st.markdown("""
                <div class="obs-box">
                    ⬇ <strong>HDPE Americas bajo 3.2%</strong> en 4 semanas (ICIS). No reflejado.<br><br>
                    ⚖️ <strong>Light-weighting:</strong> 22g vs benchmark 18-20g para 120ml HDPE. Oportunidad de $0.04-0.08/pza adicional.<br><br>
                    🔧 <strong>Molde casi amortizado:</strong> 850k ciclos producidos sobre vida util de 800k. No debe incluir cargo de amortizacion.<br><br>
                    📉 <strong>Historico $3.91</strong> (Jul 2024) con HDPE mas caro. Incremento injustificado.
                </div>
                """, unsafe_allow_html=True)

            if st.button("Nueva consulta", key="btn_hdpe_reset"):
                st.session_state.hdpe_analizado = False
                st.rerun()

    with tab3:
        if not st.session_state.hdpe_analizado:
            st.info("Primero ejecuta el analisis en la pestana anterior.")
        else:
            col1, col2 = st.columns([1.6, 1])
            with col1:
                st.markdown('<div style="font-size: 13px; font-weight: 600; color: #0f172a; margin-bottom: 8px;">Argumento de negociacion — listo para usar</div>', unsafe_allow_html=True)
                st.markdown("""
                <div class="arg-box">
                    "Gracias por su cotizacion del frasco HDPE 120ml para Cicatricure. Hemos realizado nuestro analisis.<br><br>
                    El precio de HDPE Americas segun ICIS bajo 3.2% en las ultimas cuatro semanas, cerrando en $1.17 USD/kg. Nuestro ultimo contrato fue $3.91 MXN/pieza en julio 2024, cuando el HDPE cotizaba mas caro. La cotizacion actual de $4.20 no refleja la direccion del mercado.<br><br>
                    Nuestro should cost — resina, colorante, transformacion, molde, USP y logistica — arroja <strong>$3.72 MXN/pieza</strong> con margen de 18%.<br><br>
                    Adicionalmente, el molde tiene 850,000 ciclos producidos sobre una vida util de 800,000. Solicitamos que se refleje en el precio.<br><br>
                    Precio objetivo: <strong>$3.72 – $3.85 MXN/pieza</strong>. Podemos discutir pago a 30 dias o consolidacion trimestral."
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown("""
                <div class="ahorro-box">
                    <div class="ahorro-label">Ahorro potencial</div>
                    <div class="ahorro-valor">$38,400 MXN</div>
                    <div style="color: #bbf7d0; font-size: 12px;">($4.20 − $3.72) × 80,000 pzas</div>
                    <div style="color: #86efac; font-size: 11px; margin-top: 8px;">Precio objetivo: $3.72 – $3.85</div>
                </div>
                """, unsafe_allow_html=True)
                st.markdown("""
                <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 14px; margin-top: 12px; font-size: 12px; color: #1e3a5f; line-height: 1.6;">
                    <strong>Oportunidad adicional:</strong><br>
                    Light-weighting 22g → 19g ahorra $0.06/pza adicional en produccion recurrente.
                </div>
                """, unsafe_allow_html=True)
