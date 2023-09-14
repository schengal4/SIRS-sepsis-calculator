import streamlit as st

def main():
    st.title("SIRS, Sepsis, and Septic Shock Criteria")
    st.write("Defines the severity of sepsis and septic shock.")

    # Instructions for using the calculator
    st.write(":black[**INSTRUCTIONS**]")
    st.write("Answer the questions and scroll down to see the results.")
    st.write("""**Note**: sepsis definitions are evolving and difficult to finalize without a gold standard.\
            These criteria are what is reported and the literature is listed, but note that nuances\
            exist for all sepsis definitions and can differ locally, regionally, nationally, and \
            internationally, as well as in clinical vs administrative vs research settings. Sepsis-3 \
            Consensus Definitions are frequently cited as one paradigm. """)
    st.write("For patients under 18, please use the Pediatric SIRS, Sepsis, and Septic Shock Criteria.")

    # Input fields for SIRS
    st.write(":orange[**Systemic inflammatory response syndrome (SIRS) Criteria (≥2 meets SIRS definition)**]")
    temperature = st.radio("Temp >38°C (100.4°F) or <36°C (96.8°F)?", ["No", "Yes"])
    heart_rate = st.radio("Heart Rate >90 bpm?", ["No", "Yes"])
    respiratory_rate = st.radio("Respiratory rate >20 or PaCO₂ <32 mm Hg?", ["No", "Yes"])
    white_blood_cells = st.radio("WBC >12,000/mm³, <4,000/mm³, or >10% bands?", ["No", "Yes"])

    # Input field for sepsis
    st.write(":orange[**Sepsis Criteria (SIRS + Source of Infection)**]")
    sepsis = st.radio("Suspected or present source of infection", ["No", "Yes"])

    # Input field for severe sepsis
    st.write(":orange[**Severe Sepsis Criteria (Organ Dysfunction, Hypotension, or Hypoperfusion)**]")
    severe_sepsis = st.radio("Lactic acidosis, SBP <90 or SBP drop ≥40 mm Hg of normal", ["No", "Yes"])

    # Input field for septic shock
    st.write(":orange[**Septic Shock Criteria**]")
    septic_shock = st.radio("Severe sepsis with hypotension, despite adequate fluid resuscitation", ["No", "Yes"])

    # Input field for multiple organ dysfunction syndrome
    st.write(":orange[**Multiple Organ Dysfunction Syndrome Criteria**]")
    multi_organ_failure = st.radio("Evidence of ≥2 organs failing", ["No", "Yes"])

    # Check SIRS criteria
    sirs_criteria_met = 0
    if temperature == "Yes":
        sirs_criteria_met += 1
    if heart_rate == "Yes":
        sirs_criteria_met += 1
    if respiratory_rate == "Yes":
        sirs_criteria_met += 1
    if white_blood_cells == "Yes":
        sirs_criteria_met += 1
    has_sirs = sirs_criteria_met >= 2 # If patient meets >= 2 of the criteria, he/she has SIRS

    # Check sepsis, severe sepsis, septic shock, and multi-organ dysfunction criteria
    has_sepsis = has_sirs and sepsis == "Yes"
    has_severe_sepsis = has_sirs and severe_sepsis == "Yes"
    has_septic_shock = has_sirs and septic_shock == "Yes"
    has_multi_organ_dysfunction_syndrome = has_sirs and multi_organ_failure == "Yes"

    # Display result to screen
    if not has_sirs:
        st.info("This patient does not meet SIRS criteria. For other causes of shock, see the Next Steps section.")
    if has_multi_organ_dysfunction_syndrome:
        if has_sepsis:
            st.error("**This patient meets multiple organ dysfunction syndrome criteria. Follow your guidelines for sepsis, \
                    which typically include aggresive fluid resuscitation, early, broad-spectrum antibiotics, ICU consultation,\
                    CVP evaluation, and occasionally pressors and transfusion.**")
        else:
            st.error("**This patient meets multiple organ dysfunction syndrome criteria.**")
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
        st.warning("**This patient meets sepsis criteria. Follow your guidelines for sepsis, which typically include aggressive\
                fluid resuscitation, early, broad-spectrum antibiotics, ICU consultation, CVP evaluation, and occasionally\
                pressors and transfusion.**")
    elif has_sirs:
        st.info("**This patient meets SIRS criteria.**")

    # Divider to separate calculator from the further information below.    
    st.divider()
    st.write("**Credits**")
    st.write("This calculator is built off an [MDCalc app](https://www.mdcalc.com/calc/1096/sirs-sepsis-septic-shock-criteria).")
    st.write("Much of the text in this app is taken verbatim from that app.")
    st.divider()
    # Buttons with more info if clicked on
    col1, col2, col3 = st.columns(3)
    next_steps_button_clicked = col1.button("**Next Steps**", use_container_width=True)
    evidence_button_clicked = col2.button("**Evidence**", use_container_width=True)
    creator_insights_button_clicked = col3.button("**Creator Insights**", use_container_width=True)
    if next_steps_button_clicked:
        next_steps()
    if evidence_button_clicked:
        sepsis_information()
    if creator_insights_button_clicked:
        creator_insights()
   
def next_steps():
    """
    Print out the next steps.
    """
    # Using a list to store each line for easier management
    lines = []
    
    # Adding the header
    lines.append("**MANAGEMENT**")
    
    # Adding the content
    lines.append(
        "- When a patient presents with two or more *SIRS* criteria but with hemodynamic stability "
        "(i.e. blood pressure at baseline), a clinical assessment must be made to determine the "
        "possibility of an infectious etiology."
    )
    lines.append(
        "- If an infection is suspected or confirmed, the patient is diagnosed with *Sepsis* and a "
         "lactate level is obtained to determine the degree of hypoperfusion and inflammation. A "
         "lactate level ≥4 mmol/L is considered diagnostic for *Severe Sepsis*, and aggressive management "
         "with broad spectrum antibiotics, intravenous fluids, and vasopressors should be initiated "
         "(aka *EGDT*)."
         )
    lines.append(
        "- Patients that present with a suspected or confirmed infection AND hemodynamic instability "
        "should immediately be treated for *Septic Shock*. While SIRS criteria will likely be present in "
        "these patients, aggressive management should not be delayed while waiting for laboratory values "
        "such as the WBC or lactate."
    )
    lines.append("- The management of *Severe Sepsis* and *Septic Shock* is the topic of intense research and scrutiny.")
    lines.append(
        "- While *Early Goal Directed Therapy* has been advocated in the *Surviving Sepsis Guidelines*, there "
        "remains controversy as to which of the bundled interventions are necessary."
    )
    lines.append(
        '- Recent studies have showed *EGDT* not to be better than "usual care", and called for significant '
        'amendments to currently used sepsis protocols.'
    )
    lines.append(
        "- To date, most experts agree that early recognition of *Sepsis*, *Severe Sepsis*, and *Septic Shock*, "
        "and early administration of broad spectrum and organism specific antibiotic are the most critical "
        "actions."
    )
    lines.append(
        "- There remains controversy in the type of fluids that should be used, "
        "their quantity, and the timing of vasopressors and/or inotropes.\n  "
    )

    lines.append("\n**CRITICAL ACTIONS**")
    lines.append("- Assess all patients with 2 or more *SIRS* criteria for the possibility of an infectious etiology.")
    lines.append(
        "- Screen for *Severe Sepsis* by obtaining a lactate level on patients with *Sepsis*, " 
        "that are elderly, immunocompromised, or ill appearing."
    )
    lines.append(
        "- Some experts recommend obtaining a lactate level on all patients in whom blood cultures are sent. "
        "This is institution dependent however and not mandated in any guidelines."
    )
    lines.append(
        "- When *Severe Sepsis* or *Septic Shock* are identified, initiate broad spectrum antibiotics immediately. "
        "These antibiotics should be organism specific and therefore institutional antibiograms should be used."
    )
    lines.append(
        "- The *Surviving Sepsis Campaign Guidelines* recommend initiation of antimicrobials within one hour from the time "
        "of recognition of *Severe Sepsis* or *Septic Shock*, or within three hours of the patient’s arrival to the hospital."
    )
                
    # Joining the lines together with newline characters
    output = '\n'.join(lines)
    st.write(output)
    
    return output

def sepsis_information():

    """ Print out the information about the calculator and its formula, as well as the research supporting it."""

    # Using a list to store each section for easier management
    sections = []
    
    # Adding the header and content
    sections.append("**FORMULA**\n")
    sections.append("Series of Yes/No questions.\n")
    
    sections.append("**FACTS & FIGURES**")
    sections.append("- SIRS - 2 YES answers meets criteria.")
    sections.append("- Sepsis Criteria - 2 YES of SIRS + Suspected Source of Infection.")
    sections.append("- Severe Sepsis Criteria - 2 YES of SIRS + Lactic Acidosis, SBP.")
    sections.append("- Multiple Organ Dysfunction Syndrome - 2 YES of SIRS + Evidence of ≥ 2 Organs Failing.")
    sections.append("Check with your own hospital for its sepsis guidelines, sepsis 'bundle' or sepsis algorithm. "
                    "Two excellent sepsis references ([1](https://emcrit.org/squirt/severe-sepsis-resources/), \
                    [2](https://crashingpatient.com/wp-content/pdf/Loma%20Linda%20STOP%20Sepsis%20Bundle.pdf)) \
                    come from the [EMCrit](https://emcrit.org/) website.\n")
    
    sections.append("**EVIDENCE APPRAISAL**")
    sections.append("- [This paper](https://pubmed.ncbi.nlm.nih.gov/1303622/) was released after the first consensus conference in 1991. The goal of this "
                    "conference was to standardize the use of terms such as “SIRS”, “sepsis”, “severe sepsis”, and "
                    "“septic shock” to facilitate enrollment of patients in clinical trials.")
    sections.append("- In 2001, the International Sepsis Definitions Conference expanded on these definitions by "
                    "adding additional elements such as laboratory data. See [here](https://pubmed.ncbi.nlm.nih.gov/12682500/).\n")
    
    sections.append("**LITERATURE**\n")
    sections.append("ORIGINAL/PRIMARY REFERENCE")
    sections.append("- [International Guidelines for Management of Severe Sepsis and Septic Shock: \
                    2012](https://content.guidelinecentral.com/guideline/get/pdf/3525)")
    sections.append("- Bone RC, Balk RA, Cerra FB, Dellinger RP, Fein AM, Knaus WA, Schein RM, Sibbald WJ. "
                    "[Definitions for sepsis and organ failure and guidelines for the use of innovative therapies in "
                    "sepsis.](https://pubmed.ncbi.nlm.nih.gov/1303622/) The ACCP/SCCM Consensus \
                    Conference Committee. American College of Chest "
                    "Physicians/Society of Critical Care Medicine.Chest. 1992 Jun;101(6):1644-55.\n")
    
    sections.append("CLINICAL PRACTICE GUIDELINES")
    sections.append("- [Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and \
                    Septic Shock](https://journals.lww.com/ccmjournal/Fulltext/2021/11000/Surviving_Sepsis_Campaign__International.21.aspx): "
                    "Critical Care Medicine\n")
    
    sections.append("OTHER REFERENCES")
    sections.append("- [Surviving Sepsis Campaign Responds to ProCESS Trial](https://www.icnarc.org/DataServices/Attachments/Download/3d1bc8e1-1ed1-e311-a997-d48564544b14).")
    sections.append("- Levy MM, Fink MP, Marshall JC, et al. [2001 SCCM/ESICM/ACCP/ATS/SIS International Sepsis "
                    "Definitions Conference](https://pubmed.ncbi.nlm.nih.gov/12682500/). Crit Care Med. 2003;31(4):1250–1256.")
    
    # Joining the sections together with newline characters
    output = '\n'.join(sections)
    st.write(output)
    
    return output
def creator_insights():
        st.subheader("From the creator Dr. Robert A. Balk")
        sections = []
        sections.append( "**Why did you issue the consensus statement on the SIRS Criteria and Septic protocol? "
            "Was there a clinical experience that inspired you to update these guidelines for clinicians?**\n")
        sections.append("The American College of Chest Physicians and the Society of Critical Care Medicine convened "
            "the first sepsis definitions conference in 1991 to help researchers define a population of severe "
            "septic patients who would be suitable for enrollment in clinical trials of new investigational agents "
            "that were thought to be able to block the proinflammatory cascade, and thus improve "
            "survival of patients with severe sepsis and septic shock. To accomplish this goal, the conference "
            "participants aimed to use readily available clinical signs, symptoms and basic laboratory studies "
            "that would then support a rapid diagnosis. The trade-off for such a sensitive group of parameters "
            "that would alert physicians to the early manifestations of severe sepsis and septic shock was "
            "a group of criteria that lacked a great deal of specificity. It was also recognized that the same "
            "clinical signs, symptoms and laboratory data seen in patients with severe sepsis and septic shock "
            "were also present in other populations of critically ill patients with other proinflammatory conditions"
            ", such as trauma, burns, pancreatitis, etc. It was therefore decided to define the patients with a "
            "documented or highly suspicious infection that results in a systemic inflammatory response as having "
            "sepsis. In the ICU, sepsis patients would typically manifest organ dysfunction (severe sepsis) "
            "or septic shock, with or without multiple organ dysfunction syndrome.")
        sections.append("The second goal of the consensus conference was to facilitate better communication in the literature "
            "and scientific communication (including on rounds) which will enhance future comparative efforts "
            "among clinical trials and facilitate outcome comparisons of septic populations.\n")
        sections.append("**What pearls, pitfalls and/or tips do you have for users of the SIRS Criteria? Are there cases "
            "in which they have been applied, interpreted, or used inappropriately?**\n")
        sections.append("Users of the SIRS - Sepsis criteria need to understand that they are overly sensitive to identify "
            "potential patients as early as possible, but the criteria lack specificity. The 2001 international "
            "sepsis definition conference attempted to enhance the utility and specificity of the definition "
            "by including additional signs, symptoms, laboratory data, biomarkers and physiologic parameters. "
            "Unfortunately, we are still awaiting the perfect clinical definition that has both high sensitivity "
            "and specificity for severe sepsis and septic shock.\n"
            )
        sections.append("For example, if you believe the patient has an infection AND meets the SIRS criteria, then the "
            "patient may be septic. Infection is likely its most useful application. The score is designed "
            "to be sensitive, but not specific. It's meant to help with early diagnosis. SIRS was not designed "
            "to be algorithmic, such as: if you have a score of X, you must do Y. Rather, it's a table of points to "
            "see whether or not the patient has any of these criteria. You then apply that result to the specific "
            "clinical scenario.\n")
        sections.append( "**What recommendations do you have for health care providers once they have applied the SIRS Criteria? "
                         "Are there any adjustments or updates you would make to the criteria given recent changes in medicine?**\n")
        sections.append( "Investigators are continuing to refine the SIRS - Sepsis criteria and make them more clinically useful. "
            "The current approach has involved the use of various biomarkers to facilitate the identification "
            "of patients with a high likelihood of bacterial infection and/or high risk for morbidity and mortality. "
            "Some of the current biomarkers under evaluation include procalcitonin, C-reactive protein, "
            "proadrenalmodulin, N-terminal BNP and lactate.\n")
        sections.append("**Other comments? Any new research or papers on this topic in the pipeline?**\n")
        sections.append("The future will likely include significant refinements in the SIRS criteria using biomarkers and PCR or "
            "nanotechnology to improve the specificity of the diagnosis and provide the information "
            "in a more rapid fashion.\n")
        sections.append("**ABOUT THE CREATOR\n**")
        sections.append("Robert A. Balk, MD, is a professor and practicing physician in pulmonology, internal medicine and "
            "critical care at Rush University Medical Center. His research interests include septic shock, acute "
            "lung injury, acute respiratory distress syndrome and ventilator-associated pneumonia.\n")
        sections.append("*To view Dr. Robert A. Balk's publications, visit " 
            "[PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=Balk+RA%5BAuthor%5D)*.")
        output = '\n'.join(sections)
        st.write(output)
if __name__ == "__main__": 
    main()