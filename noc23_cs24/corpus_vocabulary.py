#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 20:02:22 2023

@author: ram
"""
corpus="""given a sound clip of a person or people speaking, separate it into words
given a text transform those units and produce a spoken representation
separate a chunk of continuous text into separate words
given a sentence determine the part of speech for each word"""

corpus_list=corpus.split()

V=list(set(corpus_list))