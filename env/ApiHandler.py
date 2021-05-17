from env.RecipeScraper import Scraper
from flask import Flask
from flask_restful import Resource, Api, reqparse
from env.IngredientConverter import IngredientConverter

app = Flask(__name__)
api = Api(app)


class ApiHandler(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('webUrl', required=True)
        args = parser.parse_args()
        data = {
            'success': False,
            'message': '',
            'data': {}
        }
        try:
            scraper = Scraper(args['webUrl'])
            ingredients = IngredientConverter(scraper.get_ingredients())
            scraped_data = [
                ('title', scraper.get_title()),
                ('prepTime', scraper.get_prep_time()),
                ('cookTime', scraper.get_cook_time()),
                ('servings', scraper.get_servings()),
                ('imageUrl', scraper.get_image_url()),
                ('instructions', scraper.get_instructions()),
                ('ingredients', ingredients.convert_data)
            ]
            data['success'] = True
            data['message'] = 'Success'
            data['data'].update(scraped_data)
            return data, 200
        except:
            data['success'] = False
            data['message'] = 'Invalid Url'
            return data, 400

    pass


api.add_resource(ApiHandler, "/CookEezy/recipeFromUrl")
