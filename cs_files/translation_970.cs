public override string ToString(){
    StringBuilder buffer.Append("[SXDI]\n");
    for (int i = 0;
    i < fieldInfos.Length;
    i++){
        fieldInfos[i].AppendDebugInfo(sb);
    }
    else{
        sb.Append(" .sxaxis = ").