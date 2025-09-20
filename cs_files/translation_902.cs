public override bool IsSaturated(FuzzySet bloom, FieldInfo fieldInfo){
    return bloom.IsSaturationHigh(fieldInfo);
}