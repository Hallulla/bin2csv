# bintocsv for LowLatencyLogger
Simple Python script for converting large binary files generated using Gremain's <a href="https://www.w3schools.com/html/">SdFat library</a> LowLatencyLogger program to CSV(Comma Separated Values) files in your own computer.

The SdFat library allows great SD card write/read speeds using Arduino by writting data in binary format to the card using 12 512bit buffers. These files can be converted to CSV using the built in converter functions included in the LowLatencyLogger file but conversion times can be too long for big files. I needed a way to turn this data more quickly. In the future I might make this program do other more useful stuff like this:
- Add the recently converted data to a time series database such as influxDb for later analysis and recordkeeping.
- Text interface for command line use

Minor modifications may be required for this to work on your own CSV format.



