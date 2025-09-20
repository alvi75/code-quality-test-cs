1. **Understand the Task**: GroupGroupingsFacetsExample**;
GroupingSearch groupSearch = new GroupGroupingsFacetsExample();
groupGroupingsFacetsExample.setQueryConfig(termsWithScoreGroupField);
groupSearch.setGroupGroupSort(SortField.FIELD_NAME, true);
groupSearch.setGroupGroupDocsOffset(0);
groupSearch.setGroupGroupDocsLimit(10);
groupSearch.setGroupSort(null);
groupSearch.setGroupGroupDocsCount(true);
return groupSearch.execute();
}