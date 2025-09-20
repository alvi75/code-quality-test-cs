public override void SetByteValue(int index, int value){
    if (!IsIndexed || !index.IsIndexed){
        throw new System.NotSupportedException("cannot change value type from " + fieldsData.GetType().Name + " to Byte");
    }
    fieldsData = (byte)value;
}