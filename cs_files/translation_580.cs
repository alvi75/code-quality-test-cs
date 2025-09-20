public static void RegisterMergeStrategy(MergeStrategy mergeStrategy){
    if (mergeStrategies.Contains(mergeStrategy)){
        String name = mergeStrategy.GetType().Name;
        lock (typeof(MergeStrategyRegistry)){
            if (mergeStrategyRegistry.ContainsKey(name)){
                throw new ArgumentException("Merge strategy with same name already registered: " + name);
            }
            else{
                mergeStrategyRegistry[name] = mergeStrategy;
            }
        }
    }
}