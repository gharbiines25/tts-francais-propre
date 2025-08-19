#!/usr/bin/env python3
"""
Script d'entraînement du modèle TTS français
Utilise Piper-GPL pour entraîner un modèle VITS
"""

import subprocess
import sys
from pathlib import Path

def train_model():
    """Lance l'entraînement du modèle avec Piper"""
    
    # Configuration d'entraînement
    config = {
        "voice_name": "voix-francaise-personnelle",
        "csv_path": "../data/metadata.csv",
        "audio_dir": "../data/audio/",
        "sample_rate": 22050,
        "espeak_voice": "fr",
        "cache_dir": "./cache/",
        "config_path": "./config.json",
        "batch_size": 32,
        "epochs": 25
    }
    
    # Commande d'entraînement Piper
    cmd = [
        sys.executable, "-m", "piper.train", "fit",
        "--data.voice_name", config["voice_name"],
        "--data.csv_path", config["csv_path"],
        "--data.audio_dir", config["audio_dir"],
        "--model.sample_rate", str(config["sample_rate"]),
        "--data.espeak_voice", config["espeak_voice"],
        "--data.cache_dir", config["cache_dir"],
        "--data.config_path", config["config_path"],
        "--data.batch_size", str(config["batch_size"])
    ]
    
    print("🚀 Démarrage de l'entraînement...")
    print(f"Configuration: {config}")
    
    try:
        subprocess.run(cmd, check=True)
        print("✅ Entraînement terminé avec succès")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur pendant l'entraînement: {e}")
        return False

def export_model():
    """Exporte le modèle entraîné vers ONNX"""
    
    checkpoint_path = "./lightning_logs/version_0/checkpoints/last.ckpt"
    output_path = "../model/fr-tts-model.onnx"
    
    cmd = [
        sys.executable, "-m", "piper.train.export_onnx",
        "--checkpoint", checkpoint_path,
        "--output-file", output_path
    ]
    
    print("📦 Export du modèle vers ONNX...")
    
    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Modèle exporté: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur pendant l'export: {e}")
        return False

if __name__ == "__main__":
    print("🎤 Entraînement du modèle TTS français")
    print("=" * 50)
    
    # Entraînement
    if train_model():
        # Export si entraînement réussi
        export_model()
    else:
        print("❌ Échec de l'entraînement")
