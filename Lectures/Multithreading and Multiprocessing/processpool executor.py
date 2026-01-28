{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b4fa87ab",
   "metadata": {},
   "source": [
    "### ProcessPoolExecutor \n",
    "<br>\n",
    "process pool executor is used to create multiprocesses more easily"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6666f7cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "from concurrent.futures import ProcessPoolExecutor\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e69a7251",
   "metadata": {},
   "outputs": [
    {
     "ename": "BrokenProcessPool",
     "evalue": "A process in the process pool was terminated abruptly while the future was running or pending.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mBrokenProcessPool\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 10\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m ProcessPoolExecutor(max_workers\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m3\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m executor:\n\u001b[0;32m      8\u001b[0m     result \u001b[38;5;241m=\u001b[39m executor\u001b[38;5;241m.\u001b[39mmap(compute_squares,numbers)\n\u001b[1;32m---> 10\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m result:\n\u001b[0;32m     11\u001b[0m     \u001b[38;5;28mprint\u001b[39m(i)\n",
      "File \u001b[1;32mc:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\lib\\concurrent\\futures\\process.py:567\u001b[0m, in \u001b[0;36m_chain_from_iterable_of_lists\u001b[1;34m(iterable)\u001b[0m\n\u001b[0;32m    561\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21m_chain_from_iterable_of_lists\u001b[39m(iterable):\n\u001b[0;32m    562\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    563\u001b[0m \u001b[38;5;124;03m    Specialized implementation of itertools.chain.from_iterable.\u001b[39;00m\n\u001b[0;32m    564\u001b[0m \u001b[38;5;124;03m    Each item in *iterable* should be a list.  This function is\u001b[39;00m\n\u001b[0;32m    565\u001b[0m \u001b[38;5;124;03m    careful not to keep references to yielded objects.\u001b[39;00m\n\u001b[0;32m    566\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[1;32m--> 567\u001b[0m     \u001b[38;5;28;01mfor\u001b[39;00m element \u001b[38;5;129;01min\u001b[39;00m iterable:\n\u001b[0;32m    568\u001b[0m         element\u001b[38;5;241m.\u001b[39mreverse()\n\u001b[0;32m    569\u001b[0m         \u001b[38;5;28;01mwhile\u001b[39;00m element:\n",
      "File \u001b[1;32mc:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\lib\\concurrent\\futures\\_base.py:609\u001b[0m, in \u001b[0;36mExecutor.map.<locals>.result_iterator\u001b[1;34m()\u001b[0m\n\u001b[0;32m    606\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m fs:\n\u001b[0;32m    607\u001b[0m     \u001b[38;5;66;03m# Careful not to keep a reference to the popped future\u001b[39;00m\n\u001b[0;32m    608\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m timeout \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m--> 609\u001b[0m         \u001b[38;5;28;01myield\u001b[39;00m \u001b[43mfs\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mpop\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mresult\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    610\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    611\u001b[0m         \u001b[38;5;28;01myield\u001b[39;00m fs\u001b[38;5;241m.\u001b[39mpop()\u001b[38;5;241m.\u001b[39mresult(end_time \u001b[38;5;241m-\u001b[39m time\u001b[38;5;241m.\u001b[39mmonotonic())\n",
      "File \u001b[1;32mc:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\lib\\concurrent\\futures\\_base.py:439\u001b[0m, in \u001b[0;36mFuture.result\u001b[1;34m(self, timeout)\u001b[0m\n\u001b[0;32m    437\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m CancelledError()\n\u001b[0;32m    438\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_state \u001b[38;5;241m==\u001b[39m FINISHED:\n\u001b[1;32m--> 439\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m__get_result\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    441\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_condition\u001b[38;5;241m.\u001b[39mwait(timeout)\n\u001b[0;32m    443\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_state \u001b[38;5;129;01min\u001b[39;00m [CANCELLED, CANCELLED_AND_NOTIFIED]:\n",
      "File \u001b[1;32mc:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\lib\\concurrent\\futures\\_base.py:391\u001b[0m, in \u001b[0;36mFuture.__get_result\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    389\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_exception:\n\u001b[0;32m    390\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 391\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_exception\n\u001b[0;32m    392\u001b[0m     \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[0;32m    393\u001b[0m         \u001b[38;5;66;03m# Break a reference cycle with the exception in self._exception\u001b[39;00m\n\u001b[0;32m    394\u001b[0m         \u001b[38;5;28mself\u001b[39m \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n",
      "\u001b[1;31mBrokenProcessPool\u001b[0m: A process in the process pool was terminated abruptly while the future was running or pending."
     ]
    }
   ],
   "source": [
    "def compute_squares(i):\n",
    "    time.sleep(2)\n",
    "    return f\"The square of {i}: {i*i}\"\n",
    "\n",
    "numbers = [1,3,45,6,8,9,54,2,2]\n",
    "if __name__ == '__main__':\n",
    "    with ProcessPoolExecutor(max_workers=3) as executor:\n",
    "        result = executor.map(compute_squares,numbers)\n",
    "    \n",
    "    for i in result:\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25f7fb13",
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
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
