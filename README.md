# Removes HTML tags from a column in a .csv file 

## About :
The python script runs 2 versions of cleaning and returns a file with 4 additional columns:

1. **Regex matching** with "<>" , "&;"(with 4 or 5 characters in between) anything in between will be removed and "\\*" will be replaced with a white space character. **Note: the special characters will simply be removed.** eg: \&nbsp; \&rpos; etc.
2. **BeautifulSoup** HTML to text conversion. This will remove HTML tags and convert special characters into their respective ASCII characters
3. 2 parity columns which will return the difference in the number of charcters between the newly generated columns and the original columns. (This is basically a flag that you can check if there has been too many characters replaced)

## How to use

1. Place the file in the same directory as the csv file
2. open terminal and type: python remove_html.py
3. Follow the instructions!
4. You are done.

## Future plans
1. Auto detect filetype
2. multicolumn support
