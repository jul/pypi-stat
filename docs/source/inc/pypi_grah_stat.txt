Usage: pypi_graph_stat.py [options]

Options:
  -h, --help            show this help message and exit
  -k KEY                keys to plot in stored stats amongst av_dl, total_dl,
                        min_dl','max_dl'
  -f _FROM, --from=_FROM
                        min date from which to plot
  -t _TO, --to=_TO      maximum date to which to plot
  -o _DEST, --output=_DEST
                              filename of the output image. Don't create
                        output directory if non existant. If this is enabled
                        output in TK backend is desactivated.
  -p _PACKAGE, --package=_PACKAGE
                        packages for wich to graph
