1. Replace all occurrences of {
    {
        functionName}
    }
    _v{
        {
            versionNum}
        }
        VersionsVersions with UpdateFunctionVersionsResponseUnmarshaller.Instance;
        options.ResponseUnmarshaller = UpdateDashboardVersionsResponse.UpdateLifecycleVersionsResponseUnmarshaller.Instance;
        return Invoke<UpdateRuleVersionsResponse>(request, options);
    }