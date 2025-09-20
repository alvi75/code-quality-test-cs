public virtual NGit.Storage.Pack.IndexWriterConfig FromConfig(Config rc){
    NGit.Storage.Pack.IndexWriterConfig iwConf = new NGit.Storage.Pack.IndexWriterConfig(m_config);
    iwConf.MergePolicy = MergePolicy.FromString(rc.Get("merge.policy", "Lucene.Net.Index.KeepOnlyLastCommitMergePolicy"));
    string mergeScheduler = rc.Get("merge.scheduler","Lucene.Net.Index.ConcurrentMergeScheduler, Lucene.Net");
    #if !FEATURE_CONCURRENTMERGESCHEDULERif (mergeScheduler.Contains(".ConcurrentMergeScheduler,")){
        mergeScheduler = "Lucene.Net.Index.TaskMergeScheduler, Lucene.Net";
    }