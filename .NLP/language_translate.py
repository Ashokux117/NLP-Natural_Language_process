{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "1ce8edb5-2ddd-4929-adb7-efd195ed0ce9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting mtranslate\n",
      "  Downloading mtranslate-1.8.tar.gz (2.4 kB)\n",
      "  Preparing metadata (setup.py): started\n",
      "  Preparing metadata (setup.py): finished with status 'done'\n",
      "Building wheels for collected packages: mtranslate\n",
      "  Building wheel for mtranslate (setup.py): started\n",
      "  Building wheel for mtranslate (setup.py): finished with status 'done'\n",
      "  Created wheel for mtranslate: filename=mtranslate-1.8-py3-none-any.whl size=3680 sha256=4eca65d0dbf6587e400c0bf23d4eabef39aad7c0e2bf5893e58e7de37f2d901b\n",
      "  Stored in directory: c:\\users\\dell\\appdata\\local\\pip\\cache\\wheels\\04\\5b\\83\\c25d4a866e5f15021667de75eebe8e9aec1b673237a44c4d0a\n",
      "Successfully built mtranslate\n",
      "Installing collected packages: mtranslate\n",
      "Successfully installed mtranslate-1.8\n"
     ]
    }
   ],
   "source": [
    "# !pip install mtranslate\n",
    "import streamlit as st\n",
    "import pandas as pd \n",
    "import os \n",
    "from gtts import gTTS\n",
    "import base64"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60b9d7f7-bf21-48a1-a4a0-7fec42810b87",
   "metadata": {},
   "outputs": [],
   "source": [
    "# read language dataset\n",
    "df = pd.read_csv(r'"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
