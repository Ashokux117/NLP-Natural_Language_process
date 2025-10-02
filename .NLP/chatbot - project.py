{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e5ae8bb-ef04-4c0c-8279-60e5203ac1e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi i am the cleverprogrammer and I like to chat\n",
      "please type lowercase in english language to start a conversation. type quit to leave\n"
     ]
    }
   ],
   "source": [
    "from nltk.chat.util import Chat, reflections\n",
    "# pairs is a list of patterns and responses.\n",
    "pairs = [\n",
    "    [\n",
    "        r\"(.*)my name is (.*)\",\n",
    "        [\"Hello %2, How are you today ?\",]\n",
    "    ],\n",
    "    [\n",
    "        r\"(.*)help(.*) \",\n",
    "        [\"I can help you \",]\n",
    "    ],\n",
    "     [\n",
    "        r\"(.*) your name ?\",\n",
    "        [\"My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot .\",]\n",
    "    ],\n",
    "    [\n",
    "        r\"how are you (.*) ?\",\n",
    "        [\"I'm doing very well\", \"i am great !\"]\n",
    "    ],\n",
    "    [\n",
    "        r\"sorry (.*)\",\n",
    "        [\"Its alright\",\"Its OK, never mind that\",]\n",
    "    ],\n",
    "    [\n",
    "        r\"i'm (.*) (good|well|okay|ok)\",\n",
    "        [\"Nice to hear that\",\"Alright, great !\",]\n",
    "    ],\n",
    "    [\n",
    "        r\"(hi|hey|hello|hola|holla)(.*)\",\n",
    "        [\"Hello\", \"Hey there\",]\n",
    "    ],\n",
    "    [\n",
    "        r\"what (.*) want ?\",\n",
    "        [\"Make me an offer I can't refuse\",]\n",
    "        \n",
    "    ],\n",
    "    [\n",
    "        r\"(.*)created(.*)\",\n",
    "        [\"prakash created me using Python's NLTK library \",\"top secret ;)\",]\n",
    "    ],\n",
    "    [\n",
    "        r\"(.*) (location|city) ?\",\n",
    "        ['hyderabad, India',]\n",
    "    ],\n",
    "    [\n",
    "        r\"(.*)raining in (.*)\",\n",
    "        [\"No rain in the past 4 days here in %2\",\"In %2 there is a 50% chance of rain\",]\n",
    "    ],\n",
    "    [\n",
    "        r\"how (.*) health (.*)\",\n",
    "        [\"Health is very important, but I am a computer, so I don't need to worry about my health \",]\n",
    "    ],\n",
    "    [\n",
    "        r\"(.*)(sports|game|sport)(.*)\",\n",
    "        [\"I'm a very big fan of Cricket\",]\n",
    "    ],\n",
    "    [\n",
    "        r\"who (.*) (Cricketer|Batsman)?\",\n",
    "        [\"Virat Kohli\"]\n",
    "    ],\n",
    "    [\n",
    "        r\"quit\",\n",
    "        [\"Bye for now. See you soon :) \",\"It was nice talking to you. See you soon :)\"]\n",
    "    ],\n",
    "    [\n",
    "        r\"(.*)\",\n",
    "        ['our customer service will reach you']\n",
    "    ],\n",
    " ]   \n",
    "\n",
    "# default massage at the start of chat \n",
    "print(\"Hi i am the cleverprogrammer and I like to chat\\nplease type lowercase in english language to start a conversation. type quit to leave\")\n",
    "# create chatbot\n",
    "chat = Chat(pairs, reflections)\n",
    "\n",
    "chat.converse()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8bfbaece-d5ac-4015-bbf1-b3bef684d196",
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
