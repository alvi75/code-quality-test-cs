public SynonymFilterSynonymFilter synonyms = new JCG.Dictionary<string, IList<Synonym>>(23);
#pragma warning disable 612, 618if (format.Equals("solr", StringComparison.Ordinal)){
    analyzer.GetPositionIncrementGap("synonyms");
    analyzer.GetOffsetGap("synonyms");
    List<Synonym> tmp = new List<Synonym>();
    using (TextReader reader = new StreamReader(stream)){
        string line = null;
        while ((line = reader.ReadLine()) != null){
            string[] parts = line.Split(new string[] {
                "," }
                , StringSplitOptions.RemoveEmptyEntries);
                if (parts.Length == 2){
                    tmp.Add(new Synonym(parts[0], parts[1]);
                }
                else{
                    throw new System.ArgumentException("Invalid synonym rule at line " + reader.LineNumber);
                }
                Rule rules = new Rule[ArrayUtil.CountOf(parts, 2)];
                for (int i = 0;
                i < rules.Length;
                i++){
                    rules[i] = new Rule(int.Parse(parts[i], NumberStyles.Integer, CultureInfo.InvariantCulture), int.Parse(parts[i + 1], NumberStyles.Integer, CultureInfo.InvariantCulture));
                }
            }