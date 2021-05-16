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

            if split_data[1] == "cup" \
                    or split_data[1] == "cups" \
                    or split_data[1] == "teaspoon" \
                    or split_data[1] == "teaspoons" \
                    or split_data[1] == "tablespoons" \
                    or split_data[1] == "tablespoon" \
                    or split_data[1] == "ounce" \
                    or split_data[1] == "ounces":
                converter['type'] = split_data[1]
                for k in range(2, len(split_data)):
                    extra += (split_data[k] + " ")
                converter['extra'] = extra
            else:
                converter['type'] = "other"
                for k in range(1, len(split_data)):
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
