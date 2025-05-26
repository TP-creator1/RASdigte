import streamlit as st
import PyPDF2
import io

st.title("🔍 Hjælp til digtanalyse")
st.markdown("Denne app guider dig gennem analysen af et digt med spørgsmål og en værktøjskasse til støtte. Du kan også indtaste og gemme dine egne noter.")

# Eksempeldigte
st.header("📚 Vælg et eksempeldigt")
eksempeldigte = {
    "Det er forår" : "Det er forår. I mit sind / gror der ord, som vil ud / med blomster og blade / og fuglekvidder.",
    "Jeg lægger mig ned" : "Jeg lægger mig ned i det våde græs / og lytter til jordens sagte suk / af regn, som falder.",
    "Intet" : "Intet er større end stilhed / når stormen har talt færdig / og intet står tilbage end mig."
}
valg = st.selectbox("Vælg et eksempeldigt til analyse", ["(Vælg)"] + list(eksempeldigte.keys()))
digt = ""
if valg != "(Vælg)":
    digt = eksempeldigte[valg]
    st.text_area("📖 Eksempeldigt", digt, height=150)
    st.markdown("**Modelanalyse**")
    if valg == "Det er forår":
        st.markdown("- Tema: Natur og forvandling.\n- Sproglige virkemidler: Billedsprog, allitteration.\n- Stil: Enkel og optimistisk.")
    elif valg == "Jeg lægger mig ned":
        st.markdown("- Tema: Natur og refleksion.\n- Sproglige virkemidler: Sansning, roligt tempo.\n- Stil: Meditativ.")
    elif valg == "Intet":
        st.markdown("- Tema: Eksistens og ensomhed.\n- Sproglige virkemidler: Antitese (stilhed vs. storm), minimalistisk sprog.\n- Stil: Alvorlig og eftertænksom.")

# Mulighed for at indsætte digtet
st.header("📥 Indsæt eller upload dit digt")
manual_digt = st.text_area("✏️ Indtast digtet manuelt her")
if manual_digt:
    digt = manual_digt

uploaded_file = st.file_uploader("📄 Eller upload digtet som .txt eller .pdf", type=["txt", "pdf"])
if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        digt = "\n".join([page.extract_text() or "" for page in pdf_reader.pages])
    elif uploaded_file.type == "text/plain":
        digt = uploaded_file.read().decode("utf-8")
    st.success("Digt indlæst fra fil!")
    st.text_area("📖 Digt fra fil", digt, height=150)

# Trinvis analyse
st.header("1. Første møde med digtet")
st.text_input("🔸 Hvad er din umiddelbare oplevelse af digtet?", key="oplevelse")
st.text_input("🔸 Hvilke stemninger og følelser vækker det?", key="stemning")

st.header("2. Indhold og tema")
st.text_input("🔸 Hvad handler digtet om – på overfladen og i dybden?", key="indhold")
st.text_input("🔸 Er der et centralt tema (kærlighed, død, natur, identitet, kritik)?", key="tema")
st.text_input("🔸 Hvilke billeder eller symboler optræder?", key="symboler")

st.header("3. Sprog og stil")
st.text_input("🔸 Hvilke sproglige virkemidler bruger digtet? (metaforer, sammenligninger, gentagelser, osv.)", key="virkemidler")
st.text_input("🔸 Er sproget let, svært, gammeldags, moderne?", key="sprog")
st.text_input("🔸 Er der lydlige virkemidler som rim, rytme eller allitteration?", key="lyd")

st.header("4. Form og struktur")
st.text_input("🔸 Hvor mange strofer og vers er der?", key="strofer")
st.text_input("🔸 Er der en fast form (fx sonet) eller fri form?", key="form")
st.text_input("🔸 Hvordan hænger form og indhold sammen?", key="sammenhaeng")

st.header("5. Fortolkning og perspektivering")
st.text_input("🔸 Hvad tror du digtet vil sige – hvad er budskabet?", key="budskab")
st.text_input("🔸 Hvilken tid og sammenhæng er digtet skrevet i?", key="tid")
st.text_input("🔸 Kan du sammenligne med andre tekster eller forfattere?", key="perspektiv")

# Mulighed for at gemme noter (uden filskrivning pga. Streamlit Cloud begrænsning)
st.header("📝 Noter og refleksioner")
noter = st.text_area("Skriv dine egne noter her")
st.download_button("💾 Download dine noter", noter, file_name="mine_noter.txt")

# Værktøjskassen
st.sidebar.title("🧰 Værktøjskasse til digtanalyse")
st.sidebar.subheader("Sproglige virkemidler")
st.sidebar.markdown("- **Metafor**: Et billede uden 'som'.\n- **Sammenligning**: Et billede med 'som' eller 'ligesom'.\n- **Personifikation**: Døde ting får menneskelige egenskaber.\n- **Gentagelse**: Ord eller sætninger gentages for at skabe rytme eller vægt.")

st.sidebar.subheader("Form og opbygning")
st.sidebar.markdown("- **Strofe**: En gruppe af verslinjer.\n- **Rim**: Enderim, indrim, bogstavrim (allitteration).\n- **Vers**: En enkelt linje i et digt.\n- **Fast form**: Digte med fast struktur (fx sonet).\n- **Fri form**: Uden fast rim/rytme.")

st.sidebar.subheader("Tematiske begreber")
st.sidebar.markdown("- **Eksistens**: Livets mening, identitet, død.\n- **Natur**: Forholdet mellem menneske og natur.\n- **Samfundskritik**: Digtet kritiserer sociale eller politiske forhold.\n- **Kærlighed**: Følelser og relationer mellem mennesker.")

st.sidebar.subheader("Tidsperioder og forfatterskab")
st.sidebar.markdown("- **Romantik**: Følelser, natur, det guddommelige.\n- **Modernisme**: Fremmedgørelse, by, individ.\n- **Realistisk digtning**: Hverdagsliv, social indsigt.\n- **Det moderne gennembrud**: Samfunds- og kønskritik, realisme.")
