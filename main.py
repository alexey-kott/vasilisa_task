import pandas as pd

if __name__ == "__main__":
    pd.set_option('display.max_colwidth', -1)
    df = pd.read_csv('log.csv', low_memory=False)
    # print(df.columns.values)
    print(df)

    'UserID' 'ConversionID' 'ConversionDate' 'AgencyID' 'AgencyName'
    'DeviceType' 'OperatingSystemType' 'BrowserType' 'Country' 'State-Region'
    'DMA' 'City' 'ZIPPostalCode' 'AreaCode' 'HasPaidSearch' 'HasPaidDisplay'
    'HasPaidRichMedia' 'HasPaidSocial' 'HasSiteVisitNaturalSearch'
    'HasSiteVisitSocial' 'HasSiteVisit' 'AdvertiserID' 'AdvertiserName'
    'ConversionTagID' 'ConversionTagName' 'CountConversionsSetting'
    'Quantity' 'Value' 'OrderID' 'ProductID' 'ProductInfo' 'Currency'
    'QueryString' 'WinningEventType' 'WinningEventDate'
    'WinningEventEntityID' 'WinningEventEntityType' 'WinningAdFormatID'
    'WinningAdFormatName' 'WinningSectionName' 'WinningCampaignID'
    'WinningCampaignName' 'WinningDisplaySiteID/WinningSearchEngineID'
    'WinningDisplaySiteName/WinningSearchEngineName' 'WinningWasDwelled'
    'WinningWasVideoStarted' 'WinningWasVideoCompleted'
    'WinningDidUserInteract' 'WinningDidUserExpand' 'WinningDidAutoExpand'
    'WinningWasViewable' 'WinningDisplayPlacementID\\WinningSearchKeywordID'
    'WinningPlacementName/WinningSearchKeywordName'
    'WinningDisplayAdID/WinningSearchAdID'
    'WinningDisplayAdName/WinningSearchAdName' 'WinningSearchAdGroupID'
    'WinningSearchAdGroupName' 'WinningSearchMatchType'
    'WinningMediaBuyChannel' 'WinningClickthroughURL' 'WinningPackageID'
    'WinningPackageName' 'WinningBrand' 'WinningVersionClassificationID'
    'WinningVersionClassificationName' 'WinningTargetAudienceID'
    'WinningTargetAudienceName' 'WinningPCP'
    'WinningDisplayCampaignStartDate/WinningSearchCampaignStartDate'
    'WinningDisplayCampaignEndDate/WinningSearchCampaignEndDate'
    'WinningUnitSize' 'WinningSiteVisitEventDate'
    'WinningSiteVisitClassification' 'WinningSiteVisitReferralDomain'
    'WinningNaturalSearchKeyword' 'EventType' 'EventDate' 'EntityID'
    'EntityType' 'ConversionTimeLag' 'WinnerEventTimeLag' 'AdFormatID'
    'AdFormatName' 'SectionName' 'CampaignID' 'CampaignName'
    'DisplaySiteID/SearchEngineID' 'DisplaySiteName/SearchEngineName'
    'WasDwelled' 'WasVideoStarted' 'WasVideoCompleted' 'DidUserInteract'
    'DidUserExpand' 'DidAutoExpand' 'WasViewable'
    'DisplayPlacementID\\SearchKeywordID' 'PlacementName/SearchKeywordName'
    'DisplayAdID/SearchAdID' 'DisplayAdName/SearchAdName' 'SearchAdGroupID'
    'SearchAdGroupName' 'SearchMatchType' 'MediaBuyChannel' 'ClickthroughURL'
    'PackageID' 'PackageName' 'Brand' 'VersionClassificationID'
    'VersionClassificationName' 'TargetAudienceID' 'TargetAudienceName' 'PCP'
    'DisplayCampaignStartDate/SearchCampaignStartDate'
    'DisplayCampaignEndDate/SearchCampaignEndDate' 'UnitSize'
    'SiteVisitEventDate' 'SiteVisitClassification' 'SiteVisitReferralDomain'
    'NaturalSearchKeyword'