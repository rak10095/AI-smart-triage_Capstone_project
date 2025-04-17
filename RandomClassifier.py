{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "KYfyPzZ-LGpy"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "import pickle\n",
        "\n",
        "# Loading dataset\n",
        "df = pd.read_csv(\"symbipredict_2022.csv\")\n",
        "\n",
        "# Separating features and target\n",
        "X = df.drop(columns=[\"prognosis\"])\n",
        "y = df[\"prognosis\"]\n",
        "\n",
        "# Training the model\n",
        "clf = RandomForestClassifier()\n",
        "clf.fit(X, y)\n",
        "\n",
        "# Saving model to pkl file\n",
        "with open(\"symptom_disease_model.pkl\", \"wb\") as f:\n",
        "    pickle.dump(clf, f)\n",
        "\n",
        "# Also save symptom names\n",
        "import json\n",
        "with open(\"symptom_names.json\", \"w\") as f:\n",
        "    json.dump(X.columns.tolist(), f)\n"
      ]
    }
  ]
}