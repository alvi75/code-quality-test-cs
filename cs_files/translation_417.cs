public override BreakIterator GetBreakIterator(int script){
    switch (script){
        case UScript.HANGUL:return (HANGUL SCRIPT);
        case UScript.KATAKANA:return (KATAKANA SCRIPT);
        case UScript.LATIN:return (LATIN SCRIPT);
        case UScript.TURKISH:return (TURKISH SCRIPT);
        case UScript.DEFAULT:return (DEFAULT SCRIPT);
    }
    return null;
}