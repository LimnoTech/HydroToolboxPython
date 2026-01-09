Imports atcUSGSBaseflow
Imports atcData
Imports atcTimeseriesBaseflow
Imports atcTimeseriesRDB
Imports atcUtility
Imports DotSpatial.Controls
Imports DotSpatial.Extensions

Public Class ScriptRunnerDS

    Public Sub New()

        ' This call is required by the designer.
        InitializeComponent()

        ' Add any initialization after the InitializeComponent() call.
        RunBFI()

    End Sub

    Private Sub RunBFI()

        Dim lRDBFileName As String = "C:\temp\NWIS_discharge_02203655.rdb"
        Dim lRDBDataSource As New atcTimeseriesRDB.atcTimeseriesRDB()
        lRDBDataSource.Open(lRDBFileName)
        Dim lDataGroup As New atcData.atcTimeseriesGroup
        lDataGroup.Add(lRDBDataSource.DataSets(2))

        Dim lMethods As New ArrayList
        lMethods.Add(atcTimeseriesBaseflow.BFMethods.BFIStandard)

        Dim lArgs As New atcData.atcDataAttributes
        lArgs.SetValue("OutputDir", "C:\temp")
        lArgs.SetValue(atcTimeseriesBaseflow.BFInputNames.BFMethods, lMethods)
        lArgs.SetValue(atcTimeseriesBaseflow.BFInputNames.DrainageArea, 22.5)
        lArgs.SetValue(atcTimeseriesBaseflow.BFInputNames.StartDate, 37580)
        lArgs.SetValue(atcTimeseriesBaseflow.BFInputNames.EndDate, 45818)
        lArgs.SetValue(atcTimeseriesBaseflow.BFInputNames.Streamflow, lDataGroup)
        lArgs.SetValue(atcTimeseriesBaseflow.BFInputNames.EnglishUnit, True)
        lArgs.SetValue(atcTimeseriesBaseflow.BFInputNames.BFITurnPtFrac, 0.9)
        lArgs.SetValue(atcTimeseriesBaseflow.BFInputNames.Reportby, "Water")
        lArgs.SetValue(atcTimeseriesBaseflow.BFInputNames.BFINDayScreen, 5)
        lArgs.SetValue(atcTimeseriesBaseflow.BFInputNames.BFIReportby, "Water")
        lArgs.SetValue(atcTimeseriesBaseflow.BFInputNames.FullSpanDuration, False)

        atcUSGSBaseflow.modBaseflowUtil.ComputeBaseflowIntermittent(lArgs)

    End Sub
End Class
