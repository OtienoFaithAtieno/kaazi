#code below launches the browser, navigates to the job url page and allowuser to submit application

from playwright.sync_api import sync_playwright #function used for browser automation

def apply_to_job(job, profile):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(job["url"])

        # NOTE: This is generic — real sites need custom selectors
        try:
            page.fill("input[name='name']", "Your Name")
            page.fill("input[name='email']", "your@email.com")
        except:
            pass

        input("Press ENTER to submit manually...")

        browser.close()