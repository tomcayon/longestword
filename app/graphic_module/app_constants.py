"""
HEADER for the app
Contain every constants like the dimensions, the colors, the strings, etc.
And also the libraries !
"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

import os

from .app_utils import * #the .app_utils is because this is a file contained in the package

W,H = 600,600
PAD = 5

PACKAGE_PATH = os.path.dirname(__file__)
IMAGES_PATH = os.path.join(PACKAGE_PATH,"images")

PALETTE = "/palette.json"
STRINGS = "/strings.json"
LANG = "fr"

HEADER_STYLE = ("Times New Roman",20)
LETTER_CARDS_STYLE = ("Times New Roman",16)

APP_COLOR = AppColors(PACKAGE_PATH+PALETTE)
APP_STRINGS = AppStrings(PACKAGE_PATH+STRINGS,LANG)
