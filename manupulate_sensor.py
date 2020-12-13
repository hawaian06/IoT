#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:58:57 2020

センサーからデータを出力するクラス；
・GetSensorData
センサーへデータを入力するクラス：
・InputSensorData
を実装している。

@author: pi
"""



from sense_hat import SenseHat


class GetSensorData():
    """
    class Explanation:
        ラズパイに接続したセンサーからデータを取得する関数をまとめたもの。
    Args:
        Attuributes:
        
        functions:
            sense_hat :
                ラズパイに接続するSenseHatからデータを取得する関数。
                

    """
    def sense_hat(pressure : bool = True,
                  humidity : bool = True,
                  temperature : bool = True,
                  ) -> dict:
        """
        Explanation:
            SenseHatから温度、湿度、気温を出力する関数。
            
        Input:
            pressure : bool
                気圧を取得するかどうかを決める。
                True（default）ならば取得する。
            humidity : bool
                湿度を取得するかどうかを決める。
                True（default）ならば取得する。
            temperature : bool
                気温を取得するかどうかを決める。
                True（default）ならば取得する。
                
        Return:
            output : dict
                取得したデータをdictのvalueに格納して出力する。
                keyは'pressure', 'humidity', 'temparature'であり、
                InputでTrueとしたものは、センサーの値が格納され、
                TrueでなければNoneが格納される。
            
        """
        # 箱作成
        output = {'pressure' : None,
                  'humidity' : None,
                  'temperature' : None}
        # センサーデータの取得、格納
        sense = SenseHat()
        if pressure == True:
            output['pressure'] = sense.get_pressure()
        if humidity == True:
            output['humidity'] = sense.get_humidity()
        if temperature == True:
            output['temperature'] = sense.get_temperature()
        
        # 出力
        return output

"""
sense = SenseHat()
red = (255, 0, 0)
blue = (0, 255, 0)
sense.show_message("How cool is this?", text_colour = red, back_colour = blue)
sense.clear()
SenseHat
"""



sense = SenseHat()
sense.clear()

pressure = sense.get_humidity()
print(pressure)
