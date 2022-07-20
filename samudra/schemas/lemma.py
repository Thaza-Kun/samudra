import datetime
from typing import List, Optional, Union

import pydantic as pyd

from samudra import models
from samudra.schemas._helper import PeeweeGetterDict
from samudra.schemas.konsep import KonsepRecord, KonsepCreation


class LemmaBase(pyd.BaseModel):
    nama: str
    model: models.BaseTable = models.Lemma


class LemmaCreation(LemmaBase):
    # --- Relationships
    konsep: List[KonsepCreation]


class LemmaRecord(LemmaCreation):
    # --- Record specific fields
    id: int
    tarikh_masuk: datetime.datetime
    # --- Relationships
    konsep: Union[List[KonsepRecord], KonsepRecord]

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
