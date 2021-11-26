{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a5209679",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "def large(arr): \n",
    "    max_ = arr[0]\n",
    "    for ele in arr:\n",
    "        if ele > max_:\n",
    "           max_ = ele\n",
    "    return max_ \n",
    "\n",
    "\n",
    "list1 = [1,3,5,4,12,6]\n",
    "result = large(list1)\n",
    "print(result)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "edba68bf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
