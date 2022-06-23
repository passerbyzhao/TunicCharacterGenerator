import turtle as tt
import eng_to_ipa
import re


tttttt = 'ˈ\\ˌ\\*(应该是指不存在)\\'
# 行间距0.2字符 单词间距0.5字符 句子间距1字符


def BasicTunicSymbol(draw_symbol, input, base_point, style='formal'):
    """
    draw_symbol为下级符号绘制方法
    input为单个音标组列表
    base_point为当前字符原点
    """
    vowel_dic = {
        'æ': [1, 2, 11],
        'ɑr': [1, 2, 6, 7],
        'ɑ': [1, 11],
        'ɔ': [1, 11],
        'eɪ': [1],
        'ɛ': [6, 7, 11],
        'i': [1, 6, 7, 11],
        'ɪr': [1, 7, 11],
        'ə': [1, 2],
        'ɛr': [7, 11],
        'ɪ': [6, 7],
        'aɪ': [2],
        'ər': [2, 6, 7, 11],
        'oʊ': [1, 2, 6, 7, 11],
        'ɔɪ': [6],
        'u': [1, 2, 6, 11],
        'ʊ': [6, 11],
        'aʊ': [7],
        'ʊr': [1, 2, 7, 11]

    }
    consonant_dic = {
        'b': [5, 9],
        'ʧ': [3, 10],
        'd': [5, 8, 9],
        'f': [4, 8, 10],
        'g': [4, 9, 10],
        'h': [5, 9, 10],
        'ʤ': [5, 8],
        'k': [4, 5, 9],
        'l': [5, 10],
        'm': [8, 9],
        'n': [3, 8, 9],
        'ŋ': [3, 4, 5, 8, 9, 10],
        'p': [4, 10],
        'r': [4, 5, 10],
        's': [4, 5, 8, 10],
        'ʃ': [3, 4, 8, 9, 10],
        't': [3, 4, 10],
        'θ': [3, 4, 5, 10],
        'ð': [5, 8, 9, 10],
        'v': [3, 5, 9],
        'w': [3, 4],
        'j': [3, 5, 10],
        'z': [3, 5, 9, 10],
        'ʒ': [3, 4, 5, 8, 9]
    }
    num_list = [0] if style == 'formal' else []     # 只有书面写法有横杠0
    if input[0]:  # 有没有元音
        num_list.extend(vowel_dic[input[0]])
    if input[1]:  # 有没有辅音
        num_list.extend(consonant_dic[input[1]])
    if input[2]:  # 有没有顺序反转
        num_list.append(12)
    draw_symbol(num_list, base_point)


class Division:
    """
    divider方法将句子分割为单词 返回双层列表
    """
    def __init__(self):
        pass

    def inputchecker(self, sentence):
        import re
        tmp = re.search(r'[^a-zA-Z,\.!\?\'\n\s]', sentence)
        if tmp != None:
            raise ValueError('有不支持的字符{}，请重新输入！'.format(tmp[0]))

    def divider(self, sentence):
        self.inputchecker(sentence)
        s_list = re.split('\n|\.|,|\!|\?', sentence)
        while '' in s_list:
            s_list.remove('')
        final_list = []
        for subsentence in s_list:
            tmp_list = re.split(' |\'', subsentence)
            while '' in tmp_list:
                tmp_list.remove('')
            if tmp_list != []:
                final_list.append(tmp_list)
        return final_list


class MiddleReplace:
    def __init__(self, word_list, phoneme):
        self.word_list = word_list
        self.phoneme = phoneme

    def checker(self):
        for subsen in self.word_list:
            for word in subsen:
                if not eng_to_ipa.isin_cmu(word):
                    raise Exception('{}未找到对应读音'.format(word))

    def wordtophoneme(self, debug=False):
        phoneme_list = []
        for subsen in self.word_list:
            sub_tmp_list = []
            for word in subsen:
                p = self.phoneme.process(word, debug)
                sub_tmp_list.append(p)
            phoneme_list.append(sub_tmp_list)
        return phoneme_list


class SetCanvas:
    def __init__(self, fontsize):
        self.iW = fontsize * 2 * 1.73205  # 单个字符宽度
        self.iH = fontsize * 7 * 1  # 单个字符高度(3+4)
        self.W = tt.window_width()
        self.H = tt.window_height()
        self.fontsize = fontsize

    def setcanvas(self, reshaped_phoneme_list):
        w = max([len(i) for i in reshaped_phoneme_list])
        h = len(reshaped_phoneme_list)
        if self.iH * h * 1.2 > self.H:
            raise Exception('字号过大或单词数过多，请重新输入')
        # tt.screensize(self.W, self.H)
        tt.setworldcoordinates(self.fontsize * (2 * -1.73205), -self.H + self.fontsize * 4,
                               self.W - self.fontsize * (2 * -1.73205), self.fontsize * 4)
        return w, h, self.iW, self.iH, self.W, self.H

    def reshapelist(self, phoneme_list):
        threshold = self.W / self.iW
        scale = 0.8
        reshap_list = []
        for sen in phoneme_list:
            for word in sen:
                for phon in word:
                    reshap_list.append(phon)
                reshap_list.append('')
            reshap_list.append(' ')
        reshaped_list = []
        cnt = 0
        tmp_list = [0]
        for i in range(0, len(reshap_list)):
            cnt += 1
            if cnt > threshold * scale:
                if reshap_list[i] == '' or reshap_list[i] == ' ':
                    tmp_list.append(i)
                    cnt = 0

        # if len(tmp_list) == 1:
        #     tmp_list.append(-1)
        tmp_list.append(-1)
        # print('一共{}行'.format(tmp_list))
        # print('一行{}字符'.format(threshold))
        for i in range(1, len(tmp_list)):
            reshaped_list.append(reshap_list[tmp_list[i - 1]:tmp_list[i]])
        return reshaped_list


class Phoneme:
    """
    输入word为准备翻译的词汇
    使用process方法输出分隔好的音标列表
    """

    def __init__(self):

        self.vowel_list = ['æ', 'ɑr', 'ɑ', 'ɔ',
                           'eɪ', 'ɛ', 'i', 'ɪr',
                           'ə', 'ɛr', 'ɪ', 'aɪ',
                           'ər', 'oʊ', 'ɔɪ', 'u',
                           'ʊ', 'aʊ', 'ə', 'ʊr']
        self.consonant_list = ['b', 'ʧ', 'd', 'f', 'g',
                               'h', 'ʤ', 'k', 'l', 'm',
                               'n', 'ŋ', 'p', 'r', 's',
                               'ʃ', 't', 'θ', 'ð', 'v',
                               'w', 'j', 'z', 'ʒ']

    def _is_diphthong(self, letters):
        """
        0为辅音 1为单元音 2为双元音
        """
        if letters[0]+letters[1] in self.vowel_list:
            try:
                if letters[1] == 'r':
                    if letters[2] in self.vowel_list or letters[2] in ['e', 'a', 'o']:
                        return 1
            except:
                pass
            return 2
        elif letters[0] in self.vowel_list:
            return 1
        elif letters[0] in self.consonant_list:
            return 0
        raise ValueError('音标{}不存在！'.format(letters[0:2]))

    def process(self, word, debug=False):  # 将音标分组
        phoneme = eng_to_ipa.convert(word, stress_marks=0)
        if debug:
            print('单词：{} 音标：{}'.format(word, phoneme))
        if len(phoneme) <= 0:
            raise Exception('{}音标无法获取：{}'.format(word, phoneme))
        phoneme_list = list(phoneme)
        result = []
        while len(phoneme_list) > 0:
            if len(phoneme_list) == 1:
                if phoneme_list[0] in self.vowel_list:  # 单元音
                    result.append([phoneme_list[0], '', 0])
                    return result
                elif phoneme_list[0] in self.consonant_list:  # 单辅音
                    result.append(['', phoneme_list[0], 0])
                    return result
                raise ValueError('音标{}不存在！'.format(phoneme_list[0]))
            elif len(phoneme_list) == 2:
                tmp_code = self._is_diphthong(phoneme_list)
                if tmp_code == 2:  # 双元音
                    result.append([phoneme_list[0] + phoneme_list[1], '', 0])
                    return result
                elif tmp_code == 1:  # 先元后辅
                    if phoneme_list[1] in self.consonant_list:
                        result.append([phoneme_list[0], phoneme_list[1], 1])
                        return result
                    raise ValueError('音标{}不存在！'.format(phoneme_list[0] + phoneme_list[1]))
                elif tmp_code == 0:
                    if phoneme_list[1] in self.vowel_list:  # 先辅后元
                        result.append([phoneme_list[1], phoneme_list[0], 0])
                        return result
                    elif phoneme_list[1] in self.consonant_list:  # 双辅音
                        result.append(['', phoneme_list[0], 0])
                        result.append(['', phoneme_list[1], 0])
                        return result
                    raise ValueError('音标{}不存在！'.format(phoneme_list[0] + phoneme_list[1]))
            else:  # 剩余长度大于等于3
                tmp_flag = self._is_diphthong(phoneme_list)
                if tmp_flag == 0:  # 以辅音开头
                    tmp_code = self._is_diphthong(phoneme_list[1:])
                    if tmp_code == 2:  # 辅音+双元音
                        result.append([phoneme_list[1] + phoneme_list[2], phoneme_list[0], 0])
                        phoneme_list.pop(0)
                        phoneme_list.pop(0)
                        phoneme_list.pop(0)
                    elif tmp_code == 1:  # 先辅后元
                        result.append([phoneme_list[1], phoneme_list[0], 0])
                        phoneme_list.pop(0)
                        phoneme_list.pop(0)
                    elif tmp_code == 0:  # 单辅音
                        result.append(['', phoneme_list[0], 0])
                        phoneme_list.pop(0)
                elif tmp_flag == 1:  # 以单元音开头
                    tmp_code = self._is_diphthong(phoneme_list[1:])
                    if tmp_code == 2 or tmp_code == 1:  # 元音+元音
                        result.append([phoneme_list[0], '', 0])
                        phoneme_list.pop(0)
                    elif tmp_code == 0:  # 先元后辅
                        result.append([phoneme_list[0], phoneme_list[1], 1])
                        phoneme_list.pop(0)
                        phoneme_list.pop(0)
                elif tmp_flag == 2:  # 以双元音开头
                    tmp_code = self._is_diphthong(phoneme_list[1:])
                    if tmp_code == 2 or tmp_code == 1:  # 元音+元音
                        result.append([phoneme_list[0] + phoneme_list[1], '', 0])
                        phoneme_list.pop(0)
                        phoneme_list.pop(0)
                    elif tmp_code == 0:  # 先元后辅
                        result.append([phoneme_list[0] + phoneme_list[1], phoneme_list[2], 1])
                        phoneme_list.pop(0)
                        phoneme_list.pop(0)
                        phoneme_list.pop(0)
        return result


def write(drawAPI, reshaped_list, w, h, W, H, fontsize, style='formal'):
    for i in range(h):
        y = -fontsize * (i * 7 * 1.2)
        x = 0
        for j in range(len(reshaped_list[i])):
            if reshaped_list[i][j] == '' or reshaped_list[i][j] == ' ':
                x += fontsize * 1.73205
                continue
            if j != 0:
                x += fontsize * 1.73205 * 2
            # x = fontsize * 1.73205 * 2 * j
            BasicTunicSymbol(drawAPI.draw_symbol, reshaped_list[i][j], (x, y), style)


# def draw():
#     w = Phoneme()
#     p = w.process('banana')
#     draw_api = BasicTunicLineFormal(FONTSIZE)
#     G3 = 1.73205
#     for i in range(len(p)):
#         base = (i * 2 * G3 * FONTSIZE, 0)
#         BasicTunicSymbol(draw_api.draw_symbol, p[i], base)


if __name__ == '__main__':
    print('Done')
