import json
import os


class DataHandle(object):
    def __init__(self, readfile, writefile):
        self.rf = readfile
        self.wf = writefile
        self.handle(self.rf, self.wf)

    @staticmethod
    def handle(rf, wf):
        if os.path.exists(wf):
            os.remove(wf)
        file = open(wf, encoding='utf-8', mode='w')
        with open(rf, encoding='utf-8') as f:
            for line in f.readlines():
                # print(line)
                # exit()
                line = json.loads(line)
                # print(line)
                value = line['meta']['accusation']
                # print(value)
                if len(value) == 1:
                    # print("aaa")
                    line_json = json.dumps(line, ensure_ascii=False)
                    file.writelines(line_json + '\n')
                # value = jieba.cut(value, cut_all=False)
                # value = " ".join(value)
                # file.writelines()

        file.close()


if __name__ == '__main__':
    path = 'All_legal_data.json'
    path_out = 'outAll_legal_data.json'
    try:
        DataHandle(path, path_out)
    except Exception as error:
        print(error)









