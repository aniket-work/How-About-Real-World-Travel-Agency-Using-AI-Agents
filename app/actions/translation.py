def translate_text(text, target_language):
    translations = {
        "fr": "Bonjour, comment allez-vous?",
        "es": "Hola, ¿cómo estás?",
        "de": "Hallo, wie geht es Ihnen?"
    }
    return f"'{text}' translated to {target_language}: '{translations.get(target_language, text)}'"