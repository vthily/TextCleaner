from cleaner import Clean

# output_path = './output/'
# input_path = './input/'
# text = open(input_path + 'demofile.txt', 'r').read()
#
# cleaner = Clean()
#
# text_cleaned = cleaner.clean(text, output_path, 'demodebug.txt', debug=1)
# cleaner.checksample(text_cleaned, output_path, 'checktruth.txt',)
#
#
# output_file = open(output_path + 'demooutput.txt', 'w+')
# output_file.write(text_cleaned)
# output_file.close()


class CleanStart(object):
    cleaner = Clean()

    def run(self, text):
        text_cleaned = self.cleaner.clean_server(text)
        return text_cleaned
