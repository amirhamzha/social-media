from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint

class PostBase(BaseModel):
    title:str
    content:str
    published:bool= True


class PostCreate(PostBase):
    pass



class UserOut(BaseModel):

    id:int
    email: EmailStr
    created_at: datetime
       
    class Config:
        orm_mode = True





class Post(PostBase):
    id:int
    created_at: datetime
    owner_id :int
    owner : UserOut    # pydantic model type userout

    """Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model (or any other arbitrary object with attributes).

    This way, instead of only trying to get the id value from a dict, as in"""
    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post : Post
    votes : int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password : str




class UserLogin(BaseModel):

    email: EmailStr
    password : str

class Token(BaseModel):
    access_token: str
    token_type : str


class TokenData(BaseModel):
    id: Optional[int] =None



class Vote(BaseModel):

    post_id :int
    dir :bool

