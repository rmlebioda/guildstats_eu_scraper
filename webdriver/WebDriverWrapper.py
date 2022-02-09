from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from models.boss_data import BossData, BossChances


class WebDriverWrapper:
    webdriver: WebDriver = None
    worlds: list[str] = None

    __guildstats_url = 'https://guildstats.eu'
    __guildstats_ep_worlds = '/worlds'
    __guildstats_ep_bosses = '/bosses'

    __guildstats_worlds_tdservername_xpath = '''//div[@class='starter-template']/table/tbody/tr/td[2]'''
    __guildstats_boss_spawnrate_xpath = '''//div[@class='starter-template']/div/div[@class='news'][2]/div[@class='row'][1]/div[@class='col-12'][2]/div/div[2]/div/div/div[2]/div/h5/b'''
    __guildstats_boss_lastseen_xpath = '''//div[@class='starter-template']/div/div[@class='news'][2]/div[@class='row'][1]/div[@class='col-12'][2]/div/div[1]/div/div/div[2]/div/h5'''
    __guildstats_boss_lastupdate_xpath = '''//div[@class='news']/div/span'''

    def __init__(self, _webdriver):
        self.webdriver = _webdriver

    def get_boss_data(self, boss_name: str, worlds: list[str] = None) -> list[BossData]:
        if worlds is None:
            self.__init_worlds()
            worlds = self.worlds
        return [self.__get_boss_data(boss_name, world) for world in worlds]

    def __get_boss_data(self, boss_name: str, world: str) -> BossData:
        self.webdriver.get(self.__get_boss_url(boss_name, world))
        return BossData(
            name=boss_name,
            data=BossChances(
                world=world,
                chances=self.webdriver.find_element(By.XPATH, self.__guildstats_boss_spawnrate_xpath).text,
                last_seen=self.webdriver.find_element(By.XPATH, self.__guildstats_boss_lastseen_xpath).text,
                last_update=self.webdriver.find_element(By.XPATH, self.__guildstats_boss_lastupdate_xpath).get_attribute('data-content')
            ))

    def _goto_worlds(self):
        self.webdriver.get(self.__guildstats_url + self.__guildstats_ep_worlds)

    def __get_boss_url(self, boss_name: str, world: str = None):
        world = None if world is None else world
        if world is not None:
            world = f'world={world}&'
        return f'{self.__guildstats_url}{self.__guildstats_ep_bosses}?{world}monsterName={boss_name}'

    def __fetch_worlds(self):
        self._goto_worlds()
        elements: list[WebElement] = self.webdriver.find_elements(By.XPATH, self.__guildstats_worlds_tdservername_xpath)
        self.worlds = list(map(lambda x: x.text, elements))

    def __init_worlds(self, override_existing_worlds: bool = False):
        if override_existing_worlds or self.worlds is None:
            self.__fetch_worlds()
