import os

from Twitter_Sentiment_Analysis_Django.settings import BASE_DIR
CWD=os.path.dirname(os.path.realpath(__file__))
CLEANED_CSV=CWD+"\\CleanedCSV"
DOWNLOAD_CSV=CWD+"\\CSV_Files"
BAR_CHART=BASE_DIR+"\\Twitter_Django\\static\\Twitter_Django\\Graph\\Bargraph"
PIE_CHART=BASE_DIR+"\\Twitter_Django\\static\\Twitter_Django\\Graph\\Piechart"
POLARITY_CSV=CWD+"\\Polarity CSV"
WORD_CLOUD=BASE_DIR+"\\Twitter_Django\\static\\Twitter_Django\\Graph\\Wordcloud"
IMG=BASE_DIR+"\\Twitter_Django\\static\\Twitter_Django\\img"