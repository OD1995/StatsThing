from dataclasses import dataclass
from typing import List
from app.types.GenericTableRow import GenericTableRow

@dataclass
class GenericTableData:

    def __init__(
        self,
        column_headers:List[str],
        rows:List[GenericTableRow],
        title:str=None,
        is_ranked:bool=False,
        sort_by:str=None,
        sort_direction:str=None
    ):
        self.column_headers = column_headers
        self.rows = rows
        self.title = title
        self.is_ranked = is_ranked
        self.sort_by = sort_by
        self.sort_direction = sort_direction

    def to_dict(self):
        return {
            "column_headers" : self.column_headers,
            "rows" : [
                r.to_dict()
                for r in self.rows
            ],
            "title" : self.title,
            "is_ranked" : self.is_ranked,
            'sort_by' : self.sort_by,
            'sort_direction' : self.sort_direction
        }