1. **Understand the Task**: Export DataExportSnapshot(exportImageExportTask request){
    var options = new InvokeOptions();
    options.RequestMarshaller = CreateExportExportTaskExportTaskExportTaskRequestMarshaller.Instance;
    options.ResponseUnmarshaller = CreateExportExportTaskExportResponseUnmarshaller.Instance;
    return Invoke<CreateExportTaskExportTaskResponse>(request, options);
}