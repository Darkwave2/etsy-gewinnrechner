import streamlit as st

st.set_page_config(page_title="Etsy Gewinnrechner", layout="centered")
st.title("💰 Etsy Gewinnrechner")
st.markdown("Gib unten deine Werte ein, um den verbleibenden Gewinn zu berechnen.")

# Eingabe
verkaufspreis = st.number_input("🛒 Produktpreis (€)", min_value=0.0, step=0.01, value=24.98)
versandkosten = st.number_input("📦 Versandkosten (€)", min_value=0.0, step=0.01, value=3.99)
produktkosten = st.number_input("🏷️ Einkaufskosten (€)", min_value=0.0, step=0.01, value=10.48)
rabatt_prozent = st.slider("🎁 Rabatt (%)", 0, 100, 0)


def berechne_gewinn(verkaufspreis, versandkosten, produktkosten, rabatt_prozent=0):
    rabattbetrag = verkaufspreis * (rabatt_prozent / 100)
    rabattierter_preis = verkaufspreis - rabattbetrag
    gesamtpreis = rabattierter_preis + versandkosten

    verkaufsgebuehr = gesamtpreis * 0.065
    zahlungsgebuehr = gesamtpreis * 0.04 + 0.30
    listinggebuehr = 0.19
    gesamtgebuehren = verkaufsgebuehr + zahlungsgebuehr + listinggebuehr

    gesamtkosten = produktkosten + gesamtgebuehren
    gewinn = gesamtpreis - gesamtkosten

    return {
        "Rabattbetrag": round(rabattbetrag, 2),
        "Rabattierter Preis": round(rabattierter_preis, 2),
        "Gesamtpreis (mit Versand)": round(gesamtpreis, 2),
        "Verkaufsgebühr (6,5%)": round(verkaufsgebuehr, 2),
        "Zahlungsgebühr (4% + 0,30 €)": round(zahlungsgebuehr, 2),
        "Listinggebühr": round(listinggebuehr, 2),
        "Gesamtgebühren": round(gesamtgebuehren, 2),
        "Produktkosten": round(produktkosten, 2),
        "Gesamtkosten": round(gesamtkosten, 2),
        "Verbleibender Gewinn": round(gewinn, 2)
    }

if st.button("📊 Berechnen"):
    ergebnis = berechne_gewinn(verkaufspreis, versandkosten, produktkosten, rabatt_prozent)
    st.markdown("---")
    st.subheader("📈 Auswertung")
    for key, value in ergebnis.items():
        st.write(f"**{key}:** {value} €")