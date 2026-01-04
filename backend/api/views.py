from django.shortcuts import render

# api/views.py
import joblib
from rest_framework.decorators import api_view
from rest_framework.response import Response

model = joblib.load("model.pkl")

@api_view(['POST'])
def predict(request):
    value = request.data.get("value")
    prediction = model.predict([[value]])
    return Response({"prediction": prediction[0]})

