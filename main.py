import streamlit as st

st.title("SIRS, Sepsis, and Septic Shock Criteria")
st.write("Defines the severity of sepsis and septic shock.")
st.write(":blue[**INSTRUCTIONS**]")
st.write("Answer the questions and scroll down to see the results.")
st.write("""**Note**: sepsis definitions are evolving and difficult to finalize without a gold standard.\
          These criteria are what is reported and the literature is listed, but note that nuances\
          exist for all sepsis definitions and can differ locally, regionally, nationally, and \
         internationally, as well as in clinical vs administrative vs research settings. Sepsis-3 \
         Consensus Definitions are frequently cited as one paradigm. """)
st.write("For patients under 18, please use the Pediatric SIRS, Sepsis, and Septic Shock Criteria.")

# Input fields for SIRS, sepsis, severe sepsis, septic shock, and multi-organ dysfunction criteria using radio buttons
st.write(":orange[**Systemic inflammatory response syndrome (SIRS) Criteria (≥2 meets SIRS definition)**]")
temperature = st.radio("Temp >38°C (100.4°F) or <36°C (96.8°F)?", ["No", "Yes"])
heart_rate = st.radio("Heart Rate >90 bpm?", ["No", "Yes"])
respiratory_rate = st.radio("Respiratory rate >20 or PaCO₂ <32 mm Hg?", ["No", "Yes"])
white_blood_cells = st.radio("WBC >12,000/mm³, <4,000/mm³, or >10% bands?", ["No", "Yes"])

st.write(":orange[**Sepsis Criteria (SIRS + Source of Infection)**]")
sepsis = st.radio("Suspected or present source of infection", ["No", "Yes"])

st.write(":orange[**Severe Sepsis Criteria (Organ Dysfunction, Hypotension, or Hypoperfusion)**]")
severe_sepsis = st.radio("Lactic acidosis, SBP <90 or SBP drop ≥40 mm Hg of normal", ["No", "Yes"])

st.write(":orange[**Septic Shock Criteria**]")
septic_shock = st.radio("Severe sepsis with hypotension, despite adequate fluid resuscitation", ["No", "Yes"])

st.write(":orange[**Multiple Organ Dysfunction Syndrome Criteria**]")
multi_organ_failure = st.radio("Evidence of ≥2 organs failing", ["No", "Yes"])

# Check SIRS, sepsis, severe sepsis, septic shock, and multi-organ dysfunction criteria
sirs_criteria_met = 0
if temperature == "Yes":
    sirs_criteria_met += 1
if heart_rate == "Yes":
    sirs_criteria_met += 1
if respiratory_rate == "Yes":
    sirs_criteria_met += 1
if white_blood_cells == "Yes":
    sirs_criteria_met += 1
has_sirs = sirs_criteria_met >= 2
has_sepsis = has_sirs and sepsis == "Yes"
has_severe_sepsis = has_sirs and severe_sepsis == "Yes"
has_septic_shock = has_sirs and septic_shock == "Yes"
has_multi_organ_dysfunction_syndrome = has_sirs and multi_organ_failure == "Yes"

# Display result to screen
if not has_sirs:
    st.info("**This patient does not meet SIRS criteria. For other causes of shock, see the Next Steps section.**")
if has_multi_organ_dysfunction_syndrome:
    if has_sepsis:
        st.warning("**This patient meets multiple organ dysfunction syndrome criteria. Follow your guidelines for sepsis, \
                 which typically include aggressive fluid resuscitation, early, broad-spectrum antibiotics, ICU consultation,\
                  CVP evaluation, and occasionally pressors and transfusion.**")
    else:
        st.warning("**This patient meets multiple organ dysfunction syndrome criteria.**")
elif has_septic_shock:
    if has_sepsis:
        st.warning("**This patient meets septic shock criteria. Follow your guidelines for sepsis, which typically include\
                  aggressive fluid resuscitation, early, broad-spectrum antibiotics, ICU consultation, CVP evaluation,\
                  and occasionally pressors and transfusion.**")
    else:
        st.warning("**This patient meets septic shock criteria.**")
elif has_severe_sepsis:
    if has_sepsis:
        st.warning("**This patient meets severe sepsis criteria. Follow your guidelines for sepsis, which typically include\
                  aggressive fluid resuscitation, early, broad-spectrum antibiotics, ICU consultation, CVP evaluation, and\
                  occasionally pressors and transfusion.**")
    else:
        st.warning("**This patient meets severe sepsis criteria.**")
elif has_sepsis:
    st.info("**This patient meets sepsis criteria. Follow your guidelines for sepsis, which typically include aggressive\
              fluid resuscitation, early, broad-spectrum antibiotics, ICU consultation, CVP evaluation, and occasionally\
              pressors and transfusion.**")
elif has_sirs:
    st.info("**This patient meets SIRS criteria.**")