public override SpanQuery MakeSpanQuery(){
    SpanQuery[] subSpans = MakeLuceneSubQueries();
    BooleanQuery bQuery = new BooleanQuery();
    bQuery.Add(subSpans[0], Occur.MUST);
    for (int i = 1;
    i < subSpans.Length;
    i++){
        bQuery.Add(subSpans[i], Occur.MUST);
    }
    return bQuery;
}