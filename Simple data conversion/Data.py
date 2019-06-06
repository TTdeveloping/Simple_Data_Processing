import os
import time
# input = './data.txt'
# output = './out_data.txt'


class Modification(object):
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
        self.handle(self.infile, self.outfile)

    @staticmethod
    def handle(path, out_path):
        """
        :param path:
        :param out_path:
        :return:
        """
        if os.path.exists(out_path):
            os.remove(out_path)
        file = open(out_path, encoding='utf-8', mode='w')
        with open(path, encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip()
                line = line.split()
                label = line[0]
                line = line[1:]
                line.append('|||')
                line.append(label)
                line = ' '.join(line)
                file.writelines(line + '\n')
        file.close()


if __name__ == "__main__":
    input = './data.txt'
    output = './out_data.txt'
    try:
        start_time = time.time()
        Modification(infile=input, outfile=output)
        end_time = time.time()
        print("Run Time {:.4f}s.".format(end_time - start_time))
        print("The Processing Is Over")
    except Exception as err:
        print(err)






