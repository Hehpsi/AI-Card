from flask import Flask, render_template, request
from wtforms import Form, StringField, validators, SelectMultipleField, widgets
from wtforms.widgets import TextArea

app = Flask(__name__)

class AICardsForm(Form):
    version = StringField("Version", validators=[validators.InputRequired(), validators.Length(min=4, max=5)])
    aiTechniques = SelectMultipleField(
        "AI Techniques", validators=[validators.InputRequired(),], 
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
       
    )
    providers = StringField("Provider(s)", validators=[validators.InputRequired(), validators.Length(min=4, max=150)])
    developers = StringField("Developer(s)", validators=[validators.InputRequired(), validators.Length(min=4, max=150)])
    purpose = StringField("Purpose", validators=[validators.InputRequired()], widget=TextArea())
    domain = StringField("Domain", validators=[validators.InputRequired(), validators.Length(min=4, max=150)])
    capability = StringField("Capability", validators=[validators.InputRequired()], widget=TextArea())
    deployers = StringField("Depolyer", validators=[validators.InputRequired()], widget=TextArea())
    aisubjects = StringField("AI Subjects", validators=[validators.InputRequired(), validators.Length(min=4, max=150)])

@app.route("/", methods=["GET", "POST"])
def index():
    form = AICardsForm(request.form)
    if request.method=="POST":
        print(form.version.data)
    return render_template("home.html.j2", form=form)

app.run(host="0.0.0.0", port=5001, debug=True)