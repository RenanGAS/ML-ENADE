{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "65f26788-2d69-4c4e-9ef0-9a54503f086a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "adcc2cfd-f7ab-48eb-b064-d2affc48ec40",
   "metadata": {},
   "outputs": [],
   "source": [
    "def contar_classes(dataset, classes):\n",
    "    dict_ocorrencias = {}\n",
    "    for classe in classes:\n",
    "        numero_de_ocorrencias = dataset[\"Nota_Conceito_Faixa\"].value_counts()[classe]\n",
    "        dict_ocorrencias[f\"{classe}\"] = numero_de_ocorrencias\n",
    "    return dict_ocorrencias\n",
    "\n",
    "def mostrar_distribuicao(dataset, classes):\n",
    "    dict_ocorrencias = contar_classes(dataset, classes)\n",
    "    \n",
    "    plt.style.use('_mpl-gallery')\n",
    "    \n",
    "    x = dict_ocorrencias.keys()\n",
    "   \n",
    "    y = dict_ocorrencias.values()\n",
    "    \n",
    "    fig, ax = plt.subplots(figsize=(5,3))\n",
    "\n",
    "    ax.bar(x, y, width=1, edgecolor=\"white\")\n",
    "\n",
    "    ax.set(xlim=(-1, 5), xticks=np.arange(0, 5, 1),\n",
    "           ylim=(0, 3500), yticks=np.arange(0, 3500, 500))\n",
    "    \n",
    "    plt.show()"
   ]
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
