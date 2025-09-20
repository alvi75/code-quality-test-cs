public override bool Equals(Object o){
    if (!(o is PropertySet))return false;
    PropertySet ps = (PropertySet)o;
    int byteOrder1 = ps.ByteOrder;
    int byteOrder2 = ByteOrder;
    ClassID classID1 = ps.ClassID;
    ClassID classID2 = ClassID;
    int format1 = ps.Format;
    int format2 = Format;
    int osVersion1 = ps.OSVersion;
    int osVersion2 = OSVersion;
    int sectionCount1 = ps.SectionCount;
    int sectionCount2 = SectionCount;
    if (byteOrder1 != byteOrder2 ||!classID1.Equals(classID2) ||format1 != format2 ||osVersion1 != osVersion2 ||sectionCount1 != sectionCount2)return false;
    return Util.AreEqual(Sections, ps.Sections);
}