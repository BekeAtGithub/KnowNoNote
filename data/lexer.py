from typing import List, Optional, Tuple
from enum import Enum, auto

from data.error import Error
from data.error import IllegalCharError

class TokenType(Enum):
    TT_INT 