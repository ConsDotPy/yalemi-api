''' Data Schema configuration using Pydantic '''

from pydantic import BaseModel


class May(BaseModel):
    ''' Defining the May schema '''
    id_may: int | None
    title: str
    content: str
    published: bool = True
    created_at: str | None
