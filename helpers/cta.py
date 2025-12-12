import re

MUSIC_PATTERN = re.compile( 
    r""" # Matches various forms of 'music' cues
        (\[\s*music\s*\]|\(\s*music\s*\))   
        |(\[\s*music)                       
        |(music\s*\])                       
        |^\s*music\s*$                      
    """,
    re.IGNORECASE | re.VERBOSE,
)

CTA_VERBS = {
    "subscribe", "follow", "share", "like", "rate", "review",
    "visit", "check", "sign", "donate", "support", "join",
    "buy", "use", "download", "click", "call", "email",
    "register", "tell", "spread"
}

CTA_MULTIWORD = {
    "sign up", "log in", "check out"
}

CTA_PHRASES = {
    "use code", "promo code", "discount code", "free trial",
    "link in", "show notes","dot com", "dot org", "visit us at"
}

URL_PATTERN = re.compile(
    r"https?://\S+|"
    r"www\.\S+|"
    r"\b\w+\.(com|org|net|io|co)\b|"
    r"http\s+colon|"
    r"slash\s+slash",
    re.IGNORECASE
)

SECOND_PERSON = {"you", "your", "yours"}

PHI3_SYSTEM_PROMPT = (
    "You are a text classification assistant. "
    "Your task is to determine whether a sentence contains a Call to Action (CTA). "
    "A CTA is any utterance encouraging the listening audience to perform a specific action. "
    "Respond ONLY with TRUE or FALSE."
)

FEW_SHOT_EXAMPLES = [
    {
        "role": "user",
        "content": "Sentence: If you enjoy this podcast, please subscribe and leave a review.\nCTA?"
    },
    {"role": "assistant", "content": "TRUE"},

    {
        "role": "user",
        "content": "Sentence: Climate change is a complex issue with many drivers.\nCTA?"
    },
    {"role": "assistant", "content": "FALSE"},

    {
        "role": "user",
        "content": "Sentence: There's a link in the show notes if you want to support the campaign.\nCTA?"
    },
    {"role": "assistant", "content": "TRUE"},

    {
        "role": "user",
        "content": "Sentence: Thanks for listening, see you next time.\nCTA?"
    },
    {"role": "assistant", "content": "FALSE"},
]