import youtube_dl
import sys
import getopt


class Download():

    def __init__(self, argv):
        self.url = ''
        self.output_dir = ''
        self.params = []

        try:
            opts, args = getopt.getopt(
                argv, "hu:o:p:", ["url=", "output=", "params="])
        except getopt.GetoptError:
            print('download.py -u <url> -o <outputfile> -p <params>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('download.py -i <inputfile> -o <outputfile> -p <params>')
                sys.exit()
            elif opt in ("-u", "--url"):
                self.url = arg
            elif opt in ("-o", "--output"):
                self.output_dir = arg
            elif opt in ("-p", "--params"):
                self.params = [*arg.split(',')]

    def show_args(self):
        print('url', self.url)
        print('output', self.output_dir)
        print('params', self.params)

    def run(self):
        youtube_dl.main([self.url])


if __name__ == "__main__":
    dl = Download(sys.argv[1:])
    dl.main()
