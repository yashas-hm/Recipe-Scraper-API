# Recipe Scraper API

Simple API for fetching recipes from web using URL<br>

## Requirements
 - Flask 1.1.2 (pip install Flask==1.1.2)
 - recipe_scrapers (modified an original code from https://github.com/hhursev/recipe-scrapers.git) 
 - Flask_RESTful (pip install Flask-RESTful)

## End Points
POST<br>
API -> http://127.0.0.1:5000/CookEezy/recipeFromUrl?webUrl="PASTE_URL_HERE"><br>

### Result

Test API POST -> http://127.0.0.1:5000/CookEezy/recipeFromUrl?webUrl=https://www.allrecipes.com/recipe/241917/quick-cinnamon-rolls/<br>

```json
{
  "success": true,
  "message": "Success",
  "data": {
    "title": "Quick Cinnamon Rolls",
    "prepTime": 20,
    "cookTime": 20,
    "servings": 18,
    "imageUrl": "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F7535189.jpg",
    "instructions": [
      "Preheat oven to 400 degrees F (200 degrees C). Brush a 9-inch square baking dish with 2 tablespoons melted butter.",
      "Whisk flour, 2 tablespoons white sugar, baking powder, and salt together in a large bowl. Work 3 tablespoons softened butter into flour mixture using your hands. Beat milk and egg together in another bowl; pour into flour-butter mixture and stir with a rubber spatula until a soft dough forms.",
      "Turn dough out onto a floured work surface and roll dough into a 1/4-inch thick rectangle. Brush surface of dough with 2 tablespoons melted butter.",
      "Whisk 1/2 cup white sugar, brown sugar, and cinnamon together in a small bowl. Sprinkle 1/2 of the cinnamon sugar mixture in the bottom of the prepared baking dish. Sprinkle remaining cinnamon sugar over butter-brushed dough. Roll dough around filling to form a log; cut log into 18 rolls and place rolls in the prepared baking dish.",
      "Bake in the preheated oven until rolls are set, 20 to 25 minutes.",
      "Beat confectioners' sugar, cream cheese, 1/4 cup softened butter, and vanilla extract together in a bowl until frosting is smooth. Top hot cinnamon rolls with cream cheese frosting."
    ],
    "ingredients": [
      {
        "quantity": 0.25,
        "type": "cup",
        "extra": "butter, divided "
      },
      {
        "quantity": 2,
        "type": "cups",
        "extra": "all-purpose flour "
      },
      {
        "quantity": 2,
        "type": "tablespoons",
        "extra": "white sugar "
      },
      {
        "quantity": 2,
        "type": "teaspoons",
        "extra": "baking powder "
      },
      {
        "quantity": 1,
        "type": "teaspoon",
        "extra": "salt "
      },
      {
        "quantity": 3,
        "type": "tablespoons",
        "extra": "butter, softened "
      },
      {
        "quantity": 0.75,
        "type": "cup",
        "extra": "milk "
      },
      {
        "quantity": 1,
        "type": "other",
        "extra": "egg "
      },
      {
        "quantity": 0.5,
        "type": "cup",
        "extra": "white sugar "
      },
      {
        "quantity": 0.5,
        "type": "cup",
        "extra": "brown sugar "
      },
      {
        "quantity": 1,
        "type": "tablespoon",
        "extra": "ground cinnamon "
      },
      {
        "quantity": 1,
        "type": "cup",
        "extra": "confectioners' sugar "
      },
      {
        "quantity": 4,
        "type": "ounces",
        "extra": "cream cheese, softened "
      },
      {
        "quantity": 0.25,
        "type": "cup",
        "extra": "butter, softened "
      },
      {
        "quantity": 0.5,
        "type": "teaspoon",
        "extra": "vanilla extract "
      }
    ]
  }
}
```
<br>

Test API POST -> http://127.0.0.1:5000/CookEezy/recipeFromUrl?webUrl=htt<br>

```json
{
    "success": false,
    "message": "Invalid Url",
    "data": {}
}
```
