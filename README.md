# bin2csv
Simple Python script for converting large binary files generated using Gremain's <a href="https://www.w3schools.com/html/">SdFat library</a> LowLatency logger program to CSV(Comma Separated Values) files in your own computer.

The SdFat library allows great SD card write/read speeds using Arduino by writting data in binary format to the card using 12 512bit buffers. These files can be converted to CSV using the built in converter functions included in the LowLatencyLogger file but it can take a long time if you have a lot of data. This script allows you keep the binary files for faster convertion in a PC.

Minor modifications may be required for this to work on your own CSV format.

May be added in the future: 
- Text interface for command line use
- Integration with time series database such as influxDb
