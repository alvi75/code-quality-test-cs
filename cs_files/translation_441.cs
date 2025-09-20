public override string ToString(){
    StringBuilder r = new StringBuilder();
    r.Append("Commit");
    r.Append("={
        \n");
        r.Append("tree ");
        r.Append(EntryTree);
        r.Append("\n");
        foreach (byte[] p in EntryParents){
            r.Append("parent ");
            r.Append(Constants.TypeString(p));
            r.Append("\n");
        }
        r.Append("author ");
        r.Append(EntryAuthor);
        r.Append("\n");
        r.Append("tag ");
        r.Append(EntryTag);
        r.Append("\n");
        r.Append("tagger ");
        r.Append(EntryTagger);
        r.Append("\n");
        r.Append("date ");
        r.Append(EntryDate);
        r.Append("\n");
        r.Append("message \n");
        r.Append(FormatMessage());
        r.Append("}
        ");
        return r.ToString();
    }