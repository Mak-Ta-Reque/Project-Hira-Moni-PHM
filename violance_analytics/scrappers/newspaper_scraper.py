import datetime


class NewsPaperScraperInterface:

    def load_data_source(self, url: str) -> bool:
        """
        :param url: web address of website
        :return:true if the website exist/ false if dont exist
        """
        """Load the file from the url for extracting text."""
        pass

    def scrap(self, keyword: str, date: datetime) -> list:
        """
        :param keyword: rape
        :param date:
        :return:
        """
        """Scrap the website and return a list of events based on a specific input date
        Each event is a dictionary
        {victim_name:str, age: int, location: str, profession: str, culprit: list}
        culprit:[{name:str, age:str, profession:},{},{}]
        culprit is list because they can be many or one.

        """
        pass

    def scrap(self, keyword: str, start_date: datetime, end_date: datetime) -> list:
        """
        :param keyword: 'rape'
        :param start_date:
        :param end_date:
        :return:
        """
        """Scrap the website and return a list of events based on a specific input date
        Each event is a dictionary
        {victim_name:str, age: int, location: str, profession: str, culprit: list}
        culprit:[{name:str, age:str, profession:},{},{}]
        culprit is list because they can be many or one.

        """
        pass



