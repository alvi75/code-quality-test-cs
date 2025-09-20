public override string ToXml(string tabRecordName){
    StringBuilder sb = new StringBuilder();
    sb.Append("\n");
    sb.Append(" [").Append(RecordName).Append("]\n");
    foreach (EscherRecord r in EscherRecords){
        sb.Append(r.ToXml());
    }
    sb.Append("[/").Append(RecordName).Append("\n");
    return sb.ToString();
}