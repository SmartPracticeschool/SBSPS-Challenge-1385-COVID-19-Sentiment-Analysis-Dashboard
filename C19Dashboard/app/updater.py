from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from app import scraperAnalyserAPI

def start():
    scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
    scheduler.add_job(scraperAnalyserAPI.update, 'cron', hour=1, minute=30) # https://www.worldtimebuddy.com/ist-to-cdt-converter
    scheduler.start()