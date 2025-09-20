public override void PreSerialize(){
    if (records.Tabpos > 0){
        TabIdRecord tdr = (TabIdRecord)records[records.Tabpos];
        if (tdr == null){
            tdr = new TabIdRecord();
            records.Add(records.Tabpos + 1, tdr);
        }
        ;
    }
    int idx = records.IndexOf(records.Tabid);
    records.Remove(idx);
}
}