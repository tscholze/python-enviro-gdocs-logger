# Enviro HAT to Google Drive Sheets logger
> Uses the Pimoroni Enviro HAT to log specific values to a Google Drive Sheets document.

## Prerequirements
- Raspbian Linux
- Python (2/3)
- Installed pip packages: `envirophat`, `oauth2client`, `gspread`

## Before run
1. Enable Google Sheets API in the GDC
2. Download and move the`credentials.json` to the source directory
3. Enable Google Drive APO in the GDC (maybe not required)
4. Create a new service account in the GDC and download the json file.
5. Rename it to `client.json` and move it to the source directory
4. Create a new Google Sheet
5. Copy the key from the sheet's url into the source file
5. (Optional) Name the column header
6. (Optional) Add graphs to a new tablesheet but no the first

## Run
1. `cd <source folder>`
2. `python enviro-gdocs-logger.python`

It is recommended to run the script in a detachable shell session with screen or something similar.

The script will run after the delay that is defined in the source's constant `MINUTES_BETWEEN_SYNCS`. Default value is 15 minutes between a cycle run. 

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Dashboard")


# Stop
Hit `Cntrl+C` in the terminal that runs the staeted Python process.

## Contributing

This is a time-by-time sparetime project for myself. That means, no contribution is necessary.

## Authors

Just me, [Tobi]([https://tscholze.github.io).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
Dependencies or assets maybe licensed differently.