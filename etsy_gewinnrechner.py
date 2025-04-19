import streamlit as st
import pandas as pd

st.set_page_config(page_title="Etsy Gewinnrechner", layout="centered")
st.title("💰 Etsy Gewinnrechner")
st.markdown("Gib unten deine Werte ein, um den verbleibenden Gewinn zu berechnen. Die Ergebnisse bei unterschiedlichen Rabattstufen findest du in der Tabelle unten.")

# Eingabe
verkaufspreis = st.number_input("🛒 Produktpreis (€)", min_value=0.0, step=0.01, value=24.98)
versandkosten = st.number_input("📦 Versandkosten (€)", min_value=0.0, step=0.01, value=3.99)
produktkosten = st.number_input("🏷️ Einkaufskosten (€)", min_value=0.0, step=0.01, value=10.48)


# Gewinnberechnung

def berechne_gewinn(verkaufspreis, versandkosten, produktkosten, rabatt_prozent=0):
    rabattbetrag = verkaufspreis * (rabatt_prozent / 100)
    rabattierter_preis = verkaufspreis - rabattbetrag
    gesamtpreis = rabattierter_preis  # ohne Versandkosten

    etsy_gebuehren_berechnungsbasis = rabattierter_preis + versandkosten
    verkaufsgebuehr = etsy_gebuehren_berechnungsbasis * 0.065
    zahlungsgebuehr = etsy_gebuehren_berechnungsbasis * 0.04 + 0.30
    listinggebuehr = 0.19
    gesamtgebuehren = verkaufsgebuehr + zahlungsgebuehr + listinggebuehr

    gesamtkosten = produktkosten + gesamtgebuehren
    gewinn = rabattierter_preis - gesamtkosten

    return {
        "Rabatt %": f"{rabatt_prozent}%",
        "Rabattierter Preis": round(rabattierter_preis, 2),
        "Gesamtgebühren": round(gesamtgebuehren, 2),
        "Produktkosten": round(produktkosten, 2),
        "Gewinn": round(gewinn, 2)
    }


rabattstufen = [0, 5, 10, 15, 20]
ergebnisse = [berechne_gewinn(verkaufspreis, versandkosten, produktkosten, r) for r in rabattstufen]
df = pd.DataFrame(ergebnisse)

st.markdown("---")
st.subheader("📊 Gewinnberechnung bei verschiedenen Rabatten")
st.dataframe(df.style.format("{:.2f}").highlight_max(axis=0, color="lightgreen").highlight_min(axis=0, color="salmon"))

# Highlight-Gewinn
aktueller_gewinn = berechne_gewinn(verkaufspreis, versandkosten, produktkosten, 0)["Gewinn"]
st.markdown("---")
st.subheader("💡 Wichtig")
st.markdown(f"**Gewinn ohne Rabatt:** <span style='font-size:22px;color:green;font-weight:bold'>{aktueller_gewinn:.2f} €</span>", unsafe_allow_html=True)
st.caption("Versandkosten gelten als durchlaufender Posten und werden nicht zum Gewinn gerechnet.")
