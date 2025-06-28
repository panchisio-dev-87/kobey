def get_password_by_name(name):
    companies = company_list_DZ()
    for company in companies:
        if company["name"] == name:
            return company["password"]
    return None  # Retorna None si no encuentra el nombre


def company_directa():
    return [
        {
            "name":"PRONACA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        }
    ]

def company_group_1():
    return [
        {
            "name":"PRONACA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        }
    ]


def company_single(name):
    return [
        {
            "name":name,
            "user":"SoporteBZ",
            "password": get_password_by_name(name)
        }
    ]

def company_list_DZ():
    return [
        {
            "name":"POSSO_CUEVA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"ECOAL",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"CENACOP",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISPROALZA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"JUDISPRO",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"MADELI",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"SKANDINAR",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"PRONACA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISMAG",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DIMMIA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISPROVALLES",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"PROORIENTE",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"ALSODI",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"GRAMPIR",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"ALMABI",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISANAHISA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"APRONAM",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISPROLOP",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISCARNICOS",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"GARVELPRODUCT",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"PATRICIO_CEVALLOS",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"PAUL_FLORENCIA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        }
    ]


def company_list_solo_DZ():
    return [
        {
            "name":"POSSO_CUEVA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"ECOAL",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"CENACOP",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISPROALZA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"JUDISPRO",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"MADELI",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"SKANDINAR",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISMAG",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DIMMIA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISPROVALLES",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"PROORIENTE",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"ALSODI",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"GRAMPIR",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"ALMABI",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISANAHISA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"APRONAM",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISPROLOP",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISCARNICOS",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"GARVELPRODUCT",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"PATRICIO_CEVALLOS",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"PAUL_FLORENCIA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        }
    ]


def company_list_grupo_1():
    return [
        {
            "name":"POSSO_CUEVA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"CENACOP",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISPROALZA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"MADELI",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISPROVALLES",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISPROLOP",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"PAUL_FLORENCIA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        }
    ]


def company_list_grupo_2():
    return [
        {
            "name":"JUDISPRO",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISMAG",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"PROORIENTE",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"ALSODI",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"GRAMPIR",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"ALMABI",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISANAHISA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"GARVELPRODUCT",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        }
    ]


def company_list_grupo_3():
    return [
        {
            "name":"ECOAL",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"SKANDINAR",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DIMMIA",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"PATRICIO_CEVALLOS",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"APRONAM",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        },
        {
            "name":"DISCARNICOS",
            "user":"SoporteBZ",
            "password": "BZs2025@"
        }
    ]