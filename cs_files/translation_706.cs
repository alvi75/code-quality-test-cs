public override string ToString(){
    StringBuilder sb = new StringBuilder("[");
    foreach (object item in this){
        if (sb.Length > 1){
            sb.Append(", ");
        }
        if (item is char[]){
            sb.Append((char[])item);
        }
        else{
            sb.Append(item.ToString());
        }
    }