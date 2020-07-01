from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from app import scraperAnalyserAPI

def start():
    scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
    scheduler.add_job(scraperAnalyserAPI.update, 'cron', minute=15)
    scheduler.start()