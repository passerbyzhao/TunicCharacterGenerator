from basic_function import *
from style import *
import argparse

FONTSIZE = 15


class StripArgument(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values.strip())


def get_args_parser():
    parser = argparse.ArgumentParser(prog='Tunic Character Generator ')
    parser.add_argument("--sentence", action=StripArgument, default=None, help='想要翻译的原文 有空格的话请用英文双引号括起来')
    parser.add_argument("-m", "--mode", choices=['formal', 'handwriting', 'original'], default='formal',
                        help='选择输出文字的模式 默认为formal')
    parser.add_argument("-v", "--version", action='version', version='%(prog)sv0.2', help='输出版本号')
    parser.add_argument("--fontsize", type=int, default=15, help='指定字体大小 和通常意义上的字号不相通 默认为15')
    parser.add_argument("-p", "--path", default='', help='图片输出位置 默认为根目录')
    parser.add_argument('-n', '--name', default='result', help='输出图片的名称 默认为result')
    parser.add_argument('--pictype', choices=['.jpg'], default='.jpg', help='实验功能 选择输出图片格式')
    parser.add_argument('--pensize', default=4, type=int, help='笔画的粗细 默认为4')
    parser.add_argument('-c', '--pencolor', default='black', help='符号颜色 默认黑色')
    parser.add_argument('-s', '--save', action='store_false', help='是否保存图片 默认保存')
    parser.add_argument('-d', '--debug', action='store_true', help='调试用')
    return parser


def FullFuction(sentence, font_size, style='formal', pensize=4, pencolor='black', debug=False):
    if style == 'formal':
        drawAPI = BasicTunicLineFormal(font_size, pensize=pensize, pencolor=pencolor)
    elif style == 'handwriting':
        drawAPI = BasicTunicLineHandwriting(font_size, pensize=pensize, pencolor=pencolor)
    elif style == 'original':
        drawAPI = BasicTunicLineOriginal(font_size, pensize=pensize, pencolor=pencolor)
    else:
        raise Exception('文字格式错误 可选：formal handwriting, original')
    div = Division()
    phoneme = Phoneme()
    setc = SetCanvas(font_size)

    print('正在生成：{}'.format(sentence))
    sentence_list = div.divider(sentence)
    # print(sentence_list)
    mid = MiddleReplace(sentence_list, phoneme)
    mid.checker()
    phoneme_list = mid.wordtophoneme(debug)
    if debug:
        print('音标1：{}'.format(phoneme_list))
    reshaped_list = setc.reshapelist(phoneme_list)
    w, h, iW, iH, W, H = setc.setcanvas(reshaped_list)
    if debug:
        print('音标2：{}'.format(reshaped_list))
    #     print(w, h, W, H)
    write(drawAPI, reshaped_list, w, h, iW, iH, font_size, style)
    print('已成功生成')
    return w, h, iW, iH, W, H


def picsave(path='', name='result', pictype='.jpg', *args):
    from PIL import Image
    ts = tt.getscreen()
    ts.getcanvas().postscript(file="temp.eps")
    im = Image.open("temp.eps")
    w0, h0 =im.size
    w, h, iW, iH, W, H = args
    h1 = h0 * ((h*iH*1.2+0.2*iH)/H)
    w1 = w0 * ((1+w)*iW)/W
    tmp_pic = im.crop((0, 0, w1, h1))
    picpath = path+'\\'+name+pictype if path != '' else name+pictype
    tmp_pic.save(picpath)
    print('图片保存完毕')


if __name__ == '__main__':
    parser = get_args_parser()
    args = parser.parse_args()
    if args.sentence == None:
        raise ValueError('未输入要转换的单词（句子）！')
    tt.pencolor(args.pencolor)
    # sen = 'hello world'
    # sen = 'banana'
    w, h, iW, iH, W, H = FullFuction(args.sentence, args.fontsize, args.mode, args.pensize, args.pencolor, args.debug)
    # print('海龟可见性{}'.format(tt.isvisible()))
    if args.save:
        picsave(args.path, args.name, args.pictype, w, h, iW, iH, W, H)
    else:
        tt.exitonclick()

    # print('Done')
