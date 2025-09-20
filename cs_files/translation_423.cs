1. Open the workbook in read-write mode){
    workbook = XSSFWorkbook.createWorkbook(workbook.getStub());
}
for (HSSFSheet sheet : _sheets) {
    HSSFSheet hs = (HSSFSheet)sheet;
    hs.setSheetName(sheet.getName());
    HSSFWorkbook wb = hs.getWorkbook();
    if (wb != null) {
        HSSFWorkbook nwb = XSSFWorkbook.createWorkbook(wb.getStub());
        nwb.setWorkbookProperties(wb.getWorkbookProperties());
        _workbookRecordList.add(RecordCreator.createWorkbookRecord(nwb));
    }
}
);
}