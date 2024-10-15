#!/usr/bin/python3
# -- coding: utf-8 -- 
# -------------------------------
# @Author : github@wd210010 https://github.com/wd210010/only_for_happly
# @Time : 2023/10/4 16:23
# -------------------------------
# cron "0 0 2 * * *" script-path=xxx.py,tag=匹配cron用
# const $ = new Env('恩山签到')
import requests,re,os

#配置恩山的cookie 到配置文件config.sh export enshanck='' 需要推送配置推送加token export plustoken=''
enshanck = os.getenv("enshanck")
enshanck = '''_dx_captcha_cid=19271343; _dx_uzZo5y=26f4d11d1b992a61cc738948f800a72367438dbb1d0f2e6d98fbbe8b825ca9fa7e1838c4; rHEX_2132_client_created=1725346204; rHEX_2132_client_token=9E964A831826C0CF5D31FD7C56227045; rHEX_2132_connect_login=1; rHEX_2132_connect_is_bind=1; rHEX_2132_connect_uin=9E964A831826C0CF5D31FD7C56227045; rHEX_2132_nofavfid=1; rHEX_2132_study_nge_extstyle=auto; rHEX_2132_study_nge_extstyle_default=auto; rHEX_2132_smile=1D1; rHEX_2132_atarget=1; rHEX_2132_saltkey=bpRb8Q76; rHEX_2132_lastvisit=1726635983; _dx_FMrPY6=66ea6de2t3WnyT2X6yAeEf6ygwRec25F6iRDZMQ1; _dx_app_captchadiscuzpluginbydingxiang2017=66ea6de2t3WnyT2X6yAeEf6ygwRec25F6iRDZMQ1; _dx_captcha_vid=9C3F06863691323285D9DA39AF024BB4E30476386FB0EC40E55D5CE76AA341705310AA6672DEEDDDD69CECBA41A33F2A657CA3C92DA261E479D4287597259A35B63FDE998D1E187FC127DBCD1CE27DA4; rHEX_2132_auth=0be5LZHxmQ5pgWWa5BwHWZNmCYBzl5H6ujI1aWFewejK6NYo%2FCH99OCg%2FB6p9urfyrM6RFMk0ozGhdyBINEWon2S954; rHEX_2132_lastcheckfeed=960314%7C1726639601; rHEX_2132_sid=0; rHEX_2132_pc_size_c=0; https_waf_cookie=4014c843-0a99-46d33e5fd46a3744747a3ee448a5009efe3b; rHEX_2132_ulastactivity=1726829969%7C0; rHEX_2132_checkpm=1; rHEX_2132_lastact=1726829970%09home.php%09misc; rHEX_2132_sendmail=1; Hm_lvt_4fd617216d6743edf4851b17882cdd82=1726639587,1726731185,1726824851,1726829972; Hm_lpvt_4fd617216d6743edf4851b17882cdd82=1726829972; HMACCOUNT=E5085C50E6E698C6'''
#推送加 token
plustoken = os.getenv("api")
plustoken = '1234567890'
def Push(contents):
    # 设置请求头，指明发送的内容类型为 JSON
    headers = {'Content-Type': 'application/json'}
    
    # 构建 JSON 数据，其中包括推送所需的 token、标题、内容（将换行符替换为 <br>），以及模板类型
    json = {
        "token": plustoken,  # 这里的 `plustoken` 是用于认证的推送 token
        'title': '恩山签到',  # 推送的标题
        'content': contents.replace('\n', '<br>'),  # 将内容中的换行符替换为 <br> 标签
        "template": "json"  # 使用 JSON 模板
    }
    
    # 发送 POST 请求到指定的推送服务接口，并将 JSON 数据传递过去
    resp = requests.post('http://www.pushplus.plus/send', json=json, headers=headers).json()
    
    # 根据响应代码输出推送成功或失败的消息
    print('push+推送成功' if resp['code'] == 200 else 'push+推送失败')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36",
    "Cookie": enshanck,
}
session = requests.session()
response = session.get('https://www.right.com.cn/FORUM/home.php?mod=spacecp&ac=credit&showcredit=1', headers=headers)
try:
    coin = re.findall("恩山币: </em>(.*?)&nbsp;", response.text)[0]
    point = re.findall("<em>积分: </em>(.*?)<span", response.text)[0]
    res = f"恩山币：{coin}\n积分：{point}"
    print(res)
    Push(contents=res)
except Exception as e:
    res = str(e)

  
  
