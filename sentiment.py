
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client_m = authenticate_client()

def sentiment_analysis_example(client_m):

    documents = [
    {"id": "1", "language": "ko", "text": "아침에 일어나니까 힘들다"},
   
]
    response = client_m.analyze_sentiment(documents=documents)[0]
   
    print(response.sentiment)
    print(response.confidence_scores.positive)
    print(response.confidence_scores.neutral)
    print(response.confidence_scores.negative)
    
          
sentiment_analysis_example(client_m)