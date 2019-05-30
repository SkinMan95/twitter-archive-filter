# Twitter Archive Filter

This software decompresses and filters Twitter feeds from the 
[Archive](https://archive.org/search.php?query=collection%3Atwitterstream&sort=-publicdate&page=2) website.

:star: **Recommendation**: when downloading files from the Archive website use a Torrent client (such as 
[qBittorrent](https://www.qbittorrent.org/)) as it will check for files integrity and retry on damaged 
pieces when downloading.

This product is one of various for my thesis project. 

Feel free to use it anytime, and any reference to the original author is welcome! :sunglasses:

## Requirements
In order to use this software you must install the following dependencies:
* bash
* Python 3.4+
* [GNU Parallel](https://www.gnu.org/software/parallel/)

You can install GNU Parallel by doing (Debian distributions like Ubuntu):
```bash
$ sudo apt install parallel
$ parallel --citation # this step is for removing annoyng messages of GNU Parallel
# type "will cite"
```

## Execution
This software is divided into different parts:

### uncompress.sh
Assuming that this file is in the same directory of the downloaded **tars** from the Archive website you can execute it as:

:warning: Be aware, as this software will uncompress every tar file that it finds into the **bz2** files that are inside
and each of those uncompressed will weight **~10x** their original sizes, meaning that if you downloaded **50GB**, 
decompressing them will yield more than **500GB**. Also this will take cosiderable time to finish since it is 
reading and writting on the same disk a considerable amount of data.

```bash
chmod +x uncompress.sh
./uncompress.sh
```

### filter-tweets.py
Prior to execution you need to generate a file called **json-files.txt**, you can generate this file by doing:
```bash
$ find -type f -iname '*.json' > json-files.txt
```

To execute this program you can do:
```bash
python3 filter-tweets.py
```

This will generate a file called **out.dat** that contains the filtered data, in this case it uses 
**colombia-lugares.txt** to filter the tweets, if it finds anything that contains something that is mentioned in
this file it will include it in the output.

## TODOs
- [ ] Implement the filter without having to decompress all the data in a location, maybe just in RAM.
- [ ] Implement some kind of buffered writter that will hold some information until it is full, then write it to disk. 
- [ ] Add CLI options to let the user specify different parameters instead of changing them in the script.

## Author
**Alejandro Anzola**, Computer Science student

Escuela Colombiana de Ingenieria Julio Garavito

Bogota, Colombia
