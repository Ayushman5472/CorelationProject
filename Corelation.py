import numpy as np
import csv
import plotly.express as px

def Corelation(dataLocation):
    marks = []
    daysPresent = []
    with open(dataLocation) as L:
        df = csv.DictReader(L)
        for row in df:
            marks.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
    return {'x':marks, 'y': daysPresent}

def findCorelation(data):
    Corelation = np.corrcoef(data["x"], data['y'])
    print(Corelation)

data = Corelation("data1.csv")

findCorelation(data)