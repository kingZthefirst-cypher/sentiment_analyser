from typing import Callable
from rest_framework.views import APIView
from rest_framework.response import Response
import flair

# Create your views here.


def init_sentiment_analyser() -> Callable[[str], int]:
    flair_sentiment = flair.models.TextClassifier.load("en-sentiment")

    def sentiment_analyser(text: str) -> int:
        try:
            s = flair.data.Sentence(text)
            flair_sentiment.predict(s)
            label, score = s.labels[0].value, s.labels[0].score
            if label == "NEGATIVE":
                score = -score
            return int(round(score, 2) * 100)
        except Exception as e:
            return 0

    return sentiment_analyser


sentiment_analyser = init_sentiment_analyser()


class SentimentAnalyserAPI(APIView):
    def post(self, request, format=None):
        text = request.data.get("text", "")
        sentiment = sentiment_analyser(text)
        return Response({"text": text, "sentiment": sentiment,})
