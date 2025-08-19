# Données d'entraînement

## Contenu
- `metadata.csv`: 93 phrases françaises avec correspondances audio
- `sample_audio/`: Échantillons des enregistrements audio

## Format des données
- **Audio**: WAV 22050 Hz mono
- **Durée totale**: ~15 minutes
- **Qualité**: Enregistrements studio

## Structure metadata.csv
```
phrase001.wav|Bonjour, comment allez-vous aujourd'hui ?
phrase002.wav|La synthèse vocale française fonctionne parfaitement.
phrase003.wav|Les modèles de langue naturelle sont fascinants.
...
```

## Utilisation
Ces données ont été utilisées pour entraîner le modèle VITS français selon la méthodologie Piper-GPL.
