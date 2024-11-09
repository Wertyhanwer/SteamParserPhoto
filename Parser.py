import requests
from bs4 import BeautifulSoup


class GetDocResponseError(Exception):
    pass


# STATIC_CLASS!!!!!
class Parser:
    @staticmethod
    def page_counter(url: str):
        response = requests.get(url)

        if response.status_code == 200:
            page_content = response.text
            response.encoding = "UTF-8"
            soup = BeautifulSoup(page_content, 'html.parser')
            pages = soup.find_all("a", {"class": "pagingPageLink"})
            pages_info_lst = [int(page.getText()) for page in pages]
            if pages_info_lst:
                page_count = max(pages_info_lst)
                return page_count
            return 1

        else:
            raise (GetDocResponseError
                   (f"Не удалось получить данные. Статус код: {response.status_code}"))

    @staticmethod
    def photo_from_url(photo_url: str):
        response = requests.get(photo_url)

        if response.status_code == 200:
            return response

        else:
            raise (GetDocResponseError
                   (f"Не удалось получить данные. Статус код: {response.status_code}"))

    @staticmethod
    def get_parce_info(url: str, our_object: str, attrs: dict = None):
        """
        Находение искомого объекта путём передачи искомого элемента с возможнутью добавления условий в виде словаря.
        Пример аргументов: 'p', attrs={'class': 'example'}
        """

        response = requests.get(url)

        if response.status_code == 200:
            page_content = response.text
            response.encoding = "UTF-8"
            soup = BeautifulSoup(page_content, 'html.parser')

            if attrs is None:
                headers = soup.find_all(our_object)
            else:
                headers = soup.find_all(our_object, attrs)

            # print(headers)
            return headers
        else:
            raise (GetDocResponseError
                   (f"Не удалось получить данные. Статус код: {response.status_code}"))
