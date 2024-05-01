# SPDX-License-Identifier: WTFPL
# SPDX-FileCopyrightText: 2023 Anna <cyber@sysrq.in>
# No warranty

"""
Generic generator interface.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Type

from gentle.metadata import MetadataXML

GentleGenerator = Type["AbstractGenerator"]


class AbstractGenerator(ABC):
    """
    Generic class for metadata generators.
    """

    _subclasses: list[GentleGenerator] = []

    @classmethod
    def get_generator_subclasses(cls) -> list[GentleGenerator]:
        """
        Get generators inheriting from this abstract class.

        :returns: subclasses
        """

        return cls._subclasses.copy()

    @abstractmethod
    def __init__(self, srcdir: Path):
        """
        :param srcdir: path to unpacked sources
        """

    def __init_subclass__(cls, **kwargs: dict) -> None:
        super().__init_subclass__(**kwargs)
        AbstractGenerator._subclasses.append(cls)

    @abstractmethod
    def update_metadata_xml(self, mxml: MetadataXML) -> None:
        """
        Update metadata object in place.
        """

    @property
    @abstractmethod
    def active(self) -> bool:
        """
        Whether generator works.
        """

    @property
    def slow(self) -> bool:
        """
        Whether generator takes long time to finish.
        """

        return False
