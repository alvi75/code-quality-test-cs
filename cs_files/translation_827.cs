public override bool Equals(object o){
    if (!(o is Group)){
        return false;
    }
    var group = o as Group;
    if (group == null)return false;
    return group.Name.Equals(this.groupName, StringComparison.Ordinal);
}