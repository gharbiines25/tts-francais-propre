#!/usr/bin/env python3
"""
Tests de validation du modèle TTS français
"""

import subprocess
import time
from pathlib import Path

def test_model_basic():
    """Test de base du modèle"""
    print("Test de base du modèle...")
    
    test_phrases = [
        "Bonjour, comment allez-vous ?",
        "La synthèse vocale fonctionne correctement.",
        "Test avec des chiffres: 123 et 456.",
        "Voici une phrase plus longue pour tester la qualité de la voix synthétique."
    ]
    
    model_path = "../model/fr-tts-model.onnx"
    config_path = "../model/fr-tts-model.onnx.json"
    
    if not Path(model_path).exists():
        print("Erreur: Modèle non trouvé")
        return False
    
    results = []
    
    for i, phrase in enumerate(test_phrases):
        output_file = f"test_output_{i+1}.wav"
        
        cmd = [
            "piper",
            "--model", model_path,
            "--config", config_path,
            "--output_file", output_file
        ]
        
        try:
            start_time = time.time()
            process = subprocess.run(
                cmd,
                input=phrase,
                text=True,
                capture_output=True,
                check=True
            )
            duration = time.time() - start_time
            
            file_size = Path(output_file).stat().st_size if Path(output_file).exists() else 0
            
            results.append({
                "phrase": phrase,
                "success": True,
                "duration": duration,
                "file_size": file_size
            })
            print(f"Test {i+1} réussi: {duration:.2f}s, {file_size} bytes")
            
        except subprocess.CalledProcessError as e:
            results.append({
                "phrase": phrase,
                "success": False,
                "error": str(e)
            })
            print(f"Test {i+1} échoué")
    
    return results

def generate_test_report(results):
    """Génère un rapport de test"""
    print("\nRapport de test")
    print("=" * 50)
    
    total_tests = len(results)
    successful_tests = sum(1 for r in results if r["success"])
    
    print(f"Tests réussis: {successful_tests}/{total_tests}")
    
    if successful_tests > 0:
        avg_duration = sum(r["duration"] for r in results if r["success"]) / successful_tests
        avg_size = sum(r["file_size"] for r in results if r["success"]) / successful_tests
        
        print(f"Temps moyen: {avg_duration:.2f}s")
        print(f"Taille moyenne: {avg_size:.0f} bytes")
    
    print("\nTests terminés")

if __name__ == "__main__":
    print("Tests du modèle TTS français")
    print("=" * 50)
    
    results = test_model_basic()
    if results:
        generate_test_report(results)
