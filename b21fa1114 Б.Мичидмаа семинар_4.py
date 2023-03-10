{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e4923800",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1-р даалгавар\n",
    "import numpy as np\n",
    "x = np.arange(51)\n",
    "print(x+50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8053c863",
   "metadata": {},
   "outputs": [],
   "source": [
    "#2-р даалгавар\n",
    "x = np.zeros(10)\n",
    "y = np.ones(10)\n",
    "z = (np.zeros(10)+6)\n",
    "print(x, y, z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "edf3e7f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#3-р даалгавар\n",
    "a = np.arange(20,32).reshape(3,4)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "964d4f4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#4-р даалгавар\n",
    "np.eye(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "06f82aea",
   "metadata": {},
   "outputs": [],
   "source": [
    "#5-р даалгавар\n",
    "np.diag([1, 2, 3, 4, 5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "de464071",
   "metadata": {},
   "outputs": [],
   "source": [
    "#6-р даалгавар\n",
    "a = np.arange(4).reshape(2,2)\n",
    "print(a.sum(axis=0))\n",
    "print(a.sum(axis=1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "aef32f35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5878 5248 5898 6639 6416 6383 4654 5284 4696 3941]\n",
      "[6431 5360 7533 6293 4876 5051 4604 5826 3279 5784]\n"
     ]
    }
   ],
   "source": [
    "#7-р даалгавар\n",
    "#Нийт гоал\n",
    "import numpy as np\n",
    "KobeBryant_FG = [978,813,775,800,716,740,574,738,31,266]\n",
    "JoeJohnson_FG = [632,536,647,620,635,514,423,445,462,446]\n",
    "LeBronJames_FG = [875,772,794,789,768,758,621,765,767,624]\n",
    "CarmeloAnthony_FG = [756,691,728,535,688,684,441,669,743,358]\n",
    "DwightHoward_FG = [468,526,583,560,510,619,416,470,473,251]\n",
    "ChrisBosh_FG = [549,543,507,615,600,524,393,485,492,343]\n",
    "ChrisPaul_FG = [407,381,630,631,314,430,425,412,406,568]\n",
    "KevinDurant_FG = [306,306,587,661,794,711,643,731,849,238]\n",
    "DerrickRose_FG = [208,208,208,574,672,711,302,0,58,338]\n",
    "DwayneWade_FG = [699,472,439,854,719,692,416,569,415,509]\n",
    "a = np.vstack([KobeBryant_FG, JoeJohnson_FG, LeBronJames_FG, CarmeloAnthony_FG, DwightHoward_FG, ChrisBosh_FG, ChrisPaul_FG, KevinDurant_FG, DerrickRose_FG, DwayneWade_FG])\n",
    "print(a.sum(axis=0))\n",
    "print(a.sum(axis=1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d05df849",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 50299635  57248613  98406186 120776420 139835227 144667149 166489555\n",
      " 189711742 205782921 204790923]\n",
      "[229306822 166205113 141461033 151622715 140546503 138008113 116051459\n",
      "  88510296  75445211 130851106]\n"
     ]
    }
   ],
   "source": [
    "#Цалин\n",
    "import numpy as np\n",
    "KobeBryant_Salary = np.array([15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000])\n",
    "JoeJohnson_Salary = np.array([12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790])\n",
    "LeBronJames_Salary = np.array([4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400])\n",
    "CarmeloAnthony_Salary = np.array([3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000])\n",
    "DwightHoward_Salary = np.array([4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271])\n",
    "ChrisBosh_Salary = np.array([3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400])\n",
    "ChrisPaul_Salary = np.array([3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563])\n",
    "KevinDurant_Salary = np.array([0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624])\n",
    "DerrickRose_Salary = np.array([0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875])\n",
    "DwayneWade_Salary = np.array([3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000])\n",
    "a = np.vstack([KobeBryant_Salary, JoeJohnson_Salary, LeBronJames_Salary, CarmeloAnthony_Salary, DwightHoward_Salary, ChrisBosh_Salary, ChrisPaul_Salary, KevinDurant_Salary, DerrickRose_Salary, DwayneWade_Salary])\n",
    "print(a.sum(axis=0))\n",
    "print(a.sum(axis=1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6469ee25",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[701 618 716 776 728 780 560 663 596 531]\n",
      "[653 739 752 673 727 684 699 639 460 643]\n"
     ]
    }
   ],
   "source": [
    "#Нийт тоглолт\n",
    "import numpy as np\n",
    "KobeBryant_G = [80,77,82,82,73,82,58,78,6,35]\n",
    "JoeJohnson_G = [82,57,82,79,76,72,60,72,79,80]\n",
    "LeBronJames_G = [79,78,75,81,76,79,62,76,77,69]\n",
    "CarmeloAnthony_G = [80,65,77,66,69,77,55,67,77,40]\n",
    "DwightHoward_G = [82,82,82,79,82,78,54,76,71,41]\n",
    "ChrisBosh_G = [70,69,67,77,70,77,57,74,79,44]\n",
    "ChrisPaul_G = [78,64,80,78,45,80,60,70,62,82]\n",
    "KevinDurant_G = [35,35,80,74,82,78,66,81,81,27]\n",
    "DerrickRose_G = [40,40,40,81,78,81,39,0,10,51]\n",
    "DwayneWade_G = [75,51,51,79,77,76,49,69,54,62]\n",
    "a = np.vstack([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G, KevinDurant_G, DerrickRose_G, DwayneWade_G])\n",
    "print(a.sum(axis=0))\n",
    "print(a.sum(axis=1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "90618473",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5878 5248 5898 6639 6416 6383 4654 5284 4696 3941]\n",
      "[6431 5360 7533 6293 4876 5051 4604 5826 3279 5784]\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e86e61f0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
