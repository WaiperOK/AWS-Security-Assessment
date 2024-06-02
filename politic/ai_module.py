import logging
from datetime import datetime
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

logger = logging.getLogger(__name__)


def preprocess_logs(log_messages):
    log_data = []
    for log in log_messages:
        if "Recommendation:" in log:
            parts = log.split(". Recommendation: ")
            if len(parts) == 2:
                log = parts[0]
        parts = log.split(" ", 3)
        if len(parts) < 4:
            logger.error(f"Log entry does not contain enough parts: {log}")
            continue
        timestamp = parts[0]
        level = parts[1].strip('[]')
        message = parts[2] + " " + parts[3]
        try:
            features = extract_features(timestamp, level, message)
            log_data.append(features)
        except Exception as e:
            logger.error(f"Failed to parse log: {log}, error: {e}")
    return log_data


def extract_features(timestamp, level, message):
    try:
        timestamp_numeric = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S').timestamp()
    except ValueError:
        timestamp_numeric = datetime.now().timestamp()  # Используем текущее время, если временная метка некорректна
    level_numeric = {'INFO': 0, 'WARNING': 1, 'ERROR': 2}.get(level, 0)

    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(message)

    features = [
        timestamp_numeric,
        level_numeric,
        sentiment_scores['compound'],
        sentiment_scores['pos'],
        sentiment_scores['neu'],
        sentiment_scores['neg']
    ]
    return features


def analyze_logs_for_anomalies(log_messages):
    log_data = preprocess_logs(log_messages)
    if not log_data:
        logger.error("No valid log data to analyze")
        return

    log_data = np.array(log_data)
    if log_data.ndim == 1:
        log_data = log_data.reshape(-1, 1)
    model = IsolationForest(contamination=0.1)
    model.fit(log_data)
    predictions = model.predict(log_data)

    for i in range(len(predictions)):
        if predictions[i] == -1:
            logger.warning(f"Anomalous log detected: {log_messages[i]}")

    plot_event_classification(predictions)


def plot_event_classification(predictions):
    classes = ['Normal', 'Anomalous']
    counts = [np.sum(predictions == 1), np.sum(predictions == -1)]

    plt.figure(figsize=(10, 6))
    plt.bar(classes, counts, color=['blue', 'red'])
    plt.xlabel('Event Classification')
    plt.ylabel('Count')
    plt.title('Event Classification Counts')
    plt.savefig('event_classification_counts.png')  # Сохранение графика в файл
    plt.show()
