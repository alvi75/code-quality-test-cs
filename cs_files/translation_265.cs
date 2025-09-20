public override String ToString(){
    StringBuilder buffer.Append(this.GetType().Name).Append(" [");
    Array.Append(Range.ToString());
    sb.Append("]");
    sb.Append(FormatString);
    return sb.ToString();
}