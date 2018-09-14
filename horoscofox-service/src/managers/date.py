from datetime import datetime, timedelta, date


class DateManager(object):
    today = date.today()
    tomorrow = today+timedelta(days=1)

    @staticmethod
    def get_date(kind: str):
        if kind == 'today':
            return DateManager.reset(DateManager.today)
        if kind == 'tomorrow':
            return DateManager.reset(DateManager.tomorrow)

    @staticmethod
    def reset(date):
        return datetime.combine(date, datetime.min.time())
