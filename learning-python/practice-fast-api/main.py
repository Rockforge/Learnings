from enum import Enum
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

import math

fake_items_db = [
    {'item_name': 'Foo'},
    {'item_name': 'Bar'},
    {'item_name': 'Baz'},
]


class ModelName(str, Enum):
    """A class used to represent a model name

    Attributes
    ----------
    alexnet : str
    resnet : str
    lenet : str
    """
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


class Item(BaseModel):
    """A class used to represent an item

    Attributes
    ----------
    name : str
        The name of the item.

    description : str, optional, default=None
        The description of the item.

    price : float
        The price of the item.

    tax : float, optional, default=None
        The tax for the item.
    """

    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/items/')
async def read_item(q: Optional[str] = None):
    results = {'items': [
        {'item_id': 'Foo'},
        {'item_id': 'Bar'},
    ]}

    if q:
        results.update({'q': q})

    return results

@app.post('/items')
async def create_item(item: Item):
    item_dict = item.dict()

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})

    return item_dict

@app.put('/items/{item_id}')
async def create_item(item_id: int, item: Item):
    return {'item_id': item_id, **item.dict()}

@app.get('/items/{item_id}')
async def read_user_item(item_id: str,
                         needy: str,
                         skip: int = 0,
                         limit: Optional[int] = None):
    """Read user item

    Parameters
    ----------
    item_id : str
        The item ID

    needy : str
        Determine if this is needy

    skip : int, default=0
        The skip value

    limit : int, default=None
        The limit for the data

    Returns
    -------
    dict
        The item with values
    """

    str = {
        'item_id': item_id,
        'needy': needy,
        'skip': skip,
        'limit': limit,
    }

    return item

# @app.get('/users/{user_id}/items/{item_id}')
# async def read_user_item(user_id: int, item_id: int, q: Optional[str] = None,
#                          short: bool = False):
#     item = {'item_id': item_id, 'owner_id': user_id}
#     if q:
#         item.update({'q': q})
#     if not short:
#         item.update(
#             {'description': 'This is an amazing item that has a long description'}
#         )
#     return item

"""Notice the two routes

Make sure that the /users/me is first and the /users/{user_id} is second

Otherwise, the path for /users/{user_id} would match also for /users/me,
"thinking" that it's receiving a parameter user_id with a value of "me".

"""

@app.get('/users/me')
async def read_user_me():
    return {'user_id': 'the current user'}

@app.get('/users/{user_id}')
async def read_user(user_id: str):
    """Return user_id for passed user_id

    Parameters
    ----------
    user_id : str
        The user ID
    """
    return {'user_id': user_id}

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    """Return the model name with a message

    Parameters
    ----------
    model_name : ModelName
        The type of model we're passing

    Returns
    -------
    dict
        The model name with message
    """
    if model_name == ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep Learning FTW!'}

    # You can also access the value with ModelName.lenet.value
    # Since it's an enumeration
    if model_name.value == 'lenet':
        return {'model_name': model_name, 'message': 'LeCNN all the images'}

    return {'model_name': model_name, 'message': 'Have some residuals'}

@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}
