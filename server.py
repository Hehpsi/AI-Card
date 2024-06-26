from flask import Flask, render_template, request, redirect, url_for
from wtforms import StringField, SelectMultipleField, SelectField, TextAreaField, FieldList, FormField, SubmitField, BooleanField, RadioField
from wtforms.validators import InputRequired, Length, DataRequired
from flask_wtf import FlaskForm

# Create Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Define the main form for AI Cards
class AICardsForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired(), Length(min=2, max=150)])
    version = StringField("Version", validators=[InputRequired(), Length(min=4, max=5)])
    aiTechniques = SelectMultipleField(
        u'AI Techniques', 
        choices=[
                ('reasoning_technique', 'Reasoning Technique'),
                ('learning_technique', 'Learning Technique'),
                ('machine_learning_technique', 'MachineLearning Technique'),
                ('case_based_reasoning', 'Case Based Reasoning'),
                ('common_sense_reasoning', 'Common Sense Reasoning'),
                ('reinforcement_learning', 'Reinforcement Learning'),
                ('supervised_learning', 'Supervised Learning'),
                ('semi_supervised_learning', 'Semi Supervised Learning'),
                ('unsupervised_learning', 'Unsupervised Learning'),
                ('knowledge_based_technique', 'Knowledge Based Technique'),
                ('inductive_programming', 'Inductive Programming'),
                ('symbolic_reasoning', 'Symbolic Reasoning'),
                ('knowledge_representation', 'Knowledge Representation'),
                ('logic_based_technique', 'Logic Based Technique'),
                ('statistical_technique', 'Statistical Technique'),
                ('bayesian_estimation', 'Bayesian Estimation'),
                ('bayesian_optimisation', 'Bayesian Optimisation'),
                ('optimisation_method', 'Optimisation Method'),
                ('search_method', 'Search Method')
        ],
        render_kw={"class": "custom-select-lg"},
        default=[],
        validators=[InputRequired(),]
    )
    providers = StringField("Provider(s)", validators=[InputRequired(), Length(min=4, max=150)])
    developers = StringField("Developer(s)", validators=[InputRequired(), Length(min=4, max=150)])
    purpose = SelectMultipleField(
        "Purpose", validators=[InputRequired(),], 
        choices = [
            ('remote_identification_of_people', 'Remote Identification Of People'),
            ('content_generation', 'Content Generation'),
            ('generating_audio_content', 'Generating Audio Content'),
            ('generating_image_content', 'Generating Image Content'),
            ('generating_video_content', 'Generating Video Content'),
            ('knowledge_reasoning', 'Knowledge Reasoning'),
            ('applying_the_law_to_facts', 'Applying The Law To Facts'),
            ('interpreting_law', 'Interpreting Law'),
            ('interpreting_facts', 'Interpreting Facts'),
            ('decision_making', 'Decision Making'),
            ('examining_application', 'Examining Application'),
            ('examining_asylum_application', 'Examining Asylum Application'),
            ('examining_migration_related_complaints', 'Examining Migration Related Complaints'),
            ('examining_residence_permits_application', 'Examining Residence Permits Application'),
            ('examining_visa_application', 'Examining Visa Application'),
            ('assessment', 'Assessment'),
            ('assessing_past_criminal_behaviour', 'Assessing Past Criminal Behaviour'),
            ('assessing_admission_test', 'Assessing Admission Test'),
            ('assigning_people_to_educational_institutions', 'Assigning People To Educational Institutions'),
            ('determining_access_to_education', 'Determining Access To Education'),
            ('determining_admission_to_educational_institutions', 'Determining Admission To Educational Institutions'),
            ('assessing_student', 'Assessing Student'),
            ('evaluating_learning_outcomes', 'Evaluating Learning Outcomes'),
            ('recruiting', 'Recruiting'),
            ('advertising_vacancies', 'Advertising Vacancies'),
            ('job_application_filtering', 'Job Application Filtering'),
            ('application_screening', 'Application Screening'),
            ('evaluating_job_candidates', 'Evaluating Job Candidates'),
            ('evaluating_employee', 'Evaluating Employee'),
            ('evaluating_interview', 'Evaluating Interview'),
            ('evaluating_recruitment_test', 'Evaluating Recruitment Test'),
            ('evaluating_employee_behaviour', 'Evaluating Employee Behaviour'),
            ('evaluating_employee_performance', 'Evaluating Employee Performance'),
            ('making_promotion_decision', 'Making Promotion Decision'),
            ('making_termination_decision', 'Making Termination Decision'),
            ('assessing_creditworthiness', 'Assessing Creditworthiness'),
            ('determining_credit_score', 'Determining Credit Score'),
            ('evaluating_reliability_of_evidence', 'Evaluating Reliability Of Evidence'),
            ('assessing_immigration_eligibility', 'Assessing Immigration Eligibility'),
            ('individual_risk_assessment', 'Individual Risk Assessment'),
            ('assessing_people_related_risk', 'Assessing People Related Risk'),
            ('assessing_health_risk', 'Assessing Health Risk'),
            ('assessing_risk_for_potential_victims_of_criminal_offences', 'Assessing Risk For Potential Victims Of Criminal Offences'),
            ('assessing_risk_of_irregular_immigration', 'Assessing Risk Of Irregular Immigration'),
            ('assessing_risk_of_offending', 'Assessing Risk Of Offending'),
            ('assessing_risk_of_reoffending', 'Assessing Risk Of Reoffending'),
            ('assessing_security_risk', 'Assessing Security Risk'),
            ('assessing_personality_traits', 'Assessing Personality Traits'),
            ('evaluating_eligibility_to_access_public_assistance_services', 'Evaluating Eligibility To Access Public Assistance Services'),
            ('verifying_authenticity_of_travel_document', 'Verifying Authenticity Of Travel Document'),
            ('biometric_categorisation', 'Biometric Categorisation'),
            ('detection', 'Detection'),
            ('deep_fake_detection', 'Deep Fake Detection'),
            ('detecting_non_authentic_document', 'Detecting Non-Authentic Document'),
            ('detecting_emotional_state', 'Detecting Emotional State'),
            ('discovering_crime_relationships', 'Discovering Crime Relationships'),
            ('discovering_crime_patterns', 'Discovering Crime Patterns'),
            ('planning', 'Planning'),
            ('dispatching_emergency_service', 'Dispatching Emergency Service'),
            ('prioritisation_of_emergency_service', 'Prioritisation Of Emergency Service'),
            ('allocating_tasks', 'Allocating Tasks'),
            ('allocation_of_social_benefits', 'Allocation Of Social Benefits'),
            ('reclaiming_public_assistance_services', 'Reclaiming Public Assistance Services'),
            ('granting_public_assistance_service', 'Granting Public Assistance Service'),
            ('reducing_public_assistance_services', 'Reducing Public Assistance Services'),
            ('revoking_public_assistance_services', 'Revoking Public Assistance Services'),
            ('making_prediction', 'Making Prediction'),
            ('predicting_recidivism', 'Predicting Recidivism'),
            ('predicting_occurrence_of_criminal_offence', 'Predicting Occurrence Of Criminal Offence'),
            ('predicting_reoccurrence_of_criminal_offence', 'Predicting Reoccurrence Of Criminal Offence'),
            ('monitoring', 'Monitoring'),
            ('monitoring_employee_behaviour', 'Monitoring Employee Behaviour'),
            ('monitoring_employee_performance', 'Monitoring Employee Performance'),
            ('producing_recommendation', 'Producing Recommendation'),
            ('managing', 'Managing'),
            ('managing_critical_digital_infrastructure', 'Managing Critical Digital Infrastructure'),
            ('managing_road_traffic', 'Managing Road Traffic'),
            ('managing_supply_of_water', 'Managing Supply Of Water'),
            ('managing_supply_of_gas', 'Managing Supply Of Gas'),
            ('managing_supply_of_heating', 'Managing Supply Of Heating'),
            ('managing_supply_of_electricity', 'Managing Supply Of Electricity'),
            ('operating', 'Operating'),
            ('operating_critical_digital_infrastructure', 'Operating Critical Digital Infrastructure'),
            ('operating_road_traffic', 'Operating Road Traffic'),
            ('operating_supply_of_water', 'Operating Supply Of Water'),
            ('operating_supply_of_gas', 'Operating Supply Of Gas'),
            ('operating_supply_of_heating', 'Operating Supply Of Heating'),
            ('operating_supply_of_electricity', 'Operating Supply Of Electricity'),
            ('identifying', 'Identifying'),
            ('health_insurance_risk_assessment', 'Health Insurance Risk Assessment'),
            ('life_insurance_risk_assessment', 'Life Insurance Risk Assessment'),
            ('insurance_pricing', 'Insurance Pricing'),
            ('health_insurance_pricing', 'Health Insurance Pricing'),
            ('life_insurance_pricing', 'Life Insurance Pricing'),
            ('controlling_safety', 'Controlling Safety'),
            ('controlling_safety_of_critical_digital_infrastructure_management', 'Controlling Safety Of Critical Digital Infrastructure Management'),
            ('controlling_safety_of_critical_digital_infrastructure_operation', 'Controlling Safety Of Critical Digital Infrastructure Operation'),
            ('controlling_safety_of_road_traffic_management', 'Controlling Safety Of Road Traffic Management'),
            ('controlling_safety_of_road_traffic_operation', 'Controlling Safety Of Road Traffic Operation'),
            ('controlling_safety_of_supply_of_water_management', 'Controlling Safety Of Supply Of Water Management'),
            ('controlling_safety_of_supply_of_gas_management', 'Controlling Safety Of Supply Of Gas Management'),
            ('controlling_safety_of_supply_of_gas_operation', 'Controlling Safety Of Supply Of Gas Operation'),
            ('controlling_safety_of_supply_of_heating_management', 'Controlling Safety Of Supply Of Heating Management'),
            ('controlling_safety_of_supply_of_heating_operation', 'Controlling Safety Of Supply Of Heating Operation'),
            ('controlling_safety_of_supply_of_electricity_management', 'Controlling Safety Of Supply Of Electricity Management'),
            ('controlling_safety_of_supply_of_electricity_operation', 'Controlling Safety Of Supply Of Electricity Operation'),
            ('detecting_criminal_offences', 'Detecting Criminal Offences'),
            ('investigating_criminal_offences', 'Investigating Criminal Offences'),
            ('prosecuting_criminal_offences', 'Prosecuting Criminal Offences'),
            ('verification_of_migration_seeker_claims', 'Verification Of Migration Seeker Claims'),
            ('performing_background_check', 'Performing Background Check'),
            ('verification_of_asylum_seeker_claims', 'Verification Of Asylum Seeker Claims'),
            ('border_control_security_check', 'Border Control Security Check'),
            ('job_profile_matching', 'Job Profile Matching'),
        ],
        render_kw={"class": "custom-select-lg"},
        default=[]
    )
    domain = SelectMultipleField(
        "Domain", validators=[InputRequired(),], 
        choices = [
            ('critical_infrastructure', 'Critical Infrastructure'),
            ('education', 'Education'),
            ('law_enforcement', 'Law Enforcement'),
            ('employment', 'Employment'),
            ('private_service', 'Private Service'),
            ('public_service', 'Public Service'),
            ('migration', 'Migration'),
            ('asylum', 'Asylum'),
            ('border_control', 'Border Control'),
            ('administration_of_justice', 'Administration Of Justice'),
            ('administration_of_democratic_processes', 'Administration Of Democratic Processes')
        ],
        render_kw={"class": "custom-select-lg"},
        default=[]
    )
    capability = SelectMultipleField(
    "Capability", validators=[InputRequired()],
    choices=[
        ('biometric_identification', 'Biometric Identification'),
        ('remote_biometric_identification', 'Remote Biometric Identification'),
        ('personality_traits_analysis', 'Personality Traits Analysis'),
        ('emotion_recognition', 'Emotion Recognition'),
        ('profiling', 'Profiling'),
        ('face_recognition', 'Face Recognition'),
        ('computer_vision', 'Computer Vision'),
        ('image_recognition', 'Image Recognition'),
        ('automatic_summarisation', 'Automatic Summarisation'),
        ('dialogue_management', 'Dialogue Management'),
        ('information_retrieval', 'Information Retrieval'),
        ('machine_translation', 'Machine Translation'),
        ('named_entity_recognition', 'Named Entity Recognition'),
        ('natural_language_generation', 'Natural Language Generation'),
        ('part_of_speech_tagging', 'Part Of Speech Tagging'),
        ('question_answering', 'Question Answering'),
        ('relationship_extraction', 'Relationship Extraction'),
        ('speech_recognition', 'Speech Recognition'),
        ('speech_synthesis', 'Speech Synthesis'),
        ('pattern_recognition', 'Pattern Recognition'),
        ('action_recognition', 'Action Recognition'),
        ('gesture_recognition', 'Gesture Recognition'),
        ('object_recognition', 'Object Recognition'),
        ('music_information_retrieval', 'Music Information Retrieval'),
        ('sound_event_recognition', 'Sound Event Recognition'),
        ('sound_synthesis', 'Sound Synthesis'),
        ('sound_source_separation', 'Sound Source Separation'),
        ('speaker_recognition', 'Speaker Recognition'),
        ('lie_detection', 'Lie Detection'),
        ('sentiment_analysis', 'Sentiment Analysis')
    ],
    render_kw={"class": "custom-select-lg"},
    default=[]
)

    deployers = StringField("Deployers", validators=[InputRequired()])
    aisubjects = SelectMultipleField(
        "AI Subjects", validators=[InputRequired(),], 
        choices = [
            ('natural_person', 'Natural Person'),
            ('group', 'Group'),
            ('child', 'Child'),
            ('applicant', 'Applicant'),
            ('job_applicant', 'Job Applicant'),
            ('educational_institution_applicant', 'Educational Institution Applicant'),
            ('public_services_applicant', 'Public Services Applicant'),
            ('employee', 'Employee'),
            ('suspect', 'Suspect'),
            ('victim', 'Victim'),
            ('perpetrator', 'Perpetrator'),
            ('test_participant', 'Test Participant'),
            ('asylum_seeker', 'Asylum Seeker'),
            ('citizenship_applicant', 'Citizenship Applicant'),
            ('residence_permit_applicant', 'Residence Permit Applicant'),
            ('visa_applicant', 'Visa Applicant'),
            ('passenger', 'Passenger')
        ],
        render_kw={"class": "custom-select-lg"},
        default=[]
    )
    human_involvement = SelectField(
        "Human Involvement", validators=[InputRequired()],
        choices=[
            ('human_involved', 'Human Involved'),
            ('human_involvement_for_control', 'Human Involvement For Control'),
            ('human_involvement_for_oversight', 'Human Involvement For Oversight'),
            ('human_involvement_for_verification', 'Human Involvement For Verification'),
            ('human_not_involved', 'Human Not Involved')
        ],
        render_kw={"class": "custom-select-sm"},
        default=[]
    )
    level_of_automation = SelectField(
        "Level of Automation", validators=[InputRequired()],
        choices=[
            ('assistive_automation', 'Assistive Automation'),
            ('autonomous', 'Autonomous'),
            ('conditional_automation', 'Conditional Automation'),
            ('full_automation', 'Full Automation'),
            ('high_automation', 'High Automation'),
            ('not_automated', 'Not Automated'),
            ('partial_automation', 'Partial Automation')
        ],
        render_kw={"class": "custom-select-sm"},
        default=[]
    )
    isOrganisational = BooleanField('Are there Organisational measures in place', default=False)
    isTechnical = BooleanField('Are there Technical measures in place', default=False)
    isMonitoring = BooleanField('Are there Monitoring measures in place', default=False)
    isSecurity = BooleanField('Are there Security measures in place', default=False)
    isTransparency = BooleanField('Are there Transparency measures in place', default=False)
    isLogging = BooleanField('Are there Logging measures in place', default=False)
    accuracy = SelectField(
        "Rate the accuracy of your system", validators=[InputRequired()],
        choices=[
            ('1_', '1'),
            ('2_', '2'),
            ('3_', '3'),
            ('4_', '4'),
            ('5_', '5')
        ],
        render_kw={"class": "custom-select-sm"},
        default=[]
    )
    cybersecurity = SelectField(
        "Rate the cybersecurity of your system", validators=[InputRequired()],
        choices=[
            ('1_', '1'),
            ('2_', '2'),
            ('3_', '3'),
            ('4_', '4'),
            ('5_', '5')
        ],
        render_kw={"class": "custom-select-sm"},
        default=[]
    )
    robustness = SelectField(
        "Rate the robustness of your system", validators=[InputRequired()],
        choices=[
            ('1_', '1'),
            ('2_', '2'),
            ('3_', '3'),
            ('4_', '4'),
            ('5_', '5')
        ],
        render_kw={"class": "custom-select-sm"},
        default=[]
    )
    fairness = SelectField(
        "Rate the fairness of your system", validators=[InputRequired()],
        choices=[
            ('1_', '1'),
            ('2_', '2'),
            ('3_', '3'),
            ('4_', '4'),
            ('5_', '5')
        ],
        render_kw={"class": "custom-select-sm"},
        default=[]
    )
    functional = SelectField(
        "Rate the functional adaptabiility of your system", validators=[InputRequired()],
        choices=[
            ('1_', '1'),
            ('2_', '2'),
            ('3_', '3'),
            ('4_', '4'),
            ('5_', '5')
        ],
        render_kw={"class": "custom-select-sm"},
        default=[]
    )
    explainability = SelectField(
        "Rate the explainabillity of your system", validators=[InputRequired()],
        choices=[
            ('1_', '1'),
            ('2_', '2'),
            ('3_', '3'),
            ('4_', '4'),
            ('5_', '5')
        ],
        render_kw={"class": "custom-select-sm"},
        default=[]
    )
    usability = SelectField(
        "Rate the usability of your system", validators=[InputRequired()],
        choices=[
            ('1_', '1'),
            ('2_', '2'),
            ('3_', '3'),
            ('4_', '4'),
            ('5_', '5')
        ],
        render_kw={"class": "custom-select-sm"},
        default=[]
    )
    
    involved_person = StringField('Involved Person', validators=[InputRequired()], render_kw={"class": "form-control"})
    isIntended = BooleanField('Intended', default=False)
    isActive = BooleanField('Active', default=False)
    isInformed = BooleanField('Informed', default=False)
    description = TextAreaField('Description', validators=[InputRequired()], render_kw={"class": "form-control"})
    isPersonalData = BooleanField('Personal Data', default=False)
    personal_category = StringField('Category', validators=[DataRequired()], render_kw={"class": "form-control"})
    isAnonymisedData = BooleanField('Anonymised Data', default=False)
    anonymised_category = StringField('Category', validators=[DataRequired()], render_kw={"class": "form-control"})
    isLisencedData = BooleanField('Lisenced Data', default=False)
    lisenced_category = StringField('Category', validators=[DataRequired()], render_kw={"class": "form-control"})
    data_type = SelectField(
        "Data Type", validators=[InputRequired()],
        choices=[
            ('model', 'Model'),
            ('system', 'System'),
            ('dataset', 'Dataset'),
            ('general purpose', 'General Purpose')
        ],
        render_kw={"class": "custom-select-sm"},
        default=[]
    )
    likelihood = SelectField(
        "Likelihood of Risk", validators=[InputRequired()],
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
            ('very high', 'Very High')
        ],
        render_kw={"class": "custom-select-sm"},
        default=[]
    )
    severity = SelectField(
        "Severity of Risk", validators=[InputRequired()],
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
            ('very high', 'Very High')
        ],
        render_kw={"class": "custom-select-sm"},
        default=[]
    )
    residual = SelectField(
        "Residual Risks", validators=[InputRequired()],
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
            ('very high', 'Very High')
        ],
        render_kw={"class": "custom-select-sm"},
        default=[],
    )
    frequency = StringField('Frequency of Changes', validators=[DataRequired()], render_kw={"class": "form-control"})
    performance = BooleanField('Performace of Changes', default=False)
    risks = BooleanField('Risks of Changes', default=False)
    regulations = TextAreaField('Regulations', validators=[InputRequired()], render_kw={"class": "form-control"})
    standards = TextAreaField('Standards', validators=[InputRequired()], render_kw={"class": "form-control"})
    codes = TextAreaField('Codes of Conduct', validators=[InputRequired()], render_kw={"class": "form-control"})
    key_name = StringField("Name", validators=[InputRequired(), Length(min=2, max=150)])
    data_name = StringField("Name", validators=[InputRequired(), Length(min=2, max=150)])
# 
@app.route('/', methods=['GET', 'POST'])
def index():
    form = AICardsForm(request.form)
    if request.method == "POST" and form.validate():
        # Convert the form data to a dictionary
        result = {key: request.form.getlist(key) for key in request.form.keys()}
        print(result)
        return render_template("results.html.j2", result=result)
    return render_template("home.html.j2", form=form)
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)