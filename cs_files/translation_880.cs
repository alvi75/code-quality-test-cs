public static void SetupEnvironment(string[] workbookNames, IForkedEvaluator[] evaluators){
    if (workbookNames == null || evaluators == null || workbookNames.Length != evaluators.Length){
        throw new ArgumentException("Parameters must not be null, and workbookNames.length must equal evaluators.length.");
    }
    IForkedEvaluator[] wbEvals = new IForkedEvaluator[evaluators.Length];
    for (int i = 0;
    i < wbEvals.Length;
    i++){
        wbEvals[i] = evaluators[i].GetEvaluator();
    }
    CollaboratingWorkbookGroup.Setup(workbookNames, wbEvals);
}