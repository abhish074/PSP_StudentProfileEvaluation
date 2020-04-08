from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from pspApp.models import StudentProfileModel
from django.contrib.auth.models import User, auth
from pspApp.forms.studentProfileForm import StudentProfileSubmissionForm

from bokeh.plotting import figure
from bokeh.embed import components
# load the model from disk

import pickle
import numpy as np



def viewResult(request):
    undergrad = request.user.undergrad
    if not StudentProfileModel.objects.filter(undergrad=undergrad).exists():
        HttpResponse("No profile exists")
    return render(request,"header.html")


def print_graph(university_list, probabilities_list):
    from bokeh.io import show, output_file
    from bokeh.models import ColumnDataSource, HoverTool
    from bokeh import palettes
    from bokeh.plotting import figure

    output_file("pspApp/templates/universities_result.html")



    source = ColumnDataSource(data=dict(universities=university_list, probabilities=probabilities_list,
                                        color=['red', 'green', 'blue', 'pink', 'purple', 'yellow', 'grey',
                                               'orange', 'brown', 'black']))

    p = figure(x_range=university_list, y_range=(0,2),plot_width = 1200 ,plot_height=400, title="University Prediction",
               toolbar_location=None, tools="")
    p.vbar(x='universities', top='probabilities', width=0.9, color='color',  source=source)
    p.add_tools(HoverTool(tooltips=[('probabilities','@probabilities')]))

    p.xgrid.grid_line_color = None
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    p.xaxis.axis_label_text_font_size = "5pt"
    p.xaxis.axis_label_text_font_style = 'bold'

    # show(p)

    script , div = components(p)
    return script, div, p

def PredictionView(request):
    filename = 'pspApp/static/naive_bayes_model/finalized_naive_bayes_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))



    """
    Here we are using values for the university names.
    Below step is used to achieve one hot encoding.
    
    """
    university_mapper = {"University Of Alberta": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                         "University of British Columbia": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                         "Carleton University": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         "Simon Faser University": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                         "University of Regina": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                         "University of Ottawa": [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                         "Victoria University": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                         "University of Toronto": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                         "Waterloo University": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         "Western Ontario University": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         }

    university_list = []
    probabilities_list = []
    prediction_list = []
    print("inside prediction view")

    name = request.user.username

    try:
        results = StudentProfileModel.objects.get(name=name)
    except Exception:
        return render(request, "profileDoesNotExist.html")


    print("results:--", results)
    print(results.name, results.workex)

    def predict(custom_data):
        print(custom_data)
        # custom_data_x = sc.transform(custom_data)
        custom_data_x = custom_data
        print("custom_data_x:-----", custom_data_x)
        prediction = loaded_model.predict(custom_data_x)
        print("predicted_value:----", prediction)
        proba = loaded_model.predict_proba(custom_data_x)
        probability = proba[:, 1]
        print("percentage_chance: ", probability)

        probabilities_list.append(proba[:, 1])
        prediction_list.append(prediction)
        university_list.append(key)


    """
    The following is to handle the categorical data.
    User paper published for international, national or did not publish paper at all
    """
    paper_list = []
    if results.paper == "International":
        paper_list = [1, 0, 0]
    elif results.paper == "National":
        paper_list = [0, 1, 0]
    else:
        print(results.paper)
        print(type(results.paper))
        paper_list = [0, 0, 1]


    model_data = [results.gre, results.workex, results.undergrad, results.quants, results.verbal, results.ielts,
                   results.toefl]

    custom_data = []
    custom_data.extend(paper_list)
    custom_data.extend(model_data)

    print("----------------------------------------------")
    print("custom_data:---", custom_data)
    print("------------------------------------------------")

    for key, value in university_mapper.items():
        print(key, value)
        univeristy_custom_data = value
        univeristy_custom_data.extend(custom_data)
        print(univeristy_custom_data)
        univeristy_custom_data = np.array(list(univeristy_custom_data)).reshape(1, -1)

        predict(univeristy_custom_data)

    script, div, p = print_graph(university_list, probabilities_list)

    return render(request, "boekh_chart_within_html.html", {'script':script , 'div': div})



