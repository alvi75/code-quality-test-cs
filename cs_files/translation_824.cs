public override TokenStream Create(TokenStream input){
    return new ReverseStringFilter(StringHelper.GetEncodedVersion(input));
}
string value = GetInflectionType(0);
if (value == null){
    throw new ArgumentException("wordnet dictionary requires an inflow rule");
}
this.synonymFile = value;
return new SynonymStream(this);
}