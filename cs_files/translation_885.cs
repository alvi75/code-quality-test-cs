public virtual RevCommit TryFastForward(RevCommit newCommit){
    Ref @ref = repo.GetRef(Constants.R_HEADS);
    if (@ref == null){
        return newCommit;
    }
    RevWalk walk = new RevWalk(repo);
    walk.SetRetainBody(true);
    try{
        RefUpdate update = walk.UpdateRef(@ref.GetName(), false);
        update.SetForceUpdate(true);
        RevCommit headCommit = walk.ParseCommit(@ref.GetObjectId());
        if (IsMergeResult(walk.ParseCommit(newCommit.GetObjectId()), headCommit)){
            return newCommit;
        }
        if (!CanFastForward()){
            return newCommit;
        }
        string headName = GetHeadName(@ref);
        return TryFastForward(headName, walk.ParseCommit(@ref.GetObjectId()), newCommit);
    }