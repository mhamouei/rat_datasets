#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 13:12:57 2021

@author: mhit
"""

"""
Example usage::
    .. code-block::
        my_npzfile = ...
        with NpzMMap(my_npzfile) as zfile:
            with zfile.mmap(data_name) as data:
                # do anything to memory-mapped ``data``
                ...
"""

import os
import logging
import shutil
import contextlib
import tempfile
import zipfile

import numpy as np


class _TempMMap:
    def __init__(self, data_source, mmap_mode):
        # why to use ``NamedTemporaryFile`` without automatic removal:
        # https://github.com/numpy/numpy/issues/3143
        self.cbuf = tempfile.NamedTemporaryFile(delete=False)
        try:
            with contextlib.closing(data_source):
                shutil.copyfileobj(data_source, self.cbuf)
        except:
            self.close()
            raise
        else:
            self.close(_delete=False)
        self.mmap_mode = mmap_mode

    def open(self):
        """
        :return: the memory-mapped array
        """
        return np.load(self.cbuf.name, mmap_mode=self.mmap_mode)

    def close(self, _delete=True):
        """
        Close and release the memory-mapped file.
        :param _delete: user should not modify this argument
        """
        logger = self._l(self.close.__name__)
        if self.cbuf is not None:
            self.cbuf.close()
        if _delete and self.cbuf is not None:
            try:
                os.remove(self.cbuf.name)
            except FileNotFoundError:
                self.cbuf = None
            except:
                logger.error('Error removing temp file "%s"', self.cbuf.name)
                raise
            else:
                self.cbuf = None

    def __enter__(self):
        return self.open()

    def __exit__(self, _1, _2, _3):
        self.close()

    @classmethod
    def _l(cls, method_name: str = None) -> logging.Logger:
        tokens = [__name__, cls.__name__]
        if method_name:
            tokens.append(method_name)
        return logging.getLogger('.'.join(tokens))


class NpzMMap:
    def __init__(self, npzfile) -> None:
        """
        :param npzfile: anything representing an npz file that can be
               accepted by ``numpy.load``
        """
        self.npzfile = npzfile
        with np.load(self.npzfile) as zdata:
            self.npzkeys = set(zdata)
        self._zfile = zipfile.ZipFile(self.npzfile)

    def close(self):
        if self._zfile is not None:
            self._zfile.close()

    def mmap(self, key: str, mmap_mode: str = 'r'):
        """
        :param key: which entry in ``self.npzfile`` to memory-map.
        :param mmap_mode: see ``help(numpy.load)`` for detail; default to 'r'
        :return: memory-mapped file
        :raise KeyError: if ``key`` is not in ``keys()`` of ``self.npzfile``
        :raise ValueError: if ``mmap_mode`` is ``None`` or equivalent
        """
        if key not in self.npzkeys:
            raise KeyError('key "{}" not in npzfile "{}"'
                           .format(key, self.npzfile))
        if not mmap_mode:
            raise ValueError('mmap_mode must not be empty')
        if mmap_mode != 'r':
            raise NotImplementedError
        if key not in self._zfile.namelist():
            key += '.npy'
        assert key in self._zfile.namelist(), str(key)
        return _TempMMap(self._zfile.open(key), mmap_mode)

    def __enter__(self):
        return self

    def __exit__(self, _1, _2, _3):
        self.close()
