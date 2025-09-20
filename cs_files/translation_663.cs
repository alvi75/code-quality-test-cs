public static PredictionContext FromRuleContext(Parser_4_ATNConfig(config, context){
    if (context == null){
        return PredictionContext.EMPTY;
    }
    if (config == null){
        return PredictionContext.FromRuleContext(null, ATNState.InvalidStateNumber, context);
    }
    else {
        return new SingletonPredictionContext(config, context);
    }
}