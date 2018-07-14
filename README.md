# Frequency Analysis of Words
---
## Module **lang_frequency.py** returns the most common words in text
---

### Discription
+ Specify the path to start
+ The script will print words and their number
+ You can change the number of words
+ Requrements: arguments for start to script "path"

### Script usage example
```python
import lang_frequency
text = lang_frequency.load_data("you_file.txt")
most_frequent_words = lang_frequency.get_most_frequent_words(text, 10)
lang_frequency.pprint_words(most_frequent_words)
```

### How starting
```bash
$ python lang_frequency.py exemple.txt
```

### Example result
```bash
и : 708
не : 634
в : 624
что : 469
```

##  Where to get data:
You can take any text file

### Requirements
```bash
Python ver 3.5 (or higher)
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
