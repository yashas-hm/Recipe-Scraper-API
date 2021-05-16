from recipe_scrapers import scrape_me


class Scraper:
    def __init__(self, web_url):
        self.web_url = web_url
        self.scraper = scrape_me(web_url)

    def get_title(self):
        return self.scraper.title()

    def get_prep_time(self):
        return self.scraper.total_time()[0]

    def get_cook_time(self):
        return self.scraper.total_time()[1]

    def get_servings(self):
        return int(self.scraper.yields().split(" ")[0])

    def get_image_url(self):
        return self.scraper.image()

    def get_ingredients(self):
        return self.scraper.ingredients()

    def get_instructions(self):
        return self.scraper.instructions().split("\n")

    def print_all(self):
        print(self.get_title(), end='\n')
        print(self.get_prep_time(), end='\n')
        print(self.get_cook_time(), end='\n')
        print(self.get_servings(), end='\n')
        print(self.get_instructions(), end='\n')
        print(self.get_ingredients(), end='\n')
