from Parser import Parser
from PhotoSaver import PhotoSaver


STEAM_PHOTO_URL = '''https://steamcommunity.com/sharedfiles/filedetails/?id='''
STEAM_PHOTO_TECHNICAL = '''?imw=5000&imh=5000'''


def main():
    get_parce_info = Parser.get_parce_info
    photo_from_url = Parser.photo_from_url
    save_photo = PhotoSaver.save_photo
    url = input("Введите ссылку для парсинга (если страниц несколько, то обязательно ссылка первой): ")
    pages_count = Parser.page_counter(url)
    for i in range(1, pages_count+1):
        url = url.split("/")
        url = '/'.join(url[:-1]) + "/" + f"?p={i}" + url[-1]

        print(f"Начинаю загрузку {i} страницы!")
        main_divs = []
        while not main_divs:
            main_divs = get_parce_info(url, "div", {"class": "imgWallHover"})
        for mainDiv in main_divs:
            main_div_id = mainDiv.get("id")[12:]
            photo_url = get_parce_info(STEAM_PHOTO_URL + main_div_id, "img", {"id": "ActualMedia"})[0].get("src")
            photo_url = photo_url.split("/")
            photo_url = "/".join(photo_url[:-1]) + "/" + STEAM_PHOTO_TECHNICAL
            photo_data = photo_from_url(photo_url)
            # print(photo_url)
            save_photo(photo_data,  main_div_id)

        print(f"Страница {i} была сохранена!")


if __name__ == '__main__':
    main()
