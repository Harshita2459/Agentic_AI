# backend/utils/helpers.py
import datetime

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")
