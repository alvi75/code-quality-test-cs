public static int NumNonNulls(object[] data){
    var count = 0;
    foreach (object d in data){
        if (d != null){
            count++;
        }
    }
}
}