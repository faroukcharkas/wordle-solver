class Logger:

    answer_log_calls: bool = True

    HEADER: str = '\033[95m'
    OKBLUE: str = '\033[94m'
    OKCYAN: str = '\033[96m'
    OKGREEN: str = '\033[92m'
    WARNING: str = '\033[93m'
    FAIL: str = '\033[91m'
    ENDC: str = '\033[0m'
    BOLD: str = '\033[1m'
    UNDERLINE = '\033[4m'
    
    GAME_LOG_TAG: str = f'[GAME]'
    AUTHOR_LOG_TAG: str = f'[PLYR]'

    @classmethod
    def toggle(self):
        self.answer_log_calls = not self.answer_log_calls

    @classmethod
    def log(self, message: str, author: str = '~game', nl_before: int = 0, nl_after: int = 0):
        if self.answer_log_calls == True:
            assert author == '~game' or author == '~player'

            log_tag: str = ''
            if author == '~game':
                log_tag = self.GAME_LOG_TAG
            else:
                log_tag = self.AUTHOR_LOG_TAG

            if nl_before != 0:
                print('\n'*nl_before)
            print(f'{log_tag} {message}')
            if nl_after != 0:
                print('\n'*nl_before)


    @classmethod
    def log_win(self, message: str, nl_before: int = 0, nl_after: int = 0):
        if self.answer_log_calls == True:
            if nl_before != 0:
                print('\n'*nl_before)
            print(f'{message}')
            if nl_after != 0:
                print('\n'*nl_after)

    
    @classmethod
    def log_loss(self, message: str, nl_before: int = 0, nl_after: int = 0):
        if self.answer_log_calls == True:
            print('\n'*nl_before)
            print(f'{message}')
            print('\n'*nl_after)

