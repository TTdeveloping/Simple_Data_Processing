import json
import os


class DataHandle(object):
    def __init__(self, readfile, writefile, accfile,countfile):
        self.rf = readfile
        self.wf = writefile
        self.cf = countfile
        self.af = accfile
        self.accu_dict = {}
        self.accu_list = self.getlist(self.af)
        self.process(self.accu_list, self.rf, self.wf)
        self.getcount(self.accu_dict, self.cf)
        # print(self.accu_dict)

    def getcount(self, accu_dict, countpath):
        if os.path.exists(countpath):
            os.remove(countpath)
        file = open(countpath, encoding='utf-8', mode='w')
        for k, v in accu_dict.items():
            file.writelines(k + "\t" + str(v) + '\n')
        file.close()

    def process(self, accu_list, in_path, out_path):
        # 遍历 accu_list
        for accu in accu_list:
            print(accu)
            # print(out_path)
            out_final_path = out_path + "_" + accu + ".json"
            # print(out_final_path)
            self.handle(in_path, out_final_path, accu)

    @staticmethod
    def getlist(af):
        list = []
        with open(af, encoding='utf-8') as f:
            for line in f.readlines():
                line =line.strip()
                list.append(line)
        return list

    def handle(self, rf, wf, accu):
        if os.path.exists(wf):
            os.remove(wf)
        file = open(wf, encoding='utf-8', mode='w')
        with open(rf, encoding='utf-8') as f:
            count = 0
            for line in f.readlines():
                # print(line)
                # exit()
                line = json.loads(line)
                # print(line)
                value = line['meta']['accusation']
                # print(value)
                # if len(value) == 1 and value[0] == accu:
                if accu in value:
                    count += 1
                    line_json = json.dumps(line, ensure_ascii=False)
                    file.writelines(line_json + '\n')
            self.accu_dict[accu] = count
        file.close()


if __name__ == '__main__':
    path = 'All_legal_data.json'
    path_out = 'out_data/legal_data'
    accu_path = 'accu.txt'
    countpath = 'count.txt'

    try:
        DataHandle(path, path_out, accu_path,countpath)
    except Exception as error:
        print(error)









