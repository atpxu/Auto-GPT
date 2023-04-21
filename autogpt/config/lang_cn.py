# !/usr/bin/env python
# coding=utf-8


HINT_THINKING = "思考中..."
HINT_LIMIT_REACHED = "达到步骤上限: "
HINT_NEXT_ACTION = "下一步: "
HINT_NEED_AUTH = "输入'y'授权Command, " \
                 "'y -N'授权连续执行N个Commands, " \
                 "'n'退出程序, 或者输入需要反馈的内容给"
HINT_INPUT = "输入:"
HINT_INVALID_INPUT = "输入错误. 请输入'y -n', 其中n表示要连续执行的Commands数量."
HINT_AUTHORISED = "-=-=-=-=-=-=-= COMMAND 已得到用户授权 -=-=-=-=-=-=-="
HINT_EXITING = "退出..."
HINT_SYSTEM = "系统: "
HINT_UNABLE_EXECUTE = "命令执行失败"

MEM_TYPE = "存储类型使用:"
BROWSER_TYPE = "浏览器使用:"

HINT_NAME = "名字:"
HINT_ROLE = "任务:"
HINT_GOALS = "目标:"
HINT_WELCOME = "欢迎回来！"
HINT_WCQST = "您是否需要我继续作为{}为您服务?"
HINT_CONT = "保持原有设定?"
HINT_CONT2 = "继续 (y/n): "
HINT_SHOULD_CONTINUE = "保持原有设定?\n名字:  {}\n任务:  {}\n目标: {}\n继续 (y/n): "

UPROMP_WELCOME = "欢迎使用 Auto-GPT! "
UPROMP_RUN_WITH_HELP = "使用'--help'启动获取更多帮助信息."
UPROMP_CREATE = "创建一个AI助理:"
UPROMP_LOADDEF = "输入AI的名字和它的角色任务. 空输入将使用默认值."
UPROMP_NAMEAI = "为您的AI取名: "
UPROMP_NAMECASE = "例如, '企业家-GPT'"
UPROMP_AINAME = "AI名字: "
UPROMP_DEFNAME = "企业家-GPT"
UPROMP_AIHERE = "这里是{}!"
UPROMP_READYFORSVS = "我已准备好为您服务."
UPROMP_DESCRIBE_ROLE = "您的AI所扮演角色任务是: "
UPROMP_ROLE_EXAMPLE = "例如: '通过自主开发和经营企业，实现公司净值目标的AI.'"
UPROMP_AI_IS = "{}是: "
UPROMP_DEFAULT_ROLE = "通过自主开发和经营企业，实现公司净值目标的AI."
UPROMP_ENTER_GOALS = "为您的AI输入最多5个目标: "
UPROMP_GOAL_EXAMPLES = "例如: \n增加企业净值，运营Twitter账号并增粉，自主开发和管理多个企业"
UPROMP_GOAL_FINISH = "输入空目标则表示输入结束，如果所有目标为空则使用默认值."
UPROMP_GOAL = "{}目标{} {}: "
UPROMP_DEFAULT_GOALS = [
    "增加企业净值",
    "运营Twitter账号并增粉",
    "自主开发和管理多个企业",
]

REPLY_THOUGHTS = "思考:"
REPLY_REASONING = "理由:"
REPLY_PLAN = "计划:"
REPLY_CRITICISM = "自省:"
REPLY_SPEAK = "说:"
