# -*- coding:gbk -*-

import requests
from lxml import html

def getLotteryNode():
    url = 'http://kaijiang.500.com/index3.shtml?0'
    response = requests.get(url).content
    selector = html.fromstring(response)
    colnames = selector.xpath('/html/body/div/div[@id="content1"]/table/tbody[1]/tr/td/text()')
    happy8 = selector.xpath('/html/body/div/div[@id="content1"]/table/tbody[@id="bj"]/tr[@id="row_kl8"]/td')
    resultcol = []
    result = {}
    for node in happy8:
        resultcol.append(html.tostring(happy8[1]))
        if len(colnames) == len(happy8) + 1:

    for name in colnames:
        if name == u'å°åº' or name == u'å¼å¥è¯¦æ' or name == u'èµ°å¿å¾':
            continue
        if name == u'å½©ç§å':
            selectorTmp = html.fromstring(html.tostring(happy8[0]))
            result[name] = selectorTmp.xpath('//a/text()')[0]
        if name == u'æå·':
            tmp = html.tostring(happy8[1])
            selectorTmp = html.fromstring(html.tostring(happy8[1]))
            tmp = selectorTmp.xpath('//td/text()')[0]
            result[name] = selectorTmp.xpath('//td/text()')[0]
        if name == u'å¼å¥æ¶é´':
            tmp = html.tostring(happy8[2])
            selectorTmp = html.fromstring(html.tostring(happy8[2]))
            tmp = selectorTmp.xpath('//td/text()')[0]
            result[name] = selectorTmp.xpath('//td/text()')[0]
        # if name == u'å¼å¥å·ç ':
        # if name == u'ææ°/æ¯å¤©':
        # if name == u'å¼å¥é¢ç':


if __name__ == '__main__':
    lottryNode = getLotteryNode()


