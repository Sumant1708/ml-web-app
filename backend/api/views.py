import os
import joblib
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

BASE_DIR = settings.BASE_DIR

MODEL_PATH = os.path.join(BASE_DIR, 'api', 'model.pkl')
model = joblib.load(MODEL_PATH)

@csrf_exempt
@api_view(['POST'])
def predict(request):
    value = request.data.get("value")
    prediction = model.predict([[value]])
    return Response({"prediction": prediction[0]})
