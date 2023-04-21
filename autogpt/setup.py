"""Set up the AI and its goals"""
from colorama import Fore, Style

from autogpt import utils
from autogpt.config.ai_config import AIConfig
from autogpt.logs import logger


def prompt_user() -> AIConfig:
    """Prompt the user for input

    Returns:
        AIConfig: The AIConfig object containing the user's input
    """
    ai_name = ""
    from autogpt.config.config import Config
    cfg = Config()

    # Construct the prompt
    logger.typewriter_log(
        cfg.prompt.UPROMP_WELCOME,
        Fore.GREEN,
        cfg.prompt.UPROMP_RUN_WITH_HELP,
        speak_text=True,
    )

    logger.typewriter_log(
        cfg.prompt.UPROMP_CREATE,
        Fore.GREEN,
        cfg.prompt.UPROMP_LOADDEF,
        speak_text=True,
    )

    # Get AI Name from User
    logger.typewriter_log(
        cfg.prompt.UPROMP_NAMEAI, Fore.GREEN, cfg.prompt.UPROMP_NAMECASE
    )
    ai_name = utils.clean_input(cfg.prompt.UPROMP_AINAME)
    if ai_name == "":
        ai_name = cfg.prompt.UPROMP_DEFNAME

    logger.typewriter_log(
        cfg.prompt.UPROMP_AIHERE.format(ai_name),
        Fore.LIGHTBLUE_EX,
        cfg.prompt.UPROMP_READYFORSVS,
        speak_text=True
    )

    # Get AI Role from User
    logger.typewriter_log(
        cfg.prompt.UPROMP_DESCRIBE_ROLE,
        Fore.GREEN,
        cfg.prompt.UPROMP_ROLE_EXAMPLE,
    )
    ai_role = utils.clean_input(cfg.prompt.UPROMP_AI_IS.format(ai_name))
    if ai_role == "":
        ai_role = cfg.prompt.UPROMP_DEFAULT_ROLE

    # Enter up to 5 goals for the AI
    logger.typewriter_log(
        cfg.prompt.UPROMP_ENTER_GOALS,
        Fore.GREEN,
        cfg.prompt.UPROMP_GOAL_EXAMPLES,
    )
    print(cfg.prompt.UPROMP_GOAL_FINISH, flush=True)
    ai_goals = []
    for i in range(5):
        ai_goal = utils.clean_input(
            cfg.prompt.UPROMP_GOAL.format(Fore.LIGHTBLUE_EX, Style.RESET_ALL, i+1))
        if ai_goal == "":
            break
        ai_goals.append(ai_goal)
    if not ai_goals:
        ai_goals = cfg.prompt.UPROMP_DEFAULT_GOALS

    return AIConfig(ai_name, ai_role, ai_goals)
