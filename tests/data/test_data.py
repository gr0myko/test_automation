from framework.base.utils.string_utils import RandomString

RANDOM_TITLE = RandomString.get_random_string(10)
RANDOM_BODY = RandomString.get_random_string(10)
NEW_POST = {"title": RANDOM_TITLE, "body": RANDOM_BODY, "userId": 1, "id": 101}

USER_5 = {"id": 5,
          "name": "Chelsey Dietrich",
          "username": "Kamren",
          "email": "Lucio_Hettinger@annie.ca",
          "address": {
              "street": "Skiles Walks",
              "suite": "Suite 351",
              "city": "Roscoeview",
              "zipcode": "33263",
              "geo": {
                  "lat": "-31.8129",
                  "lng": "62.5342"
              }
          },
          "phone": "(254)954-1289",
          "website": "demarco.info",
          "company": {
              "name": "Keebler LLC",
              "catchPhrase": "User-centric fault-tolerant solution",
              "bs": "revolutionize end-to-end systems"
          }
          }
