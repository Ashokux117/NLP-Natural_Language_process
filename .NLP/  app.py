{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5474cb84-948d-411b-9101-78f9fd88011e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to\n",
      "[nltk_data]     C:\\Users\\DELL\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request\n",
    "from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize, blankline_tokenize, WhitespaceTokenizer\n",
    "from nltk.util import bigrams, trigrams, ngrams\n",
    "from nltk.stem import PorterStemmer\n",
    "import nltk\n",
    "\n",
    "nltk.download('punkt')\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route(\"/\", methods=[\"GET\", \"POST\"])\n",
    "def home():\n",
    "    result = {}\n",
    "    if request.method == \"POST\":\n",
    "        text = request.form[\"user_text\"]\n",
    "\n",
    "        # Sentence Tokenize\n",
    "        sentences = sent_tokenize(text)\n",
    "        result[\"sentence_count\"] = len(sentences)\n",
    "\n",
    "        # Word Tokenize\n",
    "        words = word_tokenize(text)\n",
    "        result[\"word_count\"] = len(words)\n",
    "\n",
    "        # Whitespace Tokenizer\n",
    "        wt = WhitespaceTokenizer().tokenize(text)\n",
    "        result[\"whitespace_tokens\"] = wt\n",
    "        result[\"whitespace_count\"] = len(wt)\n",
    "\n",
    "        # Wordpunct Tokenize\n",
    "        wpt = wordpunct_tokenize(text)\n",
    "        result[\"wordpunct_tokens\"] = wpt\n",
    "        result[\"wordpunct_count\"] = len(wpt)\n",
    "\n",
    "        # Bigrams, Trigrams, Ngrams\n",
    "        result[\"bigrams\"] = list(bigrams(words))\n",
    "        result[\"trigrams\"] = list(trigrams(words))\n",
    "        result[\"4grams\"] = list(ngrams(words, 4))\n",
    "\n",
    "        # Stemming\n",
    "        pst = PorterStemmer()\n",
    "        result[\"stemming\"] = {word: pst.stem(word) for word in words if word.isalpha()}\n",
    "\n",
    "        result[\"text\"] = text\n",
    "\n",
    "    return render_template(\"index.html\", result=result)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24e7f9f0-7528-4719-a33f-ddd88f3708f8",
   "metadata": {},
   "outputs": [],
   "source": []
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
