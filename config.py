import os
import sys
from dataclasses import dataclass
from typing import Callable, Union

key = 'JIRA_USER'
def _env(key: str) -> str:
    v = os.getenv(key)
    assert v, f'Env variable {key} is not set or empty'
    return v
    print("Value of 'jira_user' environment variable :", v) 

print(_env)

class DeferredString:
    def __init__(self, fn: Callable, key_or_arg: Union[int, str]):
        self._fn = fn
        self._key_or_arg = key_or_arg

    def resolve(self) -> str:
        return self._fn(self._key_or_arg)


def from_env(key: str) -> DeferredString:
    return DeferredString(fn=_env, key_or_arg=key)





def make_settings() -> 'Settings':
    s = Settings()
    for field in s.__dict__:
        attr = getattr(s, field)
        if isinstance(attr, DeferredString):
            setattr(s, field, attr.resolve())
    return s

    
# -----------------------------------------------------------------
# ------ Configure your runtime below ------------------------------

@dataclass
class Settings:
    jira_user: Union[str, DeferredString] = from_env('JIRA_USER')
    jira_pass: Union[str, DeferredString] = from_env('JIRA_PASS')
    pickle_filepath: str = './data/jiras.bin'


# -----------------------------------------------------------------

