public override TextReader Create(TextReader input){
    return new PersianNormalizationFilter(CharsetNormalizer2.GetInstance(null, "nfkc_cf", "compose"))_input = input;
}