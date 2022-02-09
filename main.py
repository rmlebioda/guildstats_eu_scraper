from selenium import webdriver

from webdriver.WebDriverWrapper import WebDriverWrapper

if __name__ == '__main__':
    worlds = ["Adra", "Antica", "Bona", "Celesta", "Damora", "Famosa", "Harmonia", "Karna",
              "Marcia", "Monza", "Olima", "Peloria", "Refugia", "Secura", "Suna", "Thyria", "Vunira"]

    print("Starting...")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    webdriver = webdriver.Chrome(options=chrome_options)

    wrapper = WebDriverWrapper(webdriver)

    bosses = wrapper.get_boss_data('yetis', worlds=worlds)

    bosses.sort(key=lambda x: x.data.extract_chances(), reverse=True)

    for boss in bosses:
        print(boss)

