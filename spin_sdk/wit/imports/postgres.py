from typing import TypeVar, Generic, Union, Optional, Union, Protocol, Tuple, List, Any
from enum import Flag, Enum, auto
from dataclasses import dataclass
from abc import abstractmethod
import weakref

from ..types import Result, Ok, Err, Some
from ..imports import rdbms_types

class Connection:
    """
    A connection to a postgres database.
    """
    
    @staticmethod
    def open(address: str) -> Connection:
        """
        Open a connection to the Postgres instance at `address`.
        """
        raise NotImplementedError

    def query(self, statement: str, params: List[rdbms_types.ParameterValue]) -> rdbms_types.RowSet:
        """
        Query the database.
        """
        raise NotImplementedError

    def execute(self, statement: str, params: List[rdbms_types.ParameterValue]) -> int:
        """
        Execute command to the database.
        """
        raise NotImplementedError

    def drop(self):
        (_, func, args, _) = self.finalizer.detach()
        self.handle = None
        func(args[0], args[1])



