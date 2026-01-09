from hydrotoolbox import bfi


def main():
    import atcTimeseriesRDB
    import atcData
    import atcUSGSBaseflow
    import System.Collections
    import atcTimeseriesBaseflow
    from atcTimeseriesBaseflow import BFInputNames as BFInputNames

    path: str = R"C:\Users\ptomasula\Repositories\HydroToolboxWrapper\bfi_example\NWIS_discharge_02203655.rdb"
    data_source: atcTimeseriesRDB.atcTimeseriesRDB = atcTimeseriesRDB.atcTimeseriesRDB()
    # This method does not return exception for invalid path, so we might need to handle that in python
    data_source.Open(path)

    data_group: atcData.atcDataGroup = atcData.atcDataGroup()
    data_group.Add(data_source.DataSets[2])

    methods = System.Collections.ArrayList()
    methods.Add(atcTimeseriesBaseflow.BFMethods.BFIStandard)

    args = atcData.atcDataAttributes()
    args.SetValue("OutputDir", R"C:\Temp")
    args.SetValue(BFInputNames.BFMethods, methods)
    args.SetValue(BFInputNames.DrainageArea, 22.5)
    args.SetValue(BFInputNames.StartDate, 37580)
    args.SetValue(BFInputNames.EndDate, 45818)
    args.SetValue(BFInputNames.Streamflow, data_group)
    args.SetValue(BFInputNames.EnglishUnit, True)
    args.SetValue(BFInputNames.BFITurnPtFrac, 0.9)
    args.SetValue(BFInputNames.Reportby, "Water")
    args.SetValue(BFInputNames.BFINDayScreen, 5)
    args.SetValue(BFInputNames.BFIReportby, "Water")
    args.SetValue(BFInputNames.FullSpanDuration, False)

    util = atcUSGSBaseflow.modBaseflowUtil()
    util.ComputeBaseflowIntermittent(args)

    pass


if __name__ == "__main__":
    main()
