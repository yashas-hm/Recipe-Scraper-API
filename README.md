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
    "title": "Orange Cake with Semolina and Almonds",
    "prepTime": 30,
    "cookTime": 80,
    "servings": 10,
    "imageUrl": "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F4674336.jpg",
    "instructions": [
      "Combine chopped oranges and 1 tablespoon water in a small saucepan, cover, and cook over medium-low heat until oranges are soft and excess liquid has evaporated, about 30 minutes. Set aside to cool, about 20 minutes.",
      "Preheat oven to 350 degrees F (175 degrees C). Line the bottom and sides of an 8-inch springform pan with parchment paper.",
      "Place oranges in the bowl of a food processor; pulse until finely chopped.",
      "Beat egg whites in a glass, metal, or ceramic bowl until stiff peaks form. Gradually add 1/2 cup sugar, continuing to beat for 1 more minute.",
      "Beat egg yolks and remaining 1/2 cup sugar in a separate bowl until pale and thick, 2 to 3 minutes. Whisk in finely chopped oranges. Fold in ground almonds, semolina, vanilla extract, and fiori di Sicilia. Stir in 3 spoonfuls of whisked egg white to loosen the batter. Gently fold in remaining egg whites with a spatula or large metal spoon. Pour batter into prepared springform and level the top.",
      "Bake in the preheated oven until cake is golden and a skewer inserted in the center comes out clean, about 50 minutes. Check cake after 20 and 30 minutes to see if it is starting to brown too quickly. Cover top lightly with aluminum foil once cake starts to brown.",
      "Remove from oven and cool in the pan. Remove ring, peel away parchment paper and transfer cake to a serving plate. Drizzle with liqueur and dust with confectioners' sugar."
    ],
    "ingredients": [
      {
        "quantity": 2,
        "type": "other",
        "extra": "large organic oranges, scrubbed and coarsely chopped (with the skin) "
      },
      {
        "quantity": 5,
        "type": "other",
        "extra": "eggs, separated "
      },
      {
        "quantity": 1,
        "type": "cup",
        "extra": "white sugar, divided "
      },
      {
        "quantity": 0.75,
        "type": "cup",
        "extra": "ground almonds "
      },
      {
        "quantity": 0.75,
        "type": "cup",
        "extra": "semolina flour "
      },
      {
        "quantity": 0.5,
        "type": "teaspoon",
        "extra": "vanilla extract "
      },
      {
        "quantity": 0.5,
        "type": "teaspoon",
        "extra": "fiori di Sicilia (optional) "
      },
      {
        "quantity": 3,
        "type": "tablespoons",
        "extra": "brandy-based orange liqueur (such as Grand Marnier®) "
      },
      {
        "quantity": 0.5,
        "type": "teaspoon",
        "extra": "confectioners' sugar "
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
