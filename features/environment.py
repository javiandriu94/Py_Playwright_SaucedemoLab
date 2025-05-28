from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

def before_all(context):
    load_dotenv()  # Carga las variables del archivo .env

    context.username = os.getenv("SAUCE_USERNAME")
    context.password = os.getenv("SAUCE_PASSWORD")

     # Product names
    context.product_1 = os.getenv("PRODUCT_1")
    context.product_2 = os.getenv("PRODUCT_2")
    
     # Checkout info
    context.first_name = os.getenv("FIRST_NAME")
    context.last_name = os.getenv("LAST_NAME")
    context.postal_code = os.getenv("POSTAL_CODE")

    playwright = sync_playwright().start()
    context.browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context.playwright = playwright

def after_all(context):
    context.browser.close()
    context.playwright.stop()