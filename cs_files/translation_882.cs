public RandomSamplingFacetsCollector(int sampleSize, long seed){
    samplingRate = (1.0 * sampleSize) / (totalSize + 1);
    this.seed = seed;
}