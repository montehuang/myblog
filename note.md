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

#用户确认
*生成和检验token，可以分别使用itsdangerous包里的dumps和loads来实现。具体使用方法参看文档。
*发送的确认邮件，内容是一个html格式的文件。其中包含一个跳转到自己网站的链接，然后在这个链接找到对应的路由函数，进而完成确认。
*确认链接中一个注意点，就是相应的url_for需要一个参数赋值，_external = True,就可以生成完整的URL，包含协议，主机号，端口。确认的时候还需要将token作为链接的一部分传给视图函数进行处理。

#请求钩子的使用
*在请求之前或者之后调用的函数，可以避免视图函数中的重复代码。Flask中包含四个：
*before_first_request*,*before_request*,*after_request*,*teardown_request*.功能查文档。
*想在蓝图中使用针对程序全局请求的钩子，必须使用
*befroe_app_request*等修饰器

#flask-login
*提供了用户登陆，登出等功能