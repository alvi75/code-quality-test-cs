public virtual void AddIfNoOverlap(WeightedPhraseInfo wpi){
    foreach (WeightedPhraseInfo existWpi in phraseList){
        if (existWpi.IsNoOverlap(wpi)){
            existWpi.TermsInfos.AddRange(wpi.TermsInfos);
            return;
        }
        if (wpi.IsNoOverlap(existWpi)){
            AddPhraseInfo(existWpi);
        }
    }
}
}