class IngredientConverter:
    def __init__(self, args):
        self.ingredients = args

    @property
    def convert_data(self):
        data = []
        converter = {
            'quantity': 0,
            'type': "",
            'extra': ""
        }
        extra = ""
        for i in self.ingredients:
            split_data = i.split(" ")
            try:
                qty = int(split_data[0])
            except:
                if split_data[0] == '¼' or split_data[0] == "1/4":
                    qty = 0.25
                elif split_data[0] == '½' or split_data[0] == "1/2":
                    qty = 0.5
                elif split_data[0] == '¾' or split_data[0] == "3/4":
                    qty = 0.75
                elif split_data[0] == '⅓' or split_data[0] == "1/3":
                    qty = 0.67
                else:
                    split = split_data[0].split("")
                    try:
                        qty = int(split[0])
                        if len(split) > 2:
                            splits = ""
                            for j in range(1, len(split)):
                                splits += split[j]
                                if splits == '¼' or splits == "1/4":
                                    qty += 0.25
                                elif splits == '½' or splits == "1/2":
                                    qty += 0.5
                                elif splits == '¾' or splits == "3/4":
                                    qty += 0.75
                                elif splits == '⅓' or splits == "1/3":
                                    qty += 0.67
                        else:
                            if split[1] == '¼':
                                qty += 0.25
                            elif split[1] == '½':
                                qty += 0.5
                            elif split[1] == '¾':
                                qty += 0.75
                            elif split[1] == '⅓':
                                qty += 0.67
                    except:
                        qty = -1
            converter['quantity'] = qty
            converter['type'] = split_data[1]
            for k in range(2, len(split_data)):
                extra += (split_data[k] + " ")
            converter['extra'] = extra
            data.append(converter)
            extra = ""
            converter = {
                'quantity': 0,
                'type': "",
                'extra': ""
            }

        return data


print(IngredientConverter([
    "¼ cup butter, divided",
    "2 cups all-purpose flour",
    "2 tablespoons white sugar",
    "2 teaspoons baking powder",
    "1 teaspoon salt",
    "3 tablespoons butter, softened",
    "¾ cup milk",
    "1 egg",
    "½ cup white sugar",
    "½ cup brown sugar",
    "1 tablespoon ground cinnamon",
    "1 cup confectioners' sugar",
    "4 ounces cream cheese, softened",
    "¼ cup butter, softened",
    "½ teaspoon vanilla extract"
]).convert_data)