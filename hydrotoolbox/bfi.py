import logging
import os
import pathlib

LOGGER = logging.getLogger(__name__)

import System

import atcTimeseriesRDB
import atcData
import atcUSGSBaseflow
import System.Collections
import atcTimeseriesBaseflow
from atcTimeseriesBaseflow import BFInputNames as BFInputNames


def bfi_from_rdb(
    input_path: os.PathLike,
    output_dir: os.PathLike = ".\Output",
) -> None:
    LOGGER.debug("BFI function called.")

    # sanitize input path
    input_path = pathlib.Path(input_path)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file {input_path} does not exist.")

    data_source: atcTimeseriesRDB.atcTimeseriesRDB = atcTimeseriesRDB.atcTimeseriesRDB()
    # This method does not return exception for invalid path, so we might need to handle that in python
    try:
        data_source.Open(str(input_path))
    except System.ApplicationException:
        raise RuntimeError(f"Error loading data from RBD file {input_path}")

    # Prepare data group
    data_group: atcData.atcDataGroup = atcData.atcDataGroup()
    # TODO: We either need dataset index as an argument or we more likely remove
    # this function and make a general rdp read function that returns the dataset object
    # and let the user pass that to the generalized bfi function below.
    data_group.Add(data_source.DataSets[2])

    return bfi(data_group, output_dir=output_dir)


def bfi(
    input_data: atcData.atcTimeseries,
    output_dir: os.PathLike = ".\Output",
) -> None:
    # sanitize output directory
    output_dir = pathlib.Path(output_dir)
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
    if not output_dir.is_dir():
        raise NotADirectoryError(f"Output directory {output_dir} is not a directory.")

    methods = System.Collections.ArrayList()
    methods.Add(atcTimeseriesBaseflow.BFMethods.BFIStandard)

    args = atcData.atcDataAttributes()
    args.SetValue("OutputDir", str(output_dir))
    args.SetValue(BFInputNames.BFMethods, methods)
    args.SetValue(BFInputNames.DrainageArea, 22.5)
    args.SetValue(BFInputNames.StartDate, 37580)
    args.SetValue(BFInputNames.EndDate, 45818)
    args.SetValue(BFInputNames.Streamflow, input_data)
    args.SetValue(BFInputNames.EnglishUnit, True)
    args.SetValue(BFInputNames.BFITurnPtFrac, 0.9)
    args.SetValue(BFInputNames.Reportby, "Water")
    args.SetValue(BFInputNames.BFINDayScreen, 5)
    args.SetValue(BFInputNames.BFIReportby, "Water")
    args.SetValue(BFInputNames.FullSpanDuration, False)

    util = atcUSGSBaseflow.modBaseflowUtil()
    util.ComputeBaseflowIntermittent(args)
