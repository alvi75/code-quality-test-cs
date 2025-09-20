public override string ToString(){
    string coll = _collectionModel.GetName();
    if (coll != null){
        return string.Format("LM {
            0}
            - {
                1}
                ", Name, coll);
            }
            else{
                return string.Format("LM {
                    0}
                    ", Name);
                }
            }