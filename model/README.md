# Guide d'utilisation du modèle TTS français

## Installation
```bash
pip install piper-tts
```

## Utilisation de base
```bash
# Test simple
echo "Bonjour, comment allez-vous ?" | piper \
  --model fr-tts-model.onnx \
  --config fr-tts-model.onnx.json \
  --output_file sortie.wav
```

## Utilisation en Python
```python
import subprocess

def generer_audio(texte, fichier_sortie):
    cmd = [
        "piper",
        "--model", "fr-tts-model.onnx",
        "--config", "fr-tts-model.onnx.json",
        "--output_file", fichier_sortie
    ]
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, text=True)
    process.communicate(input=texte)

# Exemple
generer_audio("Bonjour le monde !", "test.wav")
```

## Spécifications techniques
- **Format**: ONNX
- **Taille**: 4.0 MB
- **Sample rate**: 22050 Hz
- **Architecture**: VITS
- **Paramètres**: 70.4M

## Compatibilité
- Piper CLI
- Piper Python API
- ONNX Runtime
- Applications tierces ONNX
