from apps.ultis.docs import error_401, error_403, error_500

post_login = {
    "parameters": [
        {
            "required": True,
            "in": "body",
            "name": "body",
            "schema": {
                "required": ["email"],
                "id": "Product",
                "properties": {
                    "email": {
                        "default": "Guarana",
                        "type": "string",
                        "description": "The product's name.",
                    }
                },
            },
        }
    ],
    "responses": {
        # "200": users_schema.dump({}),
        # "200": {
        #   "schema": {
        #     "$ref": "#/definitions/Palette"
        #   },
        #   "examples": {
        #     "rgb": [
        #       "red",
        #       "green",
        #       "blue"
        #     ]
        #   },
        #   "description": "A list of colors (may be filtered by palette)"
        # },
        "500": error_500,
    },
}
