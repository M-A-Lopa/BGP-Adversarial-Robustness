"""
collectors/ — BGP data collection and parsing from Route Views and RIPE RIS.

Modules:
    mrt_parser.py       Parse MRT-format BGP update files using mrtparse
    feature_extractor.py  Extract the 37 per-minute features from parsed
                          MRT data (same 37 columns as the SFU CSV files)
    routeviews.py       Download and manage Route Views archive data
    ripe_ris.py         Download and manage RIPE RIS archive data
    downloader.py       Common download utilities for both collectors

Data flow:
    Raw MRT files → mrt_parser → feature_extractor → 37-feature CSV
    (This replicates the original SFU feature-extraction pipeline)
"""
