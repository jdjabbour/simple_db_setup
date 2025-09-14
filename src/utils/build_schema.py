
from dataclasses import dataclass
from typing import List

@dataclass
class BuildSchema:
    schema: dict
    
    def build_schema(self: object):
        pass

    def unpack_schema(self: object):
        table = self.schema['table']
        columns = self.schema['columns']
        proxy_columns = self.build_proxy_values()


    def build_proxy_values(self: object) -> str:
        prox_cols = self.schema['columns']
        prox_len = len(prox_cols)
        prox_qm = str(tuple(list(map(str, ('?'*prox_len))))).replace("'", "").replace(' ', '')
        return prox_qm 