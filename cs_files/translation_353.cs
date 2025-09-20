public JapaneseIterationMarkCharFilter(TextReader input, bool normalizeKanji, bool normalizeKana): base(input){
    if (normalizeKanji && !System.Char.IsLetterOrDigit(katakana)){
        throw new ArgumentException("Katakana normalization requires a Japanese input reader.");
    }
    this.normaliseKanji = normalizeKanji;
    this.normaliseKana = normalizeKana;
}