from ..models.user import User, ShortUser
from typing import List
from json import load
from fastapi import HTTPException
from ..database.pymongo_users import get_user_by_id, get_user_by_email
from ..database.pymongo_manga import get_manga_by_id, get_all_manga, insert_manga, update_manga
from ...Asura.asura_manga_scraper import AsuraScraper
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

class MangaService:

    @staticmethod
    async def get_manga_data():
        try:
            manga_list = get_all_manga()
            return manga_list
        except Exception as e:
            raise Exception('Unable to load the asura mangas:', str(e))

    @staticmethod
    async def start_polling():
        try:
            """
            scheduler = AsyncIOScheduler()  # Create a scheduler instance

            # Add a job to the scheduler that runs the scraper every 2 hours
            scheduler.add_job(MangaService.run_scraper, 'interval', hours=2)

            scheduler.start()  # Start the scheduler
            asyncio.get_event_loop().run_forever()  # Run the event loop continuously
            """
            print("Scheduler started successfully.")
            return await AsuraScraper()

        except Exception as e:
            raise Exception('Unable to start polling:', str(e))

    @staticmethod
    async def run_scraper():
        try:
            manga_list = await MangaService.get_asura_mangas()
            print("Manga list updated:", manga_list)
        except Exception as e:
            print('Error in scraper:', str(e))
"""
# Add this block to execute the periodic task
if __name__ == "__main__":
    MangaService.start_polling()
"""