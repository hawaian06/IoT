#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:58:57 2020

Gdriveにデータを上げるための関数。
・UploadGdrive
Gspreadを操作するための関数
・ManupulateGspread

@author: pi
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class UploadGdrive():
    """
    Explanation:
        Gdriveにデータを上げるための関数をまとめたもの。
    """
    pass

class ManupulateGspread():
    """
    Explanation:
        GspreadSheetを作成したり、保存したりする関数。
    
    Args:
        Attributes:
            self.SCOPE : list
                google drive, GspreadのURLをリストにまとめたもの。
                認証を得る際に用いる。
            self.credentials : 
                
            self.sheet : 
                開いたGspread。ここにデータを書き込む。
            
        functions:
            self.open : 
                Gspreadを開く関数。
        
    """
    def __init__(self,
                 service_key_name : str):
        """
        Input:
            service_key_name : str
                サービスアカウントキー名（jsonファイル）
        """
        # 定数
        self.SCOPE = [
                'https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive'
                ]
        # 変数
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
                service_key_name,
                self.SCOPE)
        self.sheet = None
        
        
    def open(self,
             name_use : bool = False,
             key_use : bool = False,
             url_use : bool = False,
             name : str = None,
             key  : str = None,
             url  : str = None):
        """
        Expalanation:
            spreadsheetを開くための関数。
            開け方には、ファイル名, シートのkey, URLの三通りがあり、全て実装している。

        Input:
            name_use : bool
                ファイル名を用いてspreadsheetを開くかどうかを決める。
                Trueならファイル名を用いて開く。
             key_use : bool
                key名を用いてspreadsheetを開くかどうかを決める。
                Trueならkey名を用いて開く。
             url_use : bool
                URLを用いてspreadsheetを開くかどうかを決める。
                TrueならURLを用いて開く。
             name : str
                 ファイル名。name_useがTrueの際に指定する。
             key  : str
                 key名。key_useがTrueの際に指定する。
             url  : str
                 url。url_useがTrueの際に使用する。
        
        Return:
            (None.)
                スプレッドシートを開く。
        """
        # ファイルの開き方で分岐が生じる。
        if name_use == True:
            self.sheet = self.credentials.open(name)
        if key_use == True:
            self.sheet = self.credentials.open_by_key(key)
        if key_use == True:
            self.sheet = self.credentials.open_by_url(url)
            