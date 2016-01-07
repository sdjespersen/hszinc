#!/usr/bin/python
# -*- coding: utf-8 -*-
# Zinc Grid
# (C) 2016 VRT Systems
#
# vim: set ts=4 sts=4 et tw=78 sw=4 si:

from .metadata import MetadataObject
from .sortabledict import SortableDict
from collections import MutableSequence

class Grid(MutableSequence):
    '''
    A grid is basically a series of tabular records.  The grid has a header
    which describes some metadata about the grid and its columns.  This is
    followed by zero or more rows.
    '''

    # Grid version number
    DEFAULT_VERSION = "2.0"

    def __init__(self, version=DEFAULT_VERSION, metadata=None, columns=None):
        '''
        Create a new Grid.
        '''
        # Version
        self._version   = version

        # Metadata
        self.metadata   = MetadataObject()

        # The columns
        self.column     = SortableDict()

        # Rows
        self._row       = []

        if metadata is not None:
            self.metadata.extend(metadata)

        if columns is not None:
            if isinstance(columns, dict) or isinstance(columns, SortableDict):
                columns = columns.items()

            for col_id, col_meta in columns:
                if not isinstance(col_meta, MetadataObject):
                    mo = MetadataObject()
                    mo.extend(col_meta)
                    col_meta = mo
                self.column.add_item(col_id, col_meta)

    def __getitem__(self, index):
        '''
        Retrieve the row at index.
        '''
        return self._row[index]

    def __len__(self):
        '''
        Return the number of rows in the grid.
        '''
        return len(self._row)

    def __setitem__(self, index, value):
        '''
        Replace the row at index.
        '''
        if not isinstance(value, dict):
            raise TypeError('value must be a dict')
        self._row[index] = value

    def __delitem__(self, index):
        '''
        Delete the row at index.
        '''
        del self._row[index]

    def insert(self, index, value):
        '''
        Insert a new row before index.
        '''
        if not isinstance(value, dict):
            raise TypeError('value must be a dict')
        self._row.insert(index, value)
