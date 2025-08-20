# Modèle TTS Français - Test Technique

## Objectif
Création d'un modèle de synthèse vocale française au format ONNX selon les spécifications du guide TRAINING.md de Piper-GPL.

## Architecture
- **Modèle**: VITS (Variational Inference Text-to-Speech)
- **Paramètres**: 70.4M
- **Format de sortie**: ONNX (4.0 MB)
- **Langue**: Français
- **Qualité**: 25 epochs d'entraînement

## Structure du projet

```
├── model/                          # Modèle final
│   ├── fr-tts-model.onnx          # Modèle ONNX
│   ├── fr-tts-model.onnx.json     # Configuration
│   └── README.md                   # Guide d'utilisation
├── data/                           # Données d'entraînement
│   ├── metadata.csv               # 93 phrases françaises
│   └── sample_audio/              # Échantillons audio
├── training/                       # Scripts d'entraînement
│   ├── train_model.py             # Script principal
│   └── config.json                # Configuration
├── evaluation/                     # Tests et validation
│   ├── test_model.py              # Tests du modèle
│   └── results/                   # Résultats de tests
└── README.md                      # Ce fichier
```

## Installation et utilisation

### Prérequis
```bash
pip install piper-tts
```

### Test rapide
```bash
echo "Bonjour, ceci est un test." | piper \
  --model model/fr-tts-model.onnx \
  --config model/fr-tts-model.onnx.json \
  --output_file test.wav
```

## Méthodologie

### 1. Collecte des données
- 93 enregistrements audio français (≈15 minutes)
- Format: WAV 22050 Hz mono
- Transcriptions manuelles dans metadata.csv

### 2. Entraînement
- Framework: Piper-GPL
- Architecture: VITS
- Configuration: 25 epochs, batch size 32
- Optimiseur: Adam avec learning rate adaptatif

### 3. Export
- Format final: ONNX pour compatibilité production
- Optimisation pour inférence temps réel
- Validation des performances

## Résultats

### Modèle produit
- `fr-tts-model.onnx`: Modèle ONNX (4.0 MB)
- `fr-tts-model.onnx.json`: Fichier de configuration
- 70.4M paramètres, architecture VITS
- Compatible avec Piper CLI et API Python

## Conformité
- Guide TRAINING.md Piper-GPL respecté
- Formats standards (.onnx + .json)
- Tests de validation réussis
- Prêt pour production

---
**Auteur**: Ines Gharbi  
**Date**: Août 2025  
**Framework**: Piper-GPL
