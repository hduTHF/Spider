from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
import re

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_mail(title,href,source,time,content=''):

    form_addr = 'thfsec@163.com'
    # 不是邮箱密码,而是开启SMTP服务时的授权码
    password = 'thf1995'
    # 收件人的邮箱
    to_addr = ['thf_1995@163.com']
    # qq邮箱的服务器地址

    smpt_server = 'smtp.163.com'

    messag='<html><head></head><body><h1><a href=%s>%s</a></h1><p>%s</p></br>time:%s 来源：%s</body></html>'%(href,title,content,time,source)
    # 设置邮件信息
    msg = MIMEText(messag, 'html', 'utf-8')
    msg['From'] = _format_addr('安全监控 <%s>' %form_addr)
    msg['To'] = _format_addr('管理员 <%s>' %to_addr)
    msg['Subject'] = Header('预警', charset='utf-8').encode()

    # 发送邮件
    server = smtplib.SMTP(smpt_server, port=25)
    server.set_debuglevel(1)
    server.login(form_addr, password)
    server.sendmail(form_addr, to_addr, msg.as_string())
    server.quit()

if __name__ == '__main__':
    title='Dahua Dual Imager Dome Camera Tested (HDBW4231FN-E2-M)'
    a = re.search(r'dahua|hik|hikvision|uniview|camera|vulner', title, re.IGNORECASE)
    if a.group():
        send_mail('dahua','http://www.baidu.com','ipvm','2018-10-31','test')