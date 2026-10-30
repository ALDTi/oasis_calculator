import numpy as np
import streamlit as st

st.set_page_config(page_title="Team Calculator", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@400;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Rajdhani', sans-serif; }
.stApp { background: #0d0f14; color: #c9d1d9; }
h1, h2, h3 {
    font-family: 'Share Tech Mono', monospace !important;
    color: #58a6ff !important;
    letter-spacing: 0.05em;
}
.block-container { padding-top: 2rem; max-width: 780px; }

/* inputs + select */
input[type=number], input[type=text], .stSelectbox > div > div {
    background: #1e2330 !important;
    color: #e6edf3 !important;
    border: 1px solid #3d4558 !important;
    border-radius: 4px !important;
    font-family: 'Share Tech Mono', monospace !important;
}
/* number input wrappers */
.stNumberInput > div {
    background: #1e2330 !important;
    border: 1px solid #3d4558 !important;
    border-radius: 6px !important;
}
/* +/- buttons */
.stNumberInput button {
    background: #2d3447 !important;
    color: #c9d1d9 !important;
    border: none !important;
}
.stNumberInput button:hover {
    background: #3d4a63 !important;
}
/* selectbox */
.stSelectbox > div > div {
    background: #1e2330 !important;
    color: #e6edf3 !important;
}
/* labels */
.stNumberInput label, .stSelectbox label {
    color: #8b949e !important;
    font-size: 0.8rem !important;
}
/* calculate button */
.stButton > button {
    background: #1a2540 !important;
    color: #58a6ff !important;
    border: 1px solid #2d4a7a !important;
    border-radius: 6px !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 1rem !important;
    letter-spacing: 0.08em !important;
    padding: 0.6rem !important;
}
.stButton > button:hover {
    background: #243356 !important;
    border-color: #58a6ff !important;
}

/* result card */
.result-card {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 1.2rem 1.5rem;
    margin-top: 1rem;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.9rem;
}
.result-row {
    display: flex;
    justify-content: space-between;
    padding: 4px 0;
    border-bottom: 1px solid #21262d;
}
.result-row:last-child { border-bottom: none; }
.result-label { color: #8b949e; }
.result-value { color: #e6edf3; font-weight: 600; }
.result-value.green  { color: #3fb950; }
.result-value.red    { color: #f85149; }
.result-value.gold   { color: #d2a679; }
.result-value.blue   { color: #58a6ff; }

.section-title {
    font-family: 'Share Tech Mono', monospace;
    color: #58a6ff;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin: 1rem 0 0.4rem 0;
}
.tribe-badge {
    display: inline-block;
    padding: 3px 12px;
    border-radius: 4px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    margin-bottom: 1rem;
}
.tribe-gaul   { background:#0d4429; color:#3fb950; border:1px solid #238636; }
.tribe-teuton { background:#3d2a00; color:#e3a840; border:1px solid #a67820; }
.unclearable  { color:#f85149; font-family:'Share Tech Mono',monospace; font-size:1rem; padding:1rem 0; }

/* combat table */
.combat-wrap { margin-top: 1.2rem; }
.combat-table {
    width: 100%;
    border-collapse: collapse;
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    overflow: hidden;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.85rem;
    margin-bottom: 1rem;
}
.combat-table th, .combat-table td {
    padding: 6px 10px;
    text-align: center;
    border-bottom: 1px solid #21262d;
    border-right: 1px solid #21262d;
    color: #c9d1d9;
}
.combat-table th:last-child, .combat-table td:last-child { border-right: none; }
.combat-table tr:last-child td { border-bottom: none; }
.combat-table .header-row th {
    background: #1e2330;
    color: #8b949e;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}
.combat-table .label-cell {
    text-align: left;
    color: #8b949e;
    font-size: 0.8rem;
    white-space: nowrap;
    background: #1a1f2b;
}
.combat-table .section-header {
    text-align: left;
    font-weight: 700;
    font-size: 0.78rem;
    letter-spacing: 0.1em;
    padding: 5px 10px;
    border-bottom: 1px solid #30363d;
}
.off-header { color: #f0883e; background: #1e1a14; }
.def-header { color: #3fb950; background: #141e17; }
.zero { color: #3d4558; }
.val  { color: #e6edf3; font-weight: 600; }
.lost { color: #f85149; font-weight: 600; }
.surv { color: #3fb950; font-weight: 600; }

/* summary row */
.summary-card {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 0.9rem 1.2rem;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.85rem;
    display: flex;
    flex-wrap: wrap;
    gap: 1.2rem;
}
.sum-item { display: flex; flex-direction: column; gap: 2px; }
.sum-label { color: #8b949e; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.08em; }
.sum-value { font-size: 1rem; font-weight: 700; }
</style>
""", unsafe_allow_html=True)

# ── constants ─────────────────────────────────────────────────────────────────
ANIMAL_NAMES   = ["Rat","Spider","Serpent","Bat","Boar","Wolf","Bear","Croco","Tiger","Elephant"]
ANIMAL_KEYS    = [n.lower() for n in ANIMAL_NAMES]
ANIMAL_VALUES  = [160,160,160,160,320,320,480,480,480,800]
ANIMAL_INF_DEF = [25,35,40,66,70,80,140,380,170,440]
ANIMAL_CAV_DEF = [20,40,60,50,33,70,200,240,250,520]
SPAWN_RATES    = [5,6,7,8,9,10,11,12,13,14]
ANIMAL_ICONS   = ["🐀","🕷","🐍","🦇","🐗","🐺","🐻","🐊","🐯","🐘"]

# ── combat ────────────────────────────────────────────────────────────────────
def gaul_hp(animals, ntt):
    atk = 100 * ntt
    if atk <= 0: return 1.0
    nature = sum(a*d for a,d in zip(animals, ANIMAL_CAV_DEF)) + 10
    r = 100 * (nature / atk) ** 1.5
    return r / (r + 100)

def teuton_hp(animals, nclub, ntk):
    inf_atk = 40 * nclub
    cav_atk = 150 * ntk
    total   = inf_atk + cav_atk
    if total <= 0: return 1.0
    inf_def = sum(a*d for a,d in zip(animals, ANIMAL_INF_DEF))
    cav_def = sum(a*d for a,d in zip(animals, ANIMAL_CAV_DEF))
    nature  = (inf_def * inf_atk / total) + (cav_def * cav_atk / total) + 10
    r = 100 * (nature / total) ** 1.5
    return r / (r + 100)

def res_gained(animals, hp): return sum(round(c*(1-hp))*v for c,v in zip(animals,ANIMAL_VALUES))
def animals_left(animals, hp): return sum(round(c*hp) for c in animals)

def apply_spawns(animals, distance, speed):
    animals = animals[:]
    last = next((i for i in range(9,-1,-1) if animals[i]!=0), None)
    if last is None: return animals
    spawn_rate = SPAWN_RATES[last]
    runtime = distance/speed if distance < 20 else (20/speed) + ((distance-20)/(speed*4.2))
    units_spawned = round(int(runtime*60)/spawn_rate)
    below = [animals[i] for i in range(last-1,-1,-1) if animals[i]>0]
    if below and animals[last] < below[0]:
        units_spawned = min(units_spawned, below[0] - animals[last])
    animals[last] += units_spawned
    return animals

def find_gaul(animals, pf, max_tt=500):
    for ntt in range(1, max_tt+1):
        hp   = gaul_hp(animals, ntt)
        cost = round(ntt*hp)*1050
        gain = res_gained(animals, hp)
        if animals_left(animals, hp) <= 1 and gain >= pf*cost:
            return dict(ntt=ntt, hp=hp, cost=cost, gain=gain,
                        lost=round(ntt*hp), surviving=ntt-round(ntt*hp))
    return None

def find_teuton(animals, pf, max_clubs=500, max_tk=20):
    best_tc, best = np.inf, None
    for ntk in range(0, max_tk+1):
        for nclub in range(1, max_clubs+1):
            hp   = teuton_hp(animals, nclub, ntk)
            cost = round(ntk*hp)*1525 + round(nclub*hp)*250
            gain = res_gained(animals, hp)
            tc   = 250*nclub + 1525*ntk
            if animals_left(animals, hp) <= 1 and gain >= pf*cost and tc < best_tc:
                best_tc = tc
                best = dict(nclub=nclub, ntk=ntk, hp=hp, cost=cost, gain=gain,
                            clubs_lost=round(nclub*hp), tk_lost=round(ntk*hp),
                            clubs_surv=nclub-round(nclub*hp), tk_surv=ntk-round(ntk*hp))
    return best

# ── UI ────────────────────────────────────────────────────────────────────────
st.title("⚔ Team Calculator")

# tribe + settings
c1, c2, c3 = st.columns([1.2, 1, 1])
tribe  = c1.selectbox("Tribe", ["Gaul", "Teuton"])
dist   = c2.number_input("Distance (fields)", min_value=0.0, value=0.0, step=0.5,
                          help="Set to 0 to skip spawn calculation")
pf     = c3.number_input("Profit factor", min_value=0.0, max_value=2.0,
                          value=0.80, step=0.05, format="%.2f")

badge = "🛡 GAUL — Teutates Thunder" if tribe=="Gaul" else "🪓 TEUTON — Clubswinger + TK"
cls   = "tribe-gaul" if tribe=="Gaul" else "tribe-teuton"
st.markdown(f'<span class="tribe-badge {cls}">{badge}</span>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Animal counts</div>', unsafe_allow_html=True)

# animal inputs — 5 per row
animals = []
for row_start in range(0, 10, 5):
    cols = st.columns(5)
    for i, col in enumerate(cols):
        idx = row_start + i
        val = col.number_input(
            f"{ANIMAL_ICONS[idx]} {ANIMAL_NAMES[idx]}",
            min_value=0, value=0, step=1, key=f"animal_{idx}"
        )
        animals.append(val)

# ── calculate ─────────────────────────────────────────────────────────────────
calc = st.button("⚔ Calculate", use_container_width=True)

if calc:
    if sum(animals) == 0:
        st.warning("Enter at least one animal.")
    else:
        speed = 19 if tribe=="Gaul" else 7
        spawned = apply_spawns(animals, dist, speed) if dist > 0 else animals[:]
        result  = find_gaul(spawned, pf) if tribe=="Gaul" else find_teuton(spawned, pf)

        spawn_diff = [spawned[i]-animals[i] for i in range(10)]
        had_spawns = dist > 0 and any(d > 0 for d in spawn_diff)

        st.markdown('<div class="section-title">Result</div>', unsafe_allow_html=True)

        if result is None:
            st.markdown('<div class="unclearable">✖ No valid team found within limits.</div>',
                        unsafe_allow_html=True)
        else:
            hp   = result["hp"]
            gain = result["gain"]
            cost = result["cost"]
            net  = gain - cost

            def cell(v, cls="val"):
                s = str(v)
                c = "zero" if s == "0" else cls
                return f'<td class="{c}">{s}</td>'

            def make_table(section_label, section_cls, troops, counts, losses, survivals):
                # troops: list of (icon, name)
                html = f'<table class="combat-table"><tr><th class="section-header {section_cls}" colspan="{len(troops)+1}">{section_label}</th></tr>'
                # header row: icons
                html += '<tr class="header-row"><th></th>'
                for icon, name in troops:
                    html += f'<th>{icon}<br><span style="font-size:0.7rem">{name}</span></th>'
                html += '</tr>'
                # troops row
                html += '<tr><td class="label-cell">Troops</td>'
                for c in counts: html += cell(c)
                html += '</tr>'
                # casualties row
                html += '<tr><td class="label-cell">Casualties</td>'
                for l in losses: html += cell(l, "lost")
                html += '</tr>'
                # surviving row
                html += '<tr><td class="label-cell">Surviving</td>'
                for s in survivals: html += cell(s, "surv")
                html += '</tr></table>'
                return html

            html = '<div class="combat-wrap">'

            if tribe == "Gaul":
                troops = [("🐴", "TT")]
                counts    = [result["ntt"]]
                losses    = [result["lost"]]
                survivals = [result["surviving"]]
            else:
                troops = [("🪓", "Club"), ("🐎", "TK")]
                counts    = [result["nclub"], result["ntk"]]
                losses    = [result["clubs_lost"], result["tk_lost"]]
                survivals = [result["clubs_surv"], result["tk_surv"]]

            html += make_table("⚔ OFFENSE", "off-header", troops, counts, losses, survivals)

            # defense table: animals
            animal_troops = [(ANIMAL_ICONS[i], ANIMAL_NAMES[i]) for i in range(10) if spawned[i] > 0]
            animal_counts  = [spawned[i] for i in range(10) if spawned[i] > 0]
            animal_killed  = [round(spawned[i]*(1-hp)) for i in range(10) if spawned[i] > 0]
            animal_surv    = [round(spawned[i]*hp) for i in range(10) if spawned[i] > 0]
            html += make_table("🐾 DEFENSE (nature)", "def-header", animal_troops, animal_counts, animal_killed, animal_surv)

            html += '</div>'

            # spawn note
            if had_spawns:
                spawn_strs = [f"+{spawn_diff[i]} {ANIMAL_NAMES[i].lower()}"
                              for i in range(10) if spawn_diff[i] > 0]
                html += f'<div style="font-family:Share Tech Mono,monospace;font-size:0.8rem;color:#58a6ff;margin-bottom:0.6rem">↑ Spawned during travel: {", ".join(spawn_strs)}</div>'

            # summary bar
            net_col = "#3fb950" if net >= 0 else "#f85149"
            html += f'''<div class="summary-card">
  <div class="sum-item"><span class="sum-label">HP lost</span><span class="sum-value" style="color:#58a6ff">{hp*100:.1f}%</span></div>
  <div class="sum-item"><span class="sum-label">Animals left</span><span class="sum-value">{animals_left(spawned, hp)}</span></div>
  <div class="sum-item"><span class="sum-label">Resources gained</span><span class="sum-value" style="color:#3fb950">{gain:,}</span></div>
  <div class="sum-item"><span class="sum-label">Troops cost</span><span class="sum-value" style="color:#f85149">{cost:,}</span></div>
  <div class="sum-item"><span class="sum-label">Net profit</span><span class="sum-value" style="color:{net_col}">{net:+,}</span></div>
</div>'''

            st.markdown(html, unsafe_allow_html=True)
