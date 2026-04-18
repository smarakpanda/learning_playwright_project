def launch_browser(playwright, browser_name, headless):
    browser = browser_name.lower()
    if browser == "chromium":
        return playwright.chromium.launch(headless=headless,args=["--start-maximized", "--window-size=1920,1080"])
    elif browser == "firefox":
        return playwright.firefox.launch(headless=headless)
    elif browser == "edge":
        return playwright.chromium.launch(channel="msedge", headless=headless,args=["--start-maximized", "--window-size=1920,1080"])
    else:
        raise ValueError(f"unsupported browser: {browser}")
