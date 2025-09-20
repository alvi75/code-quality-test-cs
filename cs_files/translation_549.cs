public override TreeFilterTree Clone(){
    return new NGit.Revwalk.FollowFilter(RevFilterResult status = Follow(s, new ObjectId(), null);
    if (status == RevWalk.FORCED_FOLLOW)return new NGit.Revwalk.Follow(status.Tree);
}
else{
    if (status == RevWalk.NO_CHANGE){
        return this;
    }
    throw new NGit.Errors.NotSupportedException(MessageFormat.Format(JGitText.Get().cannotDetermineFollowModeFor, GetType().Name));
}
}