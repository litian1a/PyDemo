# -*- coding: utf-8 -*-

# @Author  : Skye
# @Time    : 2018/1/8 20:38
# @desc    : 答题闯关辅助，截屏 ，OCR 识别，百度搜索


from PIL import Image
from common import screenshot, ocr, methods
from threading import Thread
import requests
import json
import time
import sys

lastQuestionId=0
while True:
    # 截图
    # screenshot.check_screenshot()
    print('------------------------')

    # img = Image.open("./screenshot.png")
    try:
        # req = requests.get(url='http://htpmsg.jiecaojingxuan.com/msg/current').text
        # print(req)
        # req='{"code":0,"msg":"成功","data":{"event":{"answerTime":10,"desc":"12.在节目《国家宝藏》中出现的《千里江山图》作者是   ","displayOrder":11,"liveId":97,"options":"[\"于蕾 \",\"李晨\",\"王希孟\"]","questionId":1113,"showTime":1515676395781,"status":0,"type":"showQuestion"},"type":"showQuestion"}}'
        req='{"code":0,"msg":"成功","data":{"event":{"answerTime":10,"desc":"12.中国古代\\"双手抱拳举过头顶,鞠躬\\",表达什么意思?","displayOrder":11,"liveId":98,"options":[\"稽首\",\"长揖\",\"顿首\"],"questionId":1185,"showTime":1515734140999,"status":0,"type":"showQuestion"}}}'


        req=req.replace("\"[","[")
        req=req.replace("]\"","]")

        startIndex=req.find("[")
        endIndex=req.find("]")
        array=req[startIndex:endIndex]

        newArray=array.replace("\\","")
        req=req.replace(array,newArray)

        content = json.loads(req )


        if content['msg']== '成功':

            print(req)

            questionId=content['data']['event']['questionId']
            question=content['data']['event']['desc']
            choices=content['data']['event']['options']
            # 多线程
            if lastQuestionId!=questionId:
                m1 = Thread(methods.run_algorithm(0, question, choices))
                m1.start()

                # m1 = Thread(methods.run_algorithm(0, question, choices))
                m2 = Thread(methods.run_algorithm(1, question, choices))
                m3 = Thread(methods.run_algorithm(2, question, choices))
                # m1.start()
                m2.start()
                m3.start()
            lastQuestionId=questionId

            # end_time = time.clock()
            # print(end_time - t)


            print('------------------------')
    except Exception as e:
        # as 加原因参数名称
        print(str(e))

    time.sleep(1)


