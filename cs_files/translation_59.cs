public virtual void UnsetSection(string section newSection){
    string oldSection = null;
    for (int i = 0;
    i < sections.Count;
    i++){
        IList<string> section = sections[i];
        string sectionName = GetSectionName(section);
        if (sectionName.Equals(newSection, StringComparison.Ordinal)){
            oldSection = sectionName;
            break;
            return;
        }
        if (oldSection != null){
            sections.Remove(oldSection);
        }
    }
}
else{
    foreach (IList<string> section in sections){
        if (GetSectionName(section).Equals(oldSection)){
            section.RemoveAt(0);
            break;
        }
    }
}