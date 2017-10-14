#数据库
*添加数据库操作命令使用Migrate的add_command,第一个参数是想使用的命令名，第二个参数是flask-migrate的MigrateCommand
*当数据库模型变化的使用，使用flask-migrate做数据库的更新，分别执行migrate和upgrade。
#发送邮件
*使用flask-mail发送邮件注意点：
1 所指定的发送者的邮箱需要开启smtp功能 
2 每个邮箱的smtp可以通过搜索引擎找到
3 配置中的MAIL_PASSWORD有可能是发送邮箱的密码(网易等)，还可能是此邮箱提供的一个单独的验证码(qq邮箱等)，具体看邮箱的说明
4 配置中的MAIL_USERNAME可以是去除尾部之后的用户名或者是邮箱账号
5 MAIL_DEFAULT_SENDER为默认的发送邮箱，或者在构建Message时候指定sender，sender结构为"发送者名 邮箱"发送这名可以省掉，或者是个元表(发送者名,邮箱)
6 还要注意是否打开SSL问题，如果打开，则配置里的端口要相应修改(各个邮箱不同，可以搜索找到)
