'''
Afshin Masoudi
CS50p/Problem Set 1/File Extensions
input : 'happy.jpg', 'document.pdf'
'''

font_extensions = {'ttf' : 'ttf',
                   'otf' : 'otf',
                   'woff' : 'woff',
                   'woff2' : 'woff2'}

video_extensions = {'avi' : 'x-msvideo',
                    'mp4' : 'mp4',
                    'mpeg' : 'mpeg',
                    'ogv' : 'ogg',
                    'ts' : 'mp2t',
                    '3gp' : '3gpp',
                    '3g2' : '3gpp2',
                    'webm' : 'webm'}

audio_extensions = {'aac' : 'aac',
                    'mid'  : 'midi,bx-midi',
                    'midi' : 'midi,bx-midi',
                    'oga' : 'ogg',
                    'mp3' : 'mpeg',
                    'opus' : 'opus',
                    'weba' : 'webm',
                    'wav' : 'wav',
                    'weba' : 'webm'}

image_extensions = {'avif' : 'avif',
                    'bmp' : 'bmp',
                    'gif' : 'gif',
                    'ico' : 'vnd.microsoft.icon',
                    'jpeg' : 'jpeg',
                    'jpg' : 'jpeg',
                    'png' : 'png',
                    'svg' : 'svg+xml',
                    'tif' : 'tiff',
                    'tiff' : 'tiff',
                    'webp' : 'webp'}

text_extensions = {'txt'  : 'plain',
                    'css' : 'css',
                    'csv' : 'csv',
                    'htm'  : 'html',
                    'html' : 'html',
                    'js' : 'javascript',
                    'mjs' : 'javascript',
                    'ics' : 'calendar'}

application_extensions = {'7z' : 'x-7z-compressed',
                        'xhtml' : 'xhtml+xml',
                        'xls' : 'vnd.ms-excel',
                        'xlsx' : 'vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                        'xml' : 'xml',
                        'xul' : 'vnd.mozilla.xul+xml',
                        'zip' : 'zip',
                        'pdf' : 'pdf',
                        'php' : 'x-httpd-php',
                        'ppt' : 'vnd.ms-powerpoint',
                        'pptx' : 'vnd.openxmlformats-officedocument.presentationml.presentation',
                        'rar' : 'vnd.rar',
                        'rtf' : 'rtf',
                        'sh' : 'x-sh',
                        'mpkg' : 'vnd.apple.installer+xml',
                        'odp' : 'vnd.oasis.opendocument.presentation',
                        'ods' : 'vnd.oasis.opendocument.spreadsheet',
                        'odt' : 'vnd.oasis.opendocument.text',
                        'bz' : 'x-bzip',
                        'bz2' : 'x-bzip2',
                        'cda' : 'x-cdf',
                        'csh' : 'x-csh',
                        'abw' : 'x-abiword',
                        'arc' : 'x-freearc',
                        'azw' : 'vnd.amazon.ebook',
                        'bin' : 'octet-stream',
                        'doc' : 'msword',
                        'docx' : 'vnd.openxmlformats-officedocument.wordprocessingml.document',
                        'eot' : 'vnd.ms-fontobject',
                        'epub' : 'epub+zip',
                        'gz' : 'gzip',
                        'jar' : 'java-archive',
                        'vsd' : 'vnd.visio',
                        'ogx' : 'ogg',
                        'tar' : 'x-tar',
                        'json' : 'json',
                        'jsonld' : 'ld+json'}

def answer(extension):
    if extension in image_extensions.keys():
        print(f"image/{image_extensions[extension]}")
    elif extension in text_extensions.keys():
        print(f"text/{text_extensions[extension]}")
    elif extension in video_extensions.keys():
        print(f"video/{video_extensions[extension]}")
    elif extension in audio_extensions.keys():
        print(f"audio/{audio_extensions[extension]}")
    elif extension in font_extensions.keys():
        print(f"font/{font_extensions[extension]}")
    elif extension in application_extensions.keys():
        print(f"application/{application_extensions[extension]}")
    else:
        print("application/octet-stream")

def main():
    filename = input("Please enter the name of a file: ").strip().lower().split('.')
    answer(filename[-1])

if __name__ == '__main__':
    main()