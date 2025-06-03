"""Simple keyword-based classifier."""

KEYWORDS = {
    'Madrid': ['madrid', 'espana'],
    'Barcelona': ['barcelona'],
    'Valencia': ['valencia'],
}


def classify_mail(text: str) -> str:
    text_lower = text.lower()
    for site, words in KEYWORDS.items():
        for w in words:
            if w in text_lower:
                return site
    return 'General'
