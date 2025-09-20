public IDataValidationConstraint CreateTimeConstraint(int operatorType, String formula1, String formula2){
    return DVConstraint.CreateTimeConstraint(operator, formula1, formula2);
}