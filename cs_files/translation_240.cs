public void SetRule(int idx, HSSFConditionalFormattingRule cfRule){
    cfAggregate.SetRule(idx, cfRule.CfRuleRecord);
}