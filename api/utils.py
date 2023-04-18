def create_dict(producer_name: str, interval: int, previous_win: int, following_win: int) -> dict:
            return {
                    'producer': producer_name,
                    'interval': interval,
                    'previousWin': previous_win,
                    'followingWin': following_win
                    }


