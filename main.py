from selenium import webdriver

from webdriver.WebDriverWrapper import WebDriverWrapper

if __name__ == '__main__':
    yetis_worlds = ["Adra", "Antica", "Bona", "Celesta", "Damora", "Famosa", "Harmonia", "Karna",
              "Marcia", "Monza", "Olima", "Peloria", "Refugia", "Secura", "Suna", "Thyria", "Vunira"]
    ocyakao_worlds = ['Antica', 'Bona', 'Celesta', 'Damora', 'Famosa', 'Harmonia', 'Monza',
                'Peloria', 'Premia', 'Refugia', 'Secura', 'Suna', 'Thyria', 'Vunira']

    print("Starting...")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    webdriver = webdriver.Chrome(options=chrome_options)

    wrapper = WebDriverWrapper(webdriver)

    bosses = wrapper.get_boss_data('yetis', worlds=yetis_worlds)
    bosses += wrapper.get_boss_data('Ocyakao', worlds=ocyakao_worlds)

    bosses.sort(key=lambda x: (x.name, x.data.get_chances_text_value(), x.data.get_chances(), x.data.last_seen_days()), reverse=True)

    for boss in bosses:
        print(boss)

