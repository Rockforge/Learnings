from enum import Enum

from fastapi import FastAPI

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

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}

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
