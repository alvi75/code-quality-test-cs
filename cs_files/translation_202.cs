public static int GetNearestSetSize(int maxNumberOfValuesExpected, float desiredSaturation){
    var usableBitSetSizes = new int[] {
        32, 64 }
        ;
        foreach (var usableBitSetSize in usableBitSetSizes){
            var numSetBitsAtDesiredSaturation = (int)(usableBitSetSize*desiredSaturation);
            var estimatedNumUniqueValues = GetEstimatedNumberUniqueValuesAllowingForCollisions(usableBitSetSize, numSetBitsAtDesiredSaturation);
            if (estimatedNumUniqueValues>maxNumberOfValuesExpected){
                return usableBitSetSize;
            }
            else if ((numSetBitsAtDesiredSaturation & 0x7ffffffe) != 0){
                return usableBitSetSize + 1;
            }
            else{
                return usableBitSetSize;
            }
        }