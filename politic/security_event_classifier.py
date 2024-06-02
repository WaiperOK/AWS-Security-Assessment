
import logging
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline

logger = logging.getLogger(__name__)

def train_classifier(event_data):
    texts, labels = zip(*event_data)
    model = make_pipeline(TfidfVectorizer(), RandomForestClassifier())
    model.fit(texts, labels)
    return model

def classify_events(events, model):
    predictions = model.predict(events)
    return predictions
