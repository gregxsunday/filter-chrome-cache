from os import listdir
import argparse

def filter_bytes(infile, offset=24):
    nonascii = bytearray(range(0x20)) + bytearray(range(0x80, 0x100))

    with open(infile, 'rb') as infile:
        infile.seek(offset)
        return infile.readline().translate(None, nonascii).decode('utf-8')

def extension_index(url):
    extensions = ['.css', '.png', '.js', '.gif', '.jpg', '.do', '.html', '.jsp', '.min', '.ttf', '.woff', '.ico', '.aspx', '.txt']

    end = len(url)
    for ext in extensions:
        index = url.find(ext)
        if index != -1:
            potential_end = index + len(ext)
            end = min(potential_end, end)
    return end

def terminator_index(url):
    terminators = ['<!--', '?', '<', '>', 'META-INF', 'WEB-INF', '#', 'HTTP/1.1', '{', '*', ',', ' ', '$', '}', '{}']

    end = len(url)
    for term in terminators:
        index = url.find(term)
        if index != -1:
            potential_end = index
            end = potential_end if potential_end < end else end
    return end

def cut_url(url):
    url = url[url.find('http'):] if url.find('http') != -1 else url

    ext = extension_index(url)
    terminator = terminator_index(url)
    return url[:min(ext, terminator)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='The script returns the source url of every file with cached data from google chrome. The format is "FILENAME URL" Keep in mind, that the url may have some trash appended. Suggested usage is grepping the tested domain and reviewing the cache manually.')
    parser.add_argument('--path', help='usually something like ~/.cache/google-chrome/Profile 1/Cache/ for chrome', required=True)
    args = parser.parse_args()

    #folder with cached files
    path = args.path
    #url is not at the beginning of the file, thus offset
    offset = 24

    #files with cache have _ in the filename
    files_filtered = list(filter(lambda x: '_' in x, listdir(path)))

    print('FILENAME', 'CACHED FROM URL', sep=' '*(len('0d9af11944673918_0') - len('FILENAME') + 1))
    for file in files_filtered:
        url = filter_bytes(path + file, offset)
        print(file, cut_url(url), sep=' ')

