error_401 = {
    "schema": {
        "type": "object",
        "properties": {
            "message": {"type": "string", "example": "ForbiddenError"},
            "type": {"type": "string", "example": "FORBIDDEN_ERROR"},
            "success": {"type": "string", "example": False},
        },
    },
    "description": "Forbidden",
}

error_403 = {
    "schema": {
        "type": "object",
        "properties": {
            "message": {"type": "string", "example": "UnauthorizedError"},
            "type": {"type": "string", "example": "UNAUTHORIZED_ERROR"},
            "success": {"type": "string", "example": False},
        },
    },
    "description": "Unauthorized",
}

error_500 = {
    "schema": {
        "type": "object",
        "properties": {
            "message": {"type": "string", "example": "SystemError"},
            "type": {"type": "string", "example": "SYSTEM_ERROR"},
            "success": {"type": "string", "example": False},
        },
    },
    "description": "SystemError",
}
