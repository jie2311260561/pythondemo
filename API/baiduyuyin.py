from aip import AipSpeech


APP_ID = '17692619'
API_KEY = 'Z98pRtfNVQOGheA77PdbqSli'
SECRET_KEY = 'DMKRQo8uTuSbhtb5gamaM4bMZGNrSQGG'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
result  = client.synthesis('你好吗？', 'zh', 1, {
    'vol': 5,
})
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
       # 识别本地文件
    



def mian():
    get_file_content()
    m=client.asr(get_file_content('demo.wav'), 'wav', 16000, {'1537': 1536,})
    print(m)


# result  = client.synthesis('你好吗？', 'zh', 1, {
#     'vol': 5,
# })
# # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
# if not isinstance(result, dict):
#     with open('auido.mp3', 'wb') as f:
#         f.write(result)
