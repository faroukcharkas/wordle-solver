class Logger:

    HEADER: str = '\033[95m'
    OKBLUE: str = '\033[94m'
    OKCYAN: str = '\033[96m'
    OKGREEN: str = '\033[92m'
    WARNING: str = '\033[93m'
    FAIL: str = '\033[91m'
    ENDC: str = '\033[0m'
    BOLD: str = '\033[1m'
    UNDERLINE = '\033[4m'
    
    GAME_LOG_TAG: str = f'{BOLD}[GAME]'
    AUTHOR_LOG_TAG: str = 'f{OKCYAN}[PLYR]'

    def log(self, message: str, author: str = '~game', nl_before: int = 0, nl_after: int = 0):
        assert author == '~game' or author == '~system'

        log_tag: str = ''
        if author == '~game':
            log_tag = self.GAME_LOG_TAG
        else:
            log_tag = self.AUTHOR_LOG_TAG

        print('\n'*nl_before)
        print(f'{log_tag} {message}')
        print('\n'*nl_after)


    def log_win(self, message: str, nl_before: int = 0, nl_after: int = 0):
        print('\n'*nl_before)
        print(f'{self.OKGREEN} {message}')
        print('\n'*nl_after)

    
    def log_loss(self, message: str, nl_before: int = 0, nl_after: int = 0):
        print('\n'*nl_before)
        print(f'{self.FAIL} {message}')
        print('\n'*nl_after)

